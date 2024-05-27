# Culinary API


## About

The Culinary API is designed to help users share their favorite recipes and explore new ones. This project is implemented using Python Django Rest Framework. This project uses db.sqlite3 as it's database.


## Installation
To get a local copy up and running, follow these steps:

- Clone the repository:
```
git clone https://github.com/onise2001/culinary_api.git
```
- Navigate to project directory:
```
cd culinary_api
```
- Install required modules by running the following command:
```
pip install -r requirements.txt
```

- Run migrations (python3 if on linux):
```
python manage.py migrate
```
- Run server (python3 if on linux):
```
python manage.py runserver
```

## Usage and API endpoints
See swagger documentaion for information about api endpoints.
```
/swagger
```
```
/redoc
```

# OR

## Functionality
- **### List recipes:** By sending a GET request to this api endpoint, ```/recipe/```, you will get an array of all recipes currently in the database.

- **### View recipe:** By sending a GET request to this api endpoint, ```/recipe/{id}```, you will get an instance of the recipe with that id.

- **### Create recipe:** By sending a POST request to this api endpoint, ```/recipe/``` , with correct request body, a new recipe will be created and added to the database if you are authenticated.

- **### Edit recipe:** By sending a PUT request to this api endpoint, ```/recipe/{id}``` , with correct request body, a recipe with that id will be edited with the information you provided in the request body if you have the permission to do so.

- **### Delete recipe:** By sending a DELETE request to this api endpoint, ```/recipe/{id}``` ,  a recipe with that id will be deleted from the database if you have the permission to do so.

- **### Rate recipe:** By sending a PATCH request to this api endpoint, ```/rate/{id}``` , with correct request body, a recipe with that id will get rated by you if you are authenticated.


- **### Recommendations:** By sending a GET request to this api endpoint, ```/rec``` , you will get recommendations about recipes based on recipes you have uploaded if you are authenticated.



## Authentication
This project uses django's built-in Token Authentication for registration and login purposes. Users can register as Chefs or Regular users.
- **Regular Users**
- Username
- Email
- Password

- **Chef**
- Same as regular users plus:
- Background
- Speciality

