users = {
    'john': {
        'password': '12345'
    },

    'marrie': {
        'password': '123'
    }
}

def Login(user,password):
    if(user in users):
        if(password == users[user]['password']):
            print('Login successful!')
        else:
            print('Incorrect Password!')
    else:
        print('User not Exists')

def register(username, password):
    if(username in users):
        print('Username in use!')
    else:
        users[username] = {
            'password': password
        }

        print('Register Successful')

def show_users():
    for user in users:
        print(user)


def options():
    print('*'*20)
    print('(1) - Login')
    print('(2) - Register')
    print('(3) - Show Users')
    print('(4) - Exit')
    print('*'*20)

while True:
    options()

    opt = input('R: ')

    if (opt == '1'):

        print('Login')
        username = input('Username: ')
        password = input('Password: ')
        Login(username, password)

    elif (opt == '2'):

        new_username = input('New Username: ')
        new_password = input('New Password: ')
        register(new_username, new_password)

    elif (opt == '3'):
        show_users()
    elif (opt == '4'):
        print('Exiting...')
        break
    else:
        print('Invalid Option')