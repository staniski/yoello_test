## How to Run 
In the top-level directory 

```
$ docker-compose build 
$ docker-compose up -d
$ docker-compose exec web python manage.py create_db
```
Go to http://localhost:5000 to view the server

## How to view database

Make sure docker containers are running and user table is created 

Then, use
```
$ docker-compose exec db psql --username=flask -dbname=flask_dev
$ \l
$ \c flask_dev
$ \dt
$ select * from users;
```
This will show all users currently in the table

## Api Docs 
To test the CRUD apis it is better to use a tool like Postman

To get all users do a GET Request to http://localhost:5000/users

To get a user by id, do a GET Request to http://localhost:5000/users/ID

To create a user, do a POST request to http://localhost:5000/users/add with a requst body as a form with values:
{first_name:"YOUR_VALUE",last_name:"YOUR_VALUE",email:"YOUR_VALUE",phone_number:"YOUR_VALUE"}

To update a user, do a PUT request to http://localhost:5000/users/update with a requst body as a form with values:
{first_name:"YOUR_VALUE",last_name:"YOUR_VALUE",email:"YOUR_VALUE",phone_number:"YOUR_VALUE"}

To delete a user, do a DELETE request to http://localhost:5000/users/delete/ID. No arguments required.




