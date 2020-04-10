# YetAnotherWoldometerCovidBot
My implementation of a bot that preriodically fetchs the Woldometer Coronavirus page and updates a JSON file with all its data.

I had more features planned for my bot, but I decided to abandon it as there are lots of people already gathering data and I have more interesiting proyects in mind.

 - mainScript.py:
Contains the bot. With the default configuration will fetch and process the web every 3h. It can store the page in /rawData. It is recomended to not lose data in case the page desing is updated. 

 - manualExportCsv.py:
 Little script to extract from the JSON file into to a csv all data from an specific Country

 - manualProcessAllRawData.py:
Processes all data in /rawData and generates a new JSON file. Usefull when processing older data or data after a page change

 - loggerConfig.py:
I used the python logger to send myself an email when an error ocurrs. This file configures this and other log options.

Requeriments:
Python3 and BeautifulSoup4
