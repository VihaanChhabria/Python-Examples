import configparser
import os
import time

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
try:
    path_config_file = os.path.join(os.environ['WINDIR'], "Print_EXE_Config.ini")

    config = configparser.ConfigParser()
    config.read(path_config_file)

    print_str = ConfigSectionMap("Print_String_Head")['test']

    print(print_str)
except:
    
    print("bad")

time.sleep(10)