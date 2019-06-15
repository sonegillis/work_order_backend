# Work Order API
An API that can be could be used to do the following
- Create a worker
- Delete a worker
- Create a work order
- Assigning a worker to an order
- Fetch all work orders
    * For a specific worker
    * Order by deadline
  
## Preliquisites
- Django
- Django Rest Framework
- PostgreSQL
- Git
- virtualevn

## Getting Started
1. Clone this repository
```bash 
    $ git clone https://github.com/sonegillis/work_order_backend.git
```
2. Create a virtual environment in any directory of your choice and activate it
```bash
    $ virtualenv -p python3 yourvirtualenvironment
    $ source yourvirtualenvironment/bin/activate
```
3. Navigate to the project directory and install the requirements in the virtual environment
```bash
    $ pip install -r requirements.txt
```
4. Create a file and name it **.env** while contain configurations for the application\
   Paste the following content in the file
   
      SECRET_KEY=YOUR_SECRET_KEY\
      DEBUG=False\
      DB_NAME=YOUR_DB_NAME\
      DB_USER=YOUR_DB_USER\
      DB_PASSWORD=YOUR_DB_PASSWORD\
      DB_HOST=YOUR_DB_HOST\
      DB_PORT=YOUR_DB_PORT
     
   You can generate a secret key [here](https://www.miniwebtool.com/django-secret-key-generator/)
   
5. Run the django migration commands
```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
```
6. Create a superuser and run the server on your preferred port
 ```bash
    $ python manage.py createsuperuser
    $ python manage.py runserver 0.0.0.0:your-port
 ```
 
7. Open your browser and enter the url (localhost:your-port/admin) to login and confirm everything is properly set up

## Testing
This api can be tested in two ways
1. Using the mozilla [rest client extension](https://addons.mozilla.org/en-US/firefox/addon/restclient/) if you have a mozilla        browser.
2. Using a test script which I developed to test from the command line
  - Navigate to api folder in the project and run the script from the command line
  ```bash
      $ cd api
      $ python3 test-api.py
   ```
   
 ## Contributors
 1. [Mekolle Sone Gillis](https://www.githubb.com/sonegillis)
   
   
  
