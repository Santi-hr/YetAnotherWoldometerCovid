import json

def aux_append_if_key(dict_all_data, dict_input, key_country, key_str):
    """Appends dict_input[key_country][str_key] to list in dict_all_data if the country_key exists"""
    aux_val = 0
    if key_str in dict_input[key_country]:
        aux_val = dict_input[key_country][key_str]
    dict_all_data[key_country][key_str].append(aux_val)


def aux_initialize_list(zeros_len):
    """Initialices the lists for a newly added county by filling previous days with 0s"""
    out_dict = {"Total_cases": [], "Total_deaths": [], "Total_recovered": [], "Active_cases": [],"Serious_cases": [],
                "Cases_per_1M": [], "Deaths_per_1M": [], "Total_Tests": [], "Tests_per_1M": []}

    for i in range(zeros_len-1):
        for key in out_dict:
            out_dict[key].append(0)

    return out_dict


def combine_worldometer_dicts(dict_combined, dict_to_append, dict_datetime):
    """Adds the data from dict_to_append into dict_combined. Dict_datetime is stored as the timestamp"""
    dict_combined["Datetime_str"].append(dict_datetime.strftime("%d/%m/%Y %H:%M:%S"))

    for key_country in dict_to_append:
        if key_country not in dict_combined.keys():
            dict_combined[key_country] = aux_initialize_list(len(dict_combined["Datetime_str"]))

        aux_append_if_key(dict_combined, dict_to_append, key_country, "Total_cases")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Total_deaths")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Total_recovered")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Active_cases")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Serious_cases")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Cases_per_1M")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Deaths_per_1M")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Total_Tests")
        aux_append_if_key(dict_combined, dict_to_append, key_country, "Tests_per_1M")
        if "Continent" in dict_to_append[key_country]:
            dict_combined[key_country]["Continent"] = dict_to_append[key_country]["Continent"]


def append_worldometer_into_output_json(dict_to_append, dict_datetime):
    """Appends data to output json file"""
    # Open json or create it if it does not exist
    try:
        with open("coronavirusData.json", "r", encoding="UTF-8") as fp:
            coronavirus_dict = json.load(fp)
    except IOError:
        # Asume file does not exist and create an empty coronavirus_dict
        coronavirus_dict = dict()
        coronavirus_dict["Datetime_str"] = []

    # Combine data
    combine_worldometer_dicts(coronavirus_dict, dict_to_append, dict_datetime)

    # Store data
    with open('coronavirusData.json', 'w', encoding="UTF-8") as fp:
        json.dump(coronavirus_dict, fp, sort_keys=True, indent=4, ensure_ascii=False)