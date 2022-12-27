# -*- coding: utf-8 -*-

import scrapy
import scrapy.exceptions
from pagecrawler.items import PagecrawlerItem
import socket
import logging
import datetime
import os
import winsound

# - Eingabeparameter -
spidername = 'schulcrawler'
depth = 0
download_delay = 5
abort_id = 0  # Bei Abbruch/Beendigung: 0 nichts, 1 herunterfahren nach Sekunden, 2 pausieren (weiter mit Eingabe)
shutdown_time = 20  # Sekunden bis zum Herunterfahren
beep_finish = False  # peep machen bei Abbruch/Beendigung
# log_level = logging.INFO
log_level = "INFO"
with open(r"C:\Users\Katzi\HiDrive\Emigration\alt\Deutsche Schulen\Deutsche_Schulen URLs-test.csv", "rt", encoding="utf-8", errors="replace") as f:
    start_urls = [url.strip() for url in f.readlines()]
psu_xpath = None#'//div[@class="section-two"]//a/@href'  # Xpath-Pfad-String für zu extrahierende Links wenn parse_start_url verwendet werden soll

time_now = f"{datetime.datetime.now():%d-%m-%Y %H°%M}"

class BaseSpider(scrapy.Spider):
    name = spidername
    start_urls = start_urls
    custom_settings = {
        'DEPTH_LIMIT': depth,
        'DOWNLOAD_DELAY': download_delay,
        'LOG_LEVEL': log_level,
        'FEEDS': {'%s.csv' % name: {'format': 'csv', }}
    }

    logging.basicConfig(  # Log-Einstellungen festlegen
        filename='log-%s-%s.txt' % (time_now, name),
        format='%(levelname)s: %(message)s',
        level=log_level  # DEBUG oder INFO für mehr Infos
        # level=log_level.INFO  # DEBUG oder INFO für mehr Infos
    )
    ip_ref = socket.gethostbyname('Katzi')  # Momentane IP-Adresse speichern für Referenzzwecke (IP-Abriss, s.u.)

    # Auslesen der Verzeichnisstruktur; auskommentieren beim Debugging für das scrapen nur der Hauptseite
    if psu_xpath:
        def parse_start_url(self, response):  # optionale Funktion (überschreiben des Default)
            for url in response.xpath(psu_xpath):
                logging.info('parse_start_url: %s' % url)
                yield scrapy.Request(url.get(), callback=self.parse)

    # def parse_item(self, response):
    def parse(self, response):
        self.ipcheck()  # IP-Identität ggü. des Beginns checken zum Testen VPN-Abriss
        self.logger.info('Scraping parse_item von: %s' % response.url)

        item = PagecrawlerItem()
        item['Name'] = response.xpath('//div[@class="content-element content-element-text"]//h1//text()').extract()
        item['AP'] = response.xpath('//p[@class="subline no-glossary-index"]//text()').extract()
        item['Funktion'] = response.xpath('//p[@class="no-glossary-index"]//text()')[0].extract()
        item['Telefon'] = response.xpath('//p[@class="no-glossary-index"]//text()')[2].extract()
        item['Mail'] = response.xpath('//p[@class="no-glossary-index"]//text()')[4].extract()
        item['Adresse'] = response.xpath('//p[@class="margin no-glossary-index"]//text()').extract()
        item['website'] = response.xpath('//a[@target="_blank"]//text()')[0].extract()
        item['Schuljahresbeginn'] = response.xpath('//p[@class="no-glossary-index"]//text()')[11].extract()

        yield item
        # yield {'Name': Name, 'Strasse': AP, 'Ort': ort, 'PLZ': plz, 'Staat': state, 'Land': land, 'Website': website,
        #        'Telefon': telefon}

    # Check für IP-Abriss
    def ipcheck(self):
        ip_now = socket.gethostbyname('Katzi')  # IP-Check für VPN-Abriss
        # Bei IP-Abriss, Ablauf unterbrechen durch Eingabeaufforderung,  optional herunterfahren
        if ip_now != self.ip_ref:
            logging.error("IP-Abriss")  # Scrapy print statement on info level (alt: error/warning)
            self.abortprocedure()
        return

    # Methode für Abbruch/Beendigung:
    def abortprocedure(self):
        # Tonsignal
        if beep_finish is not False:
            winsound.Beep(1000, 2000)
        # Weiteres Verfahren
        if  abort_id == 0:  # nichts machen
            # logging.error("Eingabefahler für %s oder %s; - Programm wird regulär beendet" % (beep_finish, abort_id) )
            pass
        elif abort_id == 1:  # Herunterfahren
            os.system("shutdown -s -t %s" % shutdown_time)  # shutdown ausführen
            # raise scrapy.exceptions.CloseSpider('Scrapy beendet. Fahre Computer herunter')  # Crawl abbrechen/beenden
        # Folgende bedarf Überarbeitung!
        elif abort_id == 2:  # Pausieren mit Warten auf Eingabe
            input("Beendet bzw. unterbrochen. Beliebige Taste drücken zum Fortfahren; STRG-C für Abbruch")
            self.ip_ref = socket.gethostbyname('Katzi')  # Neue IP-Adresse für die Referenz speichern

    # Interne Methode, die beshreibt, was nach Beendigung geschehen soll
    def close(self, spider, reason="finished"):
        # logging.info("Inside close-Method! - Shutting Down")
        self.abortprocedure()


# process = PagecrawlerProcess(settings=get_project_settings)
# process.crawl(PagecrawlerSpider)
# process.start()
