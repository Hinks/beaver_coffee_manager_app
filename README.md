# beaver_coffee_manager_app
1. Before you can run this application,
you have to meet the requirements in requirements.txt

1. start a local mongodb-server.
2. run the init-script in the shell by typing: mongo localhost:27017/beaver db_init_script.js
3. run the python app by typing the following in the shell inside the top directory: python3.6 beaver_coffee_manager_app/app.py

Some of the queries require knowledge of id:s and ssn:s.
For example have a mongo shell open alongside the app and find the right id:s and ssn:s
by queries like:
db.branch_managers.find().pretty()
db.sales_managers.find().pretty()
db.employees.find().pretty()
db.reg_customers.find().pretty()
