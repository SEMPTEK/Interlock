def is_empty(data: str) -> bool:
    for character in data:
        if not character == " ":
            return False
    return True
