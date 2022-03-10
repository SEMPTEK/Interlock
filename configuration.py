"""
This script is meant to be as bare-bones as possible so it does not rely on extensive imports from other modules that
may or may not be missing. This script is meant to be the setup for the software, as well as a recovery script that will
replace missing files/scripts required to operate this program.
"""

import file_manager

data = {
    'config': {
        'background': "white",
    },
    'preferences': {
        'project path': "",
    }
}


# build the config file and insert default settings into it. The config file must exist in order for the software to run
def save():
    file_manager.write_local("config.dat", data)


def load():
    global data
    data = file_manager.read_local("config.dat")


def set_preference(key, value):
    global data
    data[key] = value
