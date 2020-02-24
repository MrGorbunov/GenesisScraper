#Genesis Scraper

##Run Down

This program scrapes grades and sends text notifications about any changes. Was created solo
by Michael Gorbunov at HackJA 2020.

Written in Python. Uses Twilio for texting (is a wrapper class so can be easily changed), 
and Selenium with chromedriver for scraping. Scraping is specific to the 
Genesis online gradebook, which is what my district uses (unlike Canvas, no API).

To run this, you must hardcode credentials for Twilio, but Genesis credentials are taken at
runtime. This repo uses version 80 of chromedriver.




##Testing Locally
Grades don't change often enough to really be testable. For this reason, there is a
Genesis-sourced .htm file in the repo. To scrape from it instead of the online Genesis, go
to _driver.py_ and change the following:

comment out line 97, ```d.login(getpass.getPass(), getpass.getPass())```

change line 24  ```.getData()``` to ```.getDataFrom("LocalGenesis.htm)```




##.jsons

####config.json
_delay_: Specifies the internal between scrapes. Parses one letter which can be S, M, H, D, or W
corresponding to seconds, minutes, hours, days, or weeks

_sentimental messages_: Adds a little message to the end of texts depending on the change in
grades since last text

_recap mode_: Instead sending only updates, will send all grades showing their change from
last text. Implied that _delay_ should be high (1 W), because it texts with every scrape

####config_sentiments.json
Stores messages to be sent based on change in grades. Will only be used if _sentimental messages_
is turned on.

####data.json
The data from the last scrape, stored in json for far easier parsing.



