import urllib.request
import urllib.error
from datetime import datetime
import time
import logging

logger = logging.getLogger("Main."+__name__)


def fetch_web(str_url_in, max_tries=5, time_between_tries_s=600):
    """Use request library to fetch a web page"""
    # Generate request emulating a web browser
    req = urllib.request.Request(
        str_url_in,
        data=None,
        headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
        }
    )

    # Initialize outputs
    url_request_successful = False
    output_data = None

    # Try N times the request
    for n_try in range(max_tries):
        try:
            logger.info("Fetching %s, Try: %d", str_url_in, n_try)
            output_data = urllib.request.urlopen(req)
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            logger.warning("Error fetching web", exc_info=1)
            logger.info("Waiting: %d s", time_between_tries_s)
        else:
            #TODO: Check size of recieved data
            url_request_successful = True
            break
        # Wait between tries to allow the page to recover
        time.sleep(time_between_tries_s)

    return [output_data, url_request_successful]


def fetch_worldometer(flag_save_raw_copy):
    """Fetchs the Worldometer coronavirus web and optionally saves a copy of the raw html"""
    [web_response, web_successful] = fetch_web("https://www.worldometers.info/coronavirus")
    web_datetime = datetime.now()

    if web_successful:
        if flag_save_raw_copy:
            output_filename = "rawData/corona" + web_datetime.strftime("%Y%m%d_%H%M%S") + ".html"
            logger.info("Saving data: %s", output_filename)
            with open(output_filename, 'w', encoding="utf-8") as file:
                web_data_str = web_response.read().decode("utf-8")
                file.write(web_data_str)
    else:
        logger.error("Failed fetching web data")

    return [web_data_str, web_successful, web_datetime]
