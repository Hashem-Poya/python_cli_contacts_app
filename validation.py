import re

class Validation:
    @staticmethod
    def validate_name(name):
        pattern = '[a-z]{3,20}'
        result = re.match(pattern, name)
        if result:
            return True
        else:
            return False


    @staticmethod
    def validate_lastname(lastname):
        pattern = '[a-z]{3,20}'
        result = re.match(pattern, lastname)
        if result:
            return True
        else:
            return False


    @staticmethod
    def validate_age(age):
        if int(age) <= 120 and int(age) >= 1:
            return True
        else:
            return False


    @staticmethod
    def validate_address(address):
        pattern = '[a-z0-9]{5,50}'
        result = re.match(pattern, address)
        if result:
            return True
        else:
            return False


    @staticmethod
    def validate_email(email):
        if(re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)):  
            return True
        else:  
            return False

    @staticmethod
    def validate_phone(phone):
        pattern = '^(0|\+93)(7){1,1}(7|8|9){1,1}[0-9]{7}$'
        result = re.match(pattern, phone)
        if result:
            return True
        else:
            False
