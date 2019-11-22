from pymysql import connect
import os

connection = connect(
        host = os.getenv('MYSQL_HOST_banking_app'),
        user = os.getenv('MYSQL_USER_banking_app'),
        password = os.getenv('MYSQL_PASSWORD_banking_app'),
        db = os.getenv('MYSQL_DATABASE_banking_app'),
        charset = 'utf8mb4'
        )

insert_nu =  'INSERT INTO user_accounts (user_firstname, user_lastname, user_email, user_password) VALUES ({1}, {2}, {3}, {4})'

select_id = 'SELECT user_id FROM user_accounts WHERE user_email = {}'

show_details = 'SELECT * FROM user_accounts WHERE user_email = {}' 


def newaccount(a, b, c, d):
    try:
        with connection.cursor() as cursor:
            query = insert_nu.format(a, b, c, d)
            cursor.execute(query)
        connection.commit()

        with connection.cursor() as cursor:
            query = select_id.format(c)
            cursor.execute(query)
            result = cursor.fetchone()
            print('This is your ID!: ', result)
    finally:
        connection.close()


def showaccount(a):
    try:
        with connection.cursor() as cursor:
            query = show_details.format(a)
            cursor.execute(query)
            result = cursor.fetchall()
            print('Account details:\n', result)
    finally:
        connection.close()
