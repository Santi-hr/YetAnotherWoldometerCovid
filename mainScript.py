import time
import logging
import loggerConfig
import timeHelper
import combineJsonWorldometerFcns
import parseWorldometerFcns
import fetchWorldometer

saves_per_day = 8

loggerConfig.loggerInit()
logger = logging.getLogger("Main")

while True:
    [next_datetime, next_delay] = timeHelper.get_next_daily_iteration(saves_per_day)
    logger.info("Next save at %s. Waiting %d seconds", next_datetime, next_delay)
    # time.sleep(next_delay)

    [web_data, web_successful, web_datetime] = fetchWorldometer.fetch_worldometer(flag_save_raw_copy=True)

    if web_successful:
        dict_raw_data = parseWorldometerFcns.extract_dict_from_worldometer_html(web_data)
        if dict_raw_data is None:
            logger.error("An error occurred while parsing the webpage")
        else:
            combineJsonWorldometerFcns.append_worldometer_into_output_json(dict_raw_data, web_datetime)
    time.sleep(10)

exit(1)
