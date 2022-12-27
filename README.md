# scrape-Deutsche-Schulen
scrape german international schools

## Disclaimer
This is for educational purpose only. I won't be responsible for any misuse.

## Motivation
Get a better, structured overview or do analysis on this data of German international schools.

## Procedure and result

The following data is being extracted and saved into a `csv` spreadsheet:

- name of school
- contact person
- role of contact person (usually principal or vice principal)
- his/her telephone number
- his/her email address
- address of school
- website of school
- begin of school year

<img src="https://github.com/dossma/scrape-Deutsche-Schulen/blob/main/example_pictures/Dt_Schulen_csv_screenshot.jpg" width=100% height=100%>
<img src="https://github.com/dossma/scrape-Deutsche-Schulen/blob/main/example_pictures/Dt_Schulen_Gmaps_screenshot.jpg" width=100% height=100%>

## Get started
After the development setup has been established (see below), go to the `spiders` directory and run with

`scrapy runspider schulcrawler.py`

The result will be saved under `schulcrawler.csv`

## Development setup
Required is
- Scrapy: https://github.com/scrapy/scrapy

```sh
pip install scrapy
```

## Meta

Author: Jonas Dossmann

Distributed under the AGPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)
