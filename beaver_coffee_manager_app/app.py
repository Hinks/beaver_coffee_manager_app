from pymongo import MongoClient
from fsm import run_next
from rules import default_app_data


def main():
    client = MongoClient('mongodb://localhost:27017/beaver')
    db = client.beaver
    print('connected to database')

    run_next(db, default_app_data)

if __name__ == "__main__":
   main()
