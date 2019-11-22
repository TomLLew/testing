from pymysql import connect
import os
from methods import newaccount 



connection = connect(
        host = os.getenv('MYSQL_HOST_banking_app'),
        user = os.getenv('MYSQL_USER_banking_app'),
        password = os.getenv('MYSQL_PASSWORD_banking_app'),
        db = os.getenv('MYSQL_DATABASE_banking_app'),
        charset = 'utf8mb4'
        )


 




print('Welcome!')
print('---------------------------------')
print('')
current_account = input('Do you currently have an account with us?   y/n     ')
ca = current_account.lower()
print('')
print('---------------------------------')

if ca == 'y':
    print('Welcome back!\n')
    ca_options = int(input('What can we do for you?\n 1.View current account details?\n 2.Make a withdrawal?\n 3.Make a deposit?\n 4.Quit\n Choice?:  '))

elif ca == 'n':
    choice = str(input('Create account y/n?   '))
    if choice == 'y':
        fn = str(input('Enter first name:  '))   
        ln = str(input('Enter last name:  '))
        n_email = str(input('Enter your email:  '))
        pas = str(input('Enter password:  ')) 
        newaccount(fn, ln, n_email, pas)

else:
    print('failure')


    






