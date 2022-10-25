import re
from src.enums.EnumCargo import EnumCargos

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex,email):
        return True
    return False 

def check_cargo(cargo):
    for data in EnumCargos:
        if cargo.upper() == data.value:
            return True
    return False