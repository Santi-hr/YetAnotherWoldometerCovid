from bs4 import BeautifulSoup
from collections import defaultdict
import logging
import re

def helper_convert_to_num(input_text):
    """Sanitizes the text input from the html to ensure proper conversion and converts it"""
    output_num = 0
    input_text = input_text.replace(' ', '')
    input_text = input_text.replace('   ', '')
    input_text = input_text.replace(',', '')
    if input_text is not '':
        if re.match("\d*\.?\d+\Z", input_text): # Prevent anything not number shaped to be casted
            if '.' in input_text:
                output_num = float(input_text)
            else:
                output_num = int(input_text)

    return output_num


def helper_format_country_name(input_text):
    """Sanitizes the text input from the html"""
    input_text = input_text.strip()
    output_text = input_text.replace(':', '')

    if input_text == "United Kingdom":
        output_text = "UK"
    elif input_text == "United Arab Emirates":
        output_text = "UAE"
    elif input_text == "United States":
        output_text = "USA"

    return output_text


def extract_data_4_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0,
                  "Serious_cases": 0, "Cases_per_1M": 0, "Deaths_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())


    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[2].text)
            # 3 - Region

    return dict_raw_data


def extract_data_5_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0,
                  "Serious_cases": 0, "Cases_per_1M": 0, "Deaths_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())


    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            # Cases change
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            # Region

    return dict_raw_data


def extract_data_6_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0,
                  "Serious_cases": 0, "Cases_per_1M": 0, "Deaths_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())


    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            # Cases change
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            # Death change
            # Region

    return dict_raw_data


def extract_data_8_columns_with_region(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0,
                  "Serious_cases": 0, "Cases_per_1M": 0, "Deaths_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())


    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            # Cases change
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            # Death change
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[5].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[6].text)
            # Region

    return dict_raw_data


def extract_data_8_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())


    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            # Cases change
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            # Death change
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[5].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[7].text)

    return dict_raw_data


def extract_data_9_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())

    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[5].text)
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[7].text)
            dict_raw_data[country_name]["Cases_per_1M"] = helper_convert_to_num(row_data[8].text)

    return dict_raw_data


def extract_data_10_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 10 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())

    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[5].text)
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[7].text)
            dict_raw_data[country_name]["Cases_per_1M"] = helper_convert_to_num(row_data[8].text)
            dict_raw_data[country_name]["Deaths_per_1M"] = helper_convert_to_num(row_data[9].text)

    return dict_raw_data


def extract_data_12_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 12 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())

    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[5].text)
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[7].text)
            dict_raw_data[country_name]["Cases_per_1M"] = helper_convert_to_num(row_data[8].text)
            dict_raw_data[country_name]["Deaths_per_1M"] = helper_convert_to_num(row_data[9].text)
            dict_raw_data[country_name]["Total_Tests"] = helper_convert_to_num(row_data[10].text)
            dict_raw_data[country_name]["Tests_per_1M"] = helper_convert_to_num(row_data[11].text)

    return dict_raw_data


def extract_data_13_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 12 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0, "Continent": ""}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())

    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[0].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[1].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[3].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[5].text)
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[7].text)
            dict_raw_data[country_name]["Cases_per_1M"] = helper_convert_to_num(row_data[8].text)
            dict_raw_data[country_name]["Deaths_per_1M"] = helper_convert_to_num(row_data[9].text)
            dict_raw_data[country_name]["Total_Tests"] = helper_convert_to_num(row_data[10].text)
            dict_raw_data[country_name]["Tests_per_1M"] = helper_convert_to_num(row_data[11].text)
            dict_raw_data[country_name]["Continent"] = row_data[12].text

    return dict_raw_data

def extract_data_15_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 12 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0, "Continent": "",
                  "Population": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())

    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[1].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[2].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[4].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[7].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[8].text)
            dict_raw_data[country_name]["Cases_per_1M"] = helper_convert_to_num(row_data[9].text)
            dict_raw_data[country_name]["Deaths_per_1M"] = helper_convert_to_num(row_data[10].text)
            dict_raw_data[country_name]["Total_Tests"] = helper_convert_to_num(row_data[11].text)
            dict_raw_data[country_name]["Tests_per_1M"] = helper_convert_to_num(row_data[12].text)
            dict_raw_data[country_name]["Population"] = helper_convert_to_num(row_data[13].text)
            dict_raw_data[country_name]["Continent"] = row_data[14].text

    return dict_raw_data


def extract_data_19_columns(main_table, row_expected_len):
    """Extracts data into a dict from a Worldometer table with 19 columns"""
    main_table_rows = main_table.find_all("tr")
    dict_empty = {"Total_cases": 0, "Total_deaths": 0, "Total_recovered": 0, "Active_cases": 0, "Serious_cases": 0,
                  "Cases_per_1M": 0, "Deaths_per_1M": 0, "Total_Tests": 0, "Tests_per_1M": 0, "Continent": "",
                  "Population": 0}
    dict_raw_data = defaultdict(lambda: dict_empty.copy())

    for i in range(len(main_table_rows)):
        row_data = main_table_rows[i].find_all("td")
        if len(row_data) == row_expected_len:
            country_name = helper_format_country_name(row_data[1].text)
            dict_raw_data[country_name]["Total_cases"] = helper_convert_to_num(row_data[2].text)
            dict_raw_data[country_name]["Total_deaths"] = helper_convert_to_num(row_data[4].text)
            dict_raw_data[country_name]["Total_recovered"] = helper_convert_to_num(row_data[6].text)
            dict_raw_data[country_name]["Active_cases"] = helper_convert_to_num(row_data[8].text)
            dict_raw_data[country_name]["Serious_cases"] = helper_convert_to_num(row_data[9].text)
            dict_raw_data[country_name]["Cases_per_1M"] = helper_convert_to_num(row_data[10].text)
            dict_raw_data[country_name]["Deaths_per_1M"] = helper_convert_to_num(row_data[11].text)
            dict_raw_data[country_name]["Total_Tests"] = helper_convert_to_num(row_data[12].text)
            dict_raw_data[country_name]["Tests_per_1M"] = helper_convert_to_num(row_data[13].text)
            dict_raw_data[country_name]["Population"] = helper_convert_to_num(row_data[14].text)
            dict_raw_data[country_name]["Continent"] = row_data[15].text

    return dict_raw_data


def extract_dict_from_worldometer_html(raw_html_data):
    """Extracts data from the Worldometer/coronavirus html"""
    logger = logging.getLogger("Main")

    # 1. Echarlos al puchero
    soup_data = BeautifulSoup(raw_html_data, 'html.parser')

    # 2. Buscar tipo de tabla y determinar columnas
    # 2.1 Buscar tabla
    main_table = soup_data.find(id="main_table_countries")
    if main_table is None:
        main_table = soup_data.find(id="main_table_countries_today")
    if main_table is None:
        main_table = soup_data.find(id="table3")

    # print(main_table)

    dict_raw_data = None
    if main_table is not None:
        # 2.2 Extraer columnas
        main_table_column_titles = main_table.find_all("th")

        # for key_i in range(len(main_table_column_titles)):
        #     print(main_table_column_titles[key_i].text)

        if len(main_table_column_titles) == 4:
            # First table
            dict_raw_data = extract_data_4_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 5:
            # Include "Change Today" column
            dict_raw_data = extract_data_5_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 6:
            # Include "Change Today" column
            dict_raw_data = extract_data_6_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 8:
            if "Region" in main_table_column_titles[-1].text:
                dict_raw_data = extract_data_8_columns_with_region(main_table, len(main_table_column_titles))
            else:
                # Include "Change Today" column
                dict_raw_data = extract_data_8_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 9:
            # 10 columns includes Cases/1M
            dict_raw_data = extract_data_9_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 10 or len(main_table_column_titles) == 11:
            # 10 columns includes Deaths/1M
            # 11 columns includes Reported 1st case (This row is ignored)
            dict_raw_data = extract_data_10_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 12:
            # 11 and 12 columns includes Total Tests and Tests/1M pop
            # 13 includes continent
            dict_raw_data = extract_data_12_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 13:
            # 13 includes continent
            dict_raw_data = extract_data_13_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 15:
            # 15 includes # and Population
            dict_raw_data = extract_data_15_columns(main_table, len(main_table_column_titles))
        elif len(main_table_column_titles) == 19:
            # 19 includes New Recovered and 1 Case/Death/Test per people
            dict_raw_data = extract_data_19_columns(main_table, len(main_table_column_titles))
        else:
            logger.warning("Unrecognized table. Len: %d", len(main_table_column_titles))
    else:
        logger.warning("Could not find table")

    return dict_raw_data
