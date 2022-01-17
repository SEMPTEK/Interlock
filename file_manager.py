import os
import json

local_path = os.path.dirname(os.path.realpath(__file__))


# check if path exists. Returns True if it does, and prints note to command line while returning False if not
def check_path(path: str, build_on_fail=False) -> bool:
    if os.path.exists(path):
        return True
    if build_on_fail:
        create_local_dir(path)
        print(f"{path} does not exist. build_on_fail=True. Building directory")
        return True
    print(f"{path} does not exist")
    return False


def check_content(path: str) -> bool:
    with open(path, 'r') as f:
        if f.read() == "":
            print(f"File {path} is empty. Please verify this is not an error")
            return False
        return True


# read local files (JSON Format)
def read_local(file_name: str) -> dict:
    global local_path
    path = os.path.join(local_path, file_name)
    if not check_path(path):
        return {}
    if not check_content(path):
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(e)


# read files outside of local directory (JSON Format)
def read_external(file_name: str, directory: str) -> dict:
    path = os.path.join(directory, file_name)
    if not check_path(path):
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(e)


# create folder in local directory (can be several folders deep)
def create_local_dir(dir_name: str, add_path=""):
    path = os.path.join(local_path, add_path, dir_name)
    if check_path(path):
        print(f"{path} already exists")
        return
    try:
        os.makedirs(path)
    except Exception as e:
        print(e)


# remove folder from local directory
def remove_local_dir(dir_name: str, path=""):
    path = os.path.join(local_path, path, dir_name)
    if path == local_path:
        print("Cannot delete software home directory")
        return
    try:
        os.remove(path)
    except Exception as e:
        print(e)


# create local json file with .dat extension. Write data to folder. If successful, return True, else False
def write_local(file_name: str, data: dict) -> bool:
    global local_path
    path = os.path.join(local_path, file_name)
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            return True
    except Exception as e:
        print(e)
        return False


# create external json file with .dat extension. Write data to folder. If successful, return True, else False.
def write_external(file_name: str, directory: str, data: dict) -> bool:
    path = os.path.join(directory, file_name)
    try:
        with open(path, 'w') as f:
            json.dump(data, f, inden=4)
            return True
    except Exception as e:
        print(e)
        return False


# append json data to local file with .dat extension. If successful, return True, else False.
def append_local(file_name: str, new_data: dict) -> bool:
    global local_path
    path = os.path.join(local_path, file_name)
    if not check_path(path):
        return False
    if not check_content(path):
        return False
    try:
        file_data = {}
        with open(path, 'r') as f:
            file_data = json.load(f)
            file_data.update(new_data)
        with open(path, 'w') as f:
            json.dump(file_data, f, indent=4)
    except Exception as e:
        print(e)
        return False


# remove local file. If successful, return True, else False.
def remove_local(file_name: str) -> bool:
    global local_path
    path = os.path.join(local_path, file_name)
    if not check_path(path):
        return False
    try:
        os.remove(path)
        return True
    except Exception as e:
        print(e)
        return False


# list all items in external directory. Return list object.
def list_external(path: str) -> list:
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return []
    return os.listdir(path)


# list all items in local directory. Return list object.
def list_local(add_path="") -> list:
    path = os.path.join(local_path, add_path)
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return []
    return os.listdir(path)
