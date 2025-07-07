from time import sleep

AGENDA = {}

def show_contacts():
    if AGENDA:      # se a agenda existir (não estiver vazia)
        for contact in AGENDA:
            search_contact(contact)
    else:
        print('>>>> Empty agenda')
        sleep(1)

def search_contact(contact):
    try:
        print('-' * 20)
        print('Name: ', contact)
        print('Phone: ', AGENDA[contact]['phone'])
        print('Email: ', AGENDA[contact]['email'])
        print('Address: ', AGENDA[contact]['address'])
        print('-' * 20)
    except KeyError:
        print(f'The contact "{contact}" does not exist')
    except Exception as error:
        print('An unexpected error occurred')

sleep(1)

def read_contact_details():
    phone = input('Enter the contact phone: ')
    email = input('Enter the contact email: ')
    address = input('Enter the contact address: ')
    return phone, email, address

def include_edit_contact(contact, phone, email, address):
    AGENDA[contact] = {
        'phone': phone,
        'email': email,
        'address': address,
    }


def delete_contact():
    question = str(input('Enter the name of the contact to be deleted: '))
    try:
        AGENDA.pop(question)
        save()
        print()
        print(f'>>>>> Contact {question} deleted successfully!')
        print('Updating the agenda...')
        sleep(2)
        print()
        show_contacts()
        sleep(2)
    except KeyError:
        print('Contact not found')
        sleep(2)
    except Exception as error:
        print('An unexpected error occurred')

def export_contacts(file_name):
    try:
        with open(file_name, 'w') as file:
            print_executed = False
            for contact in AGENDA:
                phone = AGENDA[contact]['phone']
                email = AGENDA[contact]['email']
                address = AGENDA[contact]['address']
                file.write(f'{contact}, {phone}, {email}, {address}\n')
            print('>>>> Agenda exported successfully')
    except Exception as error:
<<<<<<< HEAD
        print('Algum erro ocorreu')
=======
        print('An error occurred')
>>>>>>> e8fa062 (Updated)

def import_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(',')
                name = details[0]
                phone = details[1]
                email = details[2]
                address = details[3]
                include_edit_contact(name, phone, email, address)
                save()
    except FileNotFoundError:
        print('>>>>> File not found')
    except Exception as error:
        print('>>>>> An unexpected error occurred')

def save():
    export_contacts('database.csv')

def load():
    try:
        with open('database.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(',')
                name = details[0]
                phone = details[1]
                email = details[2]
                address = details[3]

                AGENDA[name] = {
                    'phone': phone,
                    'email': email,
                    'address': address,
                }


        print('>>>>> Database loaded successfully')
        print(f'>>>>> {len(AGENDA)} contacts loaded')
    except FileNotFoundError:
        print('>>>>> File not found')
    except Exception as error:
<<<<<<< HEAD
        print('>>>>> Algum erro inesperado ocorreu')
=======
        print('>>>>> An unexpected error occurred')
>>>>>>> e8fa062 (Updated)

def print_menu():
    print(' 1 -> Show all contacts\n',
          '2 -> Search contact\n',
          '3 -> Add contact\n',
          '4 -> Edit contact\n',
          '5 -> Delete contact\n',
          '6 -> Export contacts to CSV\n',
          '7 -> Import contacts\n',
          '0 -> Close agenda')

load()
while True:
    print_menu()
    print()
    option = input('Choose an option: ')
    if option == '1':
        show_contacts()

    elif option == '2':
        contact = str(input('Enter the name of the contact: '))
        search_contact(contact)

    elif option == '3':
        contact = input('Enter the name of the contact: ')

        try:
            AGENDA[contact]     # se o contato existir na agenda, edite
            print(f'>>>> Editing contact {contact}')
            include_edit_contact(contact, phone, email, address)
            print()
            print('>>>> Contact edited successfully!')
            sleep(1)
        except KeyError:
            phone, email, address = read_contact_details()
            include_edit_contact(contact, phone, email, address)
            print()
            print('>>>> Contact added successfully!')
            save()
            sleep(1)

    elif option == '4':
        contact = input('Enter the name of the contact: ')

        try:
            AGENDA[contact]
            print(f'>>>> Editing contact {contact}')
            phone, email, address = read_contact_details()
            include_edit_contact(contact, phone, email, address)
            save()
        except KeyError:
            print('>>>> Contact does not exist')
            sleep(1)

    elif option == '5':
        delete_contact()

    elif option == '6':
        file_name = input('Enter the name of the file to export: ')
        export_contacts(file_name)

    elif option == '7':
        file_name = input('Enter the name of the file to import: ')
        import_contacts(file_name)
        print()
        print('>>>> Contact added/edited successfully!')
        sleep(1)
        print('Updating agenda...')
        sleep(2)
        print()
        show_contacts()
        print()
        sleep(1)

    elif option == '0':
        print('Exiting...')
        sleep(1)
        break
    else:
        print('Invalid option.')
