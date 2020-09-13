import click
import sys
import pyfiglet
from db_operations import *
from validation import *
import call_back_methods


def insertion():
    @click.command()
    @click.option('--name', prompt='Enter Your Name',callback=call_back_methods.name_validation)
    @click.option('--lastname', prompt='Enter Your Lastname', callback=call_back_methods.last_name_validation )
    @click.option('--email', prompt='Enter Your Email', callback=call_back_methods.email_validation)
    @click.option('--age', prompt='Enter Your Age', callback=call_back_methods.age_validation)
    @click.option('--address', prompt='Enter Your Address', callback=call_back_methods.address_validation)
    @click.option('--phone', prompt='Enter Your Phone', callback=call_back_methods.phone_validation)

    def userInput(name, lastname, email, age, address, phone):
        UserOperations.insert(name, lastname, email, age, address, phone)

    userInput()


def show_columns(rows):
    print('')
    print('===================================================================================================')
    print('')
    click.secho('ID      NAME         LASTNAME          EMAIL             AGE     ADDRESS            PHONE', bg='blue', fg='white')
    for row in rows:
        click.secho(
            str(row[0]) + '       ' + str(row[1]) + '          ' + str(row[2]) + '           ' +
            str(row[3]) + '         ' + str(row[4]) + '          ' + str(row[5]) + '         ' + str(row[6])
            , bg='blue', fg='white')
    print('')
    print('===================================================================================================')
    print('')

ascii_banner = pyfiglet.figlet_format("BOOK CONTACT (CLI) PROJECT")
print(ascii_banner)

while True:
    print('Type 0 for list all Contacts')
    print('Type 1 for create contacts')
    print('Type 2 for search Contacts')
    print('Type 3 for Update Contacts')
    print('Type 4 for Delete Contacts')
    print('Type 5 for other actoins...')
    print('Type 6 for Exit.')
    checker = int(input('Enter the number for the Operations: '))



    if checker == 0:
        print('Zero')
        rows = UserOperations.get_info()
        show_columns(rows)
    elif checker == 1:
        insertion()

    elif checker == 2:
        print('You can search by (ID, Name, Email)')
        search_keyword = input('Please Enter the keyword for searching... (ex: 1 , ali or zzz@gmail.com): ')
        rows = UserOperations.search(search_keyword)
        show_columns(rows)

    elif checker == 3:
        print('Whom do you want to update ? search by (ID, Name, Email)')
        search_keyword = input('Please Enter the keyword for searching... (ex: 1 , ali or zzz@gmail.com): ')
        rows = UserOperations.search(search_keyword)
        if rows:
            print('Found Data...')
            show_columns(rows)
            confirmation = click.confirm('Do you want to update?')
            if confirmation:
                name = input('Provide new name: ')
                lastname = input('Provide new lastname :')
                email = input('Provide new Email :')
                age = input('Provider new Age :')
                address = input('Provide new Address :')
                phone = input('Provide new Phone Number :')
                UserOperations.update(name, lastname, email, age, address, phone)
                click.secho('Data updated...', bg='red', fg='white')
            else:
                print('Not updated.')
        else:
            print('Not found')


    elif checker == 4:
        print('Whom do you want to Delete ? search by (ID, Name, Email)')
        search_keyword = input('Please Enter the keyword for searching... (ex: 1 , ali or zzz@gmail.com): ')
        rows = UserOperations.search(search_keyword)
        if rows:
            print('Found Data...')
            show_columns(rows)
            confirmation = click.confirm('Do you want to delete ?')
            if confirmation:
                UserOperations.delete(search_keyword)
                print('Deleted Successfully.')
            else:
                print('Not Deleted.')
        else:
            print('Not found')
    
    elif checker == 5:
        print('Actions such as Backup....')
    
    elif checker == 6:
        sys.exit()
    else:
        click.secho('Invalid Number for the specific Operations.', fg='red')
        sys.exit()

