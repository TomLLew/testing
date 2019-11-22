    



from pymysql import connect
import os


connection = connect(
        host = os.getenv('MYSQL_HOST_banking_app'),
        user = os.getenv('MYSQL_USER_banking_app'),
        password = os.getenv('MYSQL_PASSWORD_banking_app'),
        db = os.getenv('MYSQL_DATABASE_banking_app'),
        charset = 'utf8mb4'
        )
# INSERT into the database:
try: 
   #with connection.cursor() as cursor:
     #   query = 'INSERT INTO user_accounts (user_firstname, user_lastname, user_email) VALUES ("jim", "Llewelyn", "jim.jim@hmail.com");'
       # cursor.execute(query)
    #connection.commit()

# SELEFT * FROM the database:

    with connection.cursor() as cursor:
        query = 'SELECT * FROM user_accounts'
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()

#______________________________________
