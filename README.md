# AskApp

Django demo application: question answer forum.  
Dependencies are:

- Python *(>=3)*
- Django *(>=1.8)*

## Configure

    git clone https://github.com/simonsystem/askapp.git
    cd askapp
    ./manage.py migrate
    ./manage.py loaddata questions/fixtures/initial_data.json
    ./manage.py createsuperuser  # Remember your username and password
    ./manage.py runserver

## Use

- Navigate to <http://localhost:8000/admin/questions/> and log in.
- Create questions and answers.
- View an answer on <http://localhost:8000/frage/1/> or similar.