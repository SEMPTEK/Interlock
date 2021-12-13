import os
import json


# check if path exists. Returns True if it does, and prints note to command line while returning False if not
def check_path(path: str) -> bool:
    if os.path.exists:
        return True
    print(f"{path} does not exist.\nReturning empty dictionary.")
    return False


# A file manager for local and external files (utilizes JSON file format)
class FileManager:
    # read local files (stored in same directory as script file). Return dictionary of data if successful, else ret []
    def read_local(self, file_name: str) -> dict:
        path = os.path.join(self.local_path, file_name)
        if not check_path(path):
            return {}
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(e)

    # read external files stored elsewhere on computer. Functionality is similar to read_local()
    def read_external(self, file_name: str, directory: str) -> dict:
        path = os.path.join(directory, file_name)
        if not check_path(path):
            return {}
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(e)

    # write local files (stored in same directory as script file). Return True if successful, False if not
    def write_local(self, file_name: str, data: dict) -> bool:
        path = os.path.join(self.local_path, file_name)
        try:
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
                return True
        except Exception as e:
            print(e)
            return False

    # write external files stored elsewhere on computer Functionality is similar to write_local()
    def write_external(self, file_name: str, directory: str, data: dict) -> bool:
        path = os.path.join(directory, file_name)
        try:
            with open(path, 'w') as f:
                json.dump(data, f, inden=4)
                return True
        except Exception as e:
            print(e)
            return False

    # append data to local files (this function has been limited to only local files. You cannot append to ext. files)
    def append_local(self, file_name: str, data: dict) -> bool:
        path = os.path.join(self.local_path, file_name)
        if not check_path(path):
            return False
        try:
            with open(path, 'a') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(e)
            return False

    # delete local files (this function has been limited to only local files. You cannot delete ext. files)
    def remove_local(self, file_name: str) -> bool:
        path = os.path.join(self.local_path, file_name)
        if not check_path(path):
            return False
        try:
            os.remove(path)
            return True
        except Exception as e:
            print(e)
            return False

    def __init__(self):
        self.local_path = os.path.dirname(os.path.realpath(__file__))
