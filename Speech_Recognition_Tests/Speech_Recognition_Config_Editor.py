import configparser
import os

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, "Speech_Recognition_Config.ini")
config = configparser.ConfigParser()
config.read(path_config_file)

print("Sections : ", config.sections())

count_sections = 0

sections_file = config.sections()

print(len(sections_file))

print("Sections: ")

while count_sections < len(sections_file):
    print(str(count_sections) + " - " + sections_file[count_sections])
    count_sections = count_sections + 1

option_section = input("Please select which section you want to change: ")

print("You selected: " + sections_file[int(option_section)])

count_var = 0

var_sections = config.items(sections_file[int(option_section)])

while count_var < len(var_sections):
    print(str(count_var) + " - " + var_sections[count_var][1])
    count_var = count_var + 1

option_var = input("Please select which variable you want to change: ")

change = input("Please enter what you want to change the variable to: ")

config[sections_file[int(option_section)]][var_sections[count_var - 1][0]] = change

with open(path_config_file, 'w') as configfile:
    config.write(configfile)