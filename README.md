# scrape-Deutsche-Schulen
scrape german schools worldwide

## Disclaimer
This is for educational purpose only. I won't be responsible for any misuse.

## Motivation
Get a better, structured overview or do analysis on where German international schools are located and further specifics.

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

<img src="https://github.com/dossma/scrape-CAMX/blob/main/snapshot.jpg" width=100% height=100%>
<img src="https://github.com/dossma/scrape-CAMX/blob/main/Gmaps%20screenshot%20w%20profile.jpg" width=100% height=100%>

## Get started
After the development setup has been established (see below), run

`scrapy crawl schulcrawler`

The result will be saved under the 

## Development setup
Prominent required external library is
- Scrapy: https://github.com/scrapy/scrapy

```sh
pip install scrapy
```

## Meta

Author: Jonas Dossmann

Distributed under the AGPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)
