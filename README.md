# scrape-Deutsche-Schulen
scrape german international schools

## Motivation
Get a better, structured overview or do analysis on existent German international schools.

## Disclaimer
<!-- The Terms of Service of the data source do not prohibit extraction and the data is publicly available. -->
The data is publicly available and no terms of service could be found, therefore extraction is deemed permitted.  
Use this code only in an ethical way and without violating the law. 

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

`scrapy runspider Dt_Schulen.py`

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
