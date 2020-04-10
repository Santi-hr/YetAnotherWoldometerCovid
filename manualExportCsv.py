import json

with open("coronavirusData.json", "r", encoding="UTF-8") as fp:
    coronavirus_dict = json.load(fp)

# Prints all country names
for country in coronavirus_dict:
    print(country)

selected_country = "Spain"

data_len = len(coronavirus_dict[selected_country]["Total_cases"])

with open("coronavirus_"+selected_country+"_outputCsv.csv", "w", encoding="UTF-8") as fout:
    top_line = "Date;Total_cases;Total_deaths;Total_recovered;Active_cases;Serious_cases;Cases_per_1M;Deaths_per_1M;Total_Tests;Tests_per_1M\n"
    fout.write(top_line)

    for i in range(data_len):
        new_line = coronavirus_dict["Datetime_str"][i]
        new_line += ';' + str(coronavirus_dict[selected_country]["Total_cases"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Total_deaths"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Total_recovered"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Active_cases"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Serious_cases"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Cases_per_1M"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Deaths_per_1M"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Total_Tests"][i])
        new_line += ';' + str(coronavirus_dict[selected_country]["Tests_per_1M"][i])
        new_line += '\n'
        fout.write(new_line)
        print(new_line)