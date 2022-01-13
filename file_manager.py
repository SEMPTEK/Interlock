import os
import json

local_path = os.path.dirname(os.path.realpath(__file__))


# check if path exists. Returns True if it does, and prints note to command line while returning False if not
def check_path(path: str) -> bool:
    if os.path.exists(path):
        return True
    print(f"{path} does not exist.\nReturning empty dictionary.")
    return False


def check_content(path: str) -> bool:
    with open(path, 'r') as f:
        if f.read() == "":
            return False
        return True


# A file manager for local and external files (utilizes JSON file format)
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


def read_external(file_name: str, directory: str) -> dict:
    path = os.path.join(directory, file_name)
    if not check_path(path):
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(e)


def create_local_dir(dir_name: str, add_path=""):
    path = os.path.join(local_path, add_path, dir_name)
    if check_path(path):
        print(f"{path} already exists")
        return
    try:
        os.makedirs(path)
    except Exception as e:
        print(e)


def remove_local_dir(dir_name: str, path=""):
    path = os.path.join(local_path, path, dir_name)
    if path == local_path:
        print("Cannot delete software home directory")
        return
    try:
        os.remove(path)
    except Exception as e:
        print(e)


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


def write_external(file_name: str, directory: str, data: dict) -> bool:
    path = os.path.join(directory, file_name)
    try:
        with open(path, 'w') as f:
            json.dump(data, f, inden=4)
            return True
    except Exception as e:
        print(e)
        return False


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


def list_external(path: str) -> list:
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return []
    return os.listdir(path)


def list_local(add_path="") -> list:
    path = os.path.join(local_path, add_path)
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return []
    return os.listdir(path)


def make_log(data: dict):
    path = os.path.join(local_path, "logs")
    num_list = os.listdir(path)
    name = str(int(num_list[-1]) + 1)
    write_local(name, data)
