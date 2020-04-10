import logging
from datetime import datetime
import json
import os
import time
import loggerConfig
import combineJsonWorldometerFcns
import parseWorldometerFcns

# This scripts reads all raw Worldometer.html files from a folder and generates a .json file with all the data
# The script expect all files to be ordered and have an specific name
loggerConfig.loggerInit()
logger = logging.getLogger("Main")
logger = logging.getLogger("Main."+__name__)

dict_all_data = dict()
dict_all_data["Datetime_str"] = []

folder = "rawData"

list_files = os.listdir(folder)

temp_start_time = time.perf_counter()
for filename in list_files:
    file_path = folder + '/' + filename
    logger.info("Processing %s", file_path)

    # 0. Abrir archivo y tomar datos html
    with open(file_path, 'r', encoding="UTF-8") as f:
        html_data = f.read()

    dict_raw_data = parseWorldometerFcns.extract_dict_from_worldometer_html(html_data)

    if dict_raw_data is None:
        logger.error("An error occurred while parsing the webpage")
        break

    file_datetime = datetime.strptime(filename, "corona%Y%m%d_%H%M%S.html")
    combineJsonWorldometerFcns.combine_worldometer_dicts(dict_all_data, dict_raw_data, file_datetime)


with open('coronavirusData.json', 'w', encoding="UTF-8") as fp:
    json.dump(dict_all_data, fp, sort_keys=True, indent=4, ensure_ascii=False)

ellapsed_time = time.perf_counter()-temp_start_time
logger.debug("Took %f seconds (avg. %f per file)", ellapsed_time, ellapsed_time/len(list_files))