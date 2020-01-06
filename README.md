# BeaverCoffee

```console
> git clone https://github.com/Hinks/beaver_coffee_manager_app.git
> cd beaver_coffee_manager_app
> docker-compose up
```

**It is required to have two terminal windows open to test out the application. One for the console-app itself and another for 
running needed db-queries that prints out needed id:s and ssn:s.**

Open up a new terminal window and connect to the python-app-container and run the console-app by:
```console
> docker exec -it docker-beaver-app sh
> python src/app.py
```

Open up another terminal window and connect to the mongo-container and run needed db-queries to print out id:s and ssn:s.
```console
> docker exec -it mongo-beaver mongo
> use beaver
> show collections
```


```console
> db.branch_managers.find().pretty()
{...}
> db.sales_managers.find().pretty()
{...}
> db.employees.find().pretty()
{...}
> db.reg_customers.find().pretty()
{...}
```