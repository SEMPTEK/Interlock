import os
import json

local_path = os.path.dirname(os.path.realpath(__file__))


# check if path exists. Returns True if it does, and prints note to command line while returning False if not
def check_path(path: str) -> bool:
    if os.path.exists:
        return True
    print(f"{path} does not exist.\nReturning empty dictionary.")
    return False


# A file manager for local and external files (utilizes JSON file format)
def read_local(file_name: str) -> dict:
    global local_path
    path = os.path.join(local_path, file_name)
    if not check_path(path):
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


# TODO: finish create & delete local directory functions
def create_local_dir(dirname: str, path=""):
    pass

def remove_local_dir(dirname: str, path=""):
    pass


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


def append_local(file_name: str, data: dict) -> bool:
    global local_path
    path = os.path.join(local_path, file_name)
    if not check_path(path):
        return False
    try:
        with open(path, 'a') as f:
            json.dump(data, f, indent=4)
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
    if not os.listdir(path):
        print(f"{path} does not exist")
        return []
    return os.listdir(path)


def list_local() -> list:
    return os.listdir(local_path)
