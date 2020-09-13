import re
import click
import sys
import validation


def name_validation(ctx, param, value):
    if validation.Validation.validate_name(value):
        return value
    else:
        for l in range(1, 4):
            userInput = input('Enter a Valid name: ')
            if validation.Validation.validate_name(userInput):
                return userInput
                break
        sys.exit()    
                
        
def last_name_validation(ctx, param, value):
    if validation.Validation.validate_lastname(value):
        return value
    else:
        for l in range(1, 4):
            userInput = input('Enter a Valid Lastname: ')
            if validation.Validation.validate_lastname(userInput):
                return userInput
                break
        sys.exit()    


def age_validation(ctx, param, value):
    if validation.Validation.validate_age(value):
        return value
    else:
        for l in range(1, 4):
            userInput = input('Enter a Valid Age: ')
            if validation.Validation.validate_age(userInput):
                return userInput
                break
        sys.exit()    
                     
def email_validation(ctx, param, value):
    if validation.Validation.validate_email(value):
        return value
    else:
        for l in range(1, 4):
            userInput = input('Enter a Valid Email Address: ')
            if validation.Validation.validate_email(userInput):
                return userInput
                break
        sys.exit()    


def address_validation(ctx, param, value):
    if validation.Validation.validate_address(value):
        return value
    else:
        for l in range(1, 4):
            userInput = input('Enter a Valid Address: ')
            if validation.Validation.validate_address(userInput):
                return userInput
                break
        sys.exit()    

def phone_validation(ctx, param, value):
    if validation.Validation.validate_phone(value):
        return value
    else:
        for l in range(1, 4):
            userInput = input('Enter a Valid Phone Number: ')
            if validation.Validation.validate_phone(userInput):
                return userInput
                break
        sys.exit()    

