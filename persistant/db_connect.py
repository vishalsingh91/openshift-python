from pymongo import MongoClient
import pprint


# Creating instance of mongoclient

def connect():
    client = MongoClient()
    db = client.python_test_db
    employee = create_data()
    # Creating document
    employees = db.employees
    # Inserting data
    employees.insert_one(employee)
    # Fetching data
    pprint.pprint(employees.find_one())


def create_data():
    employee = {"id": "107",
                "name": "Martin",
                "profession": "Manager",
                "Address": "Sweden"
                }
    return employee
