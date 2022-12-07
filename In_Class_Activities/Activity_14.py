"""
SQL Injection Example

"""
import DBConnector as DBC

# Connect to DB
my_db = DBC.MyDB()


def CreateTablesAndFillData():
    """
    This creates one table (users) and inserts three rows, each represents a username and a password.
    """
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Data Creation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Creation statement
    my_db.query("CREATE TABLE IF NOT EXISTS CYBR_USERS (USER_NAME VARCHAR, PASS VARCHAR, ADMIN BOOLEAN);", '')

    # Verify Table Was Created by trying to execute a select statement. If the sql statement fails, an exception is
    # "caught". You can also do this using a simple if statement. This is just cooler
    try:
        my_db.query("SELECT 1 FROM CYBR_USERS;", '')
        print("Table was created successfully :)")
    except:
        print("Table was not created successfully :(")

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Adding data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    my_db.query("INSERT INTO CYBR_USERs VALUES(%s,%s,%s);", ('User1', 'Pass1', True))
    my_db.query("INSERT INTO CYBR_USERs VALUES(%s,%s,%s);", ('User2', 'Pass2', False))
    my_db.query("INSERT INTO CYBR_USERs VALUES(%s,%s,%s);", ('User3', 'Pass3', False))

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Verify data was added %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    users_check = my_db.query("SELECT COUNT (*) FROM CYBR_USERS", '')
    if users_check == 0:
        print("Users not added :(")
    else:
        print("Users added :)")


def UserExist_Method1(nameOfUser, passOfUser):
    """
       First style of a method which verifies whether provided user name and password exist in the DB
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    sql_check = "SELECT count(*) FROM CYBR_USERS WHERE (CYBR_USERS.USER_NAME = %s AND CYBR_USERS.PASS = %s);"
    print(sql_check)

    user_found = my_db.query(sql_check, (nameOfUser, passOfUser))[0][0]
    if user_found != 0:
        return True
    return False


def UserExist_Method2(nameOfUser, passOfUser):
    """
       Second style of a method which verifies whether provided user name and password exist in the DB
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    sql_check = "SELECT count(*) FROM CYBR_USERS WHERE (CYBR_USERS.USER_NAME = '" + nameOfUser + "' AND CYBR_USERS.PASS = '" + passOfUser + ")"
    print(sql_check)
    user_found = my_db.query(sql_check, '')[0][0]
    # print(user_found)
    if user_found != 0:
        return True
    return False


def UserExist_Method3(nameOfUser, passOfUser):
    """
       Third style of a method which verifies whether provided user name and password exist in the DB
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    sql_check = "SELECT count(*) FROM CYBR_USERS WHERE (CYBR_USERS.USER_NAME = '" + nameOfUser + "' AND CYBR_USERS.PASS = '" + passOfUser + "');"
    print(sql_check)
    user_found = my_db.query(sql_check, '')[0][0]
    # print(user_found)
    if user_found != 0:
        return True
    return False


def UserExist_Method4(nameOfUser, passOfUser):
    """
       Fourth style of a method which verifies whether provided user name and password exist in the DB
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    sql_check = "SELECT count(*) FROM CYBR_USERS WHERE (CYBR_USERS.USER_NAME = '" + nameOfUser + "' AND CYBR_USERS.PASS = " + passOfUser + ")"
    print(sql_check)
    user_found = my_db.query(sql_check, '')[0][0]
    # print(user_found)
    if user_found != 0:
        return True
    return False


def CheckAdmin1(nameOfUser):
    """
       First style of a method which verifies whether a provided user is an Admin
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    print("Method 1: Check Admin 1")
    sql_check = "SELECT admin FROM CYBR_USERS WHERE (CYBR_USERS.USER_NAME = %s);"
    print(sql_check)

    try:
        bool(my_db.query(sql_check, [nameOfUser])[0][0])
    except:
        return False
    return True
def CheckAdmin2(nameOfUser):
    """
       First style of a method which verifies whether a provided user is an Admin
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    sql_check = "SELECT admin FROM CYBR_USERS WHERE (CYBR_USERS.USER_NAME = '"+nameOfUser+"')"
    print(sql_check)

    try:
        bool(my_db.query(sql_check, [nameOfUser])[0][0])
    except:
        return False
    return True
    # print("=====" ,admin_found)
    # if admin_found:
    #     return True
    # return False


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    # Create the table and add data. Run only once then comment out.

    # CreateTablesAndFillData()
    # user = input("Enter User Name:")
    # password = input("EnterPassword:")

    user = "User1"
    password = "Pass1'"
    # password = "Padss1' or True"
    print('%%%%%%%%%%%%%%%%%%%%%%%%%% Check user and password %%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print("Method 1: User and password exist/ match:\t", UserExist_Method1(user, password))

    print("Method 2: User and password exist/ match:\t", UserExist_Method2(user, password))

    print("Method 3: User and password exist/ match:\t", UserExist_Method2(user, password))

    print("Method 4: User and password exist/ match:\t", UserExist_Method4(user, password))

    print('%%%%%%%%%%%%%%%%%%%%%%%%%% Check whether user is Admin %%%%%%%%%%%%%%%%%%%%%%%%%%%')

    # user = "User3"
    # print("Method 1: User is Admin :\t", CheckAdmin1(user))
    # print("Method 2: User is Admin :\t", CheckAdmin2(user))



if __name__ == "__main__":
    main()
