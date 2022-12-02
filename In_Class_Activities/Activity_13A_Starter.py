"""
SQL Injection Example

"""
from In_Class_Activities import DBConnector as DBC

# Connect to DB
my_db = DBC.MyDB()


def CreateTablesAndFillData():
    """
    This creates one table (users) and inserts three rows, each represents a username and a password.
    """

    # Your code goes here.


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    # Create the table and add data
    CreateTablesAndFillData()


if __name__ == "__main__":
    main()
