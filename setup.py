"""
This script is meant to be as bare-bones as possible so it does not rely on extensive imports from other modules that may
or may not be missing. This script is meant to be the setup for the software, as well as a recovery script that will
replace missing files/scripts required to operate this program.
"""

import os
import json


# build the config file and insert default settings into it. The config file must exist in order for the software to run
def build_config():
    data = {
        'config': {
            'background': "white",
        },
    }

    path = os.path.dirname(os.path.realpath(__file__))
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
