import requests

print('\nSend POST-Request to given website, with certain parameters')

def create_user():
    print("\n")
    url = str(input('Paste URL: '))
    user_name = str(input('Enter Username: '))
    pwd = str(input('Please enter a password: '))

    package = {"email":user_name, "password":pwd,"role":"admin"}

    x = requests.post(url, data = package)
    print('\n' + x.text + '\n')

create_user()
input('Press anykey to exit')
