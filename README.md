# REALTYNA

## About The Project

We would like to send you our Python and Django tech challenge. You will have one week to prepare it and send the results to us. Please consider you should not work more than 8 hours on this technical 
challenge.

Description:
As a listing owner, I want a system for making and tracking reservations that can be handled by third-party services.

* The system can be used by multiple listings.
* The system provides REST API endpoints:
-> To make reservations
-> To check if a number of rooms are available at a certain time
* A reservation is for a name (any string) and for a certain amount of time
* The listing owner can get an overview over the booked rooms as an HTML or TEXT report


Limitations:

* Authentication / Authorization is not in the scope of this task
* No localization needed

Hints:
* Use third-party packages where applicable!


## Installation

### Prerequisites

create your env file and put your desired values instead of default:

```cp .envs/.env.sample .envs/.env```

After creating the virtual environment, install the requirements :

‍‍‍‍```pip install -r requirements/development.txt   # for development```

```pip install -r requirements/production.txt   # for production```

### Pre-Run

run migration :

```./manage.py migrate```


### Run Project

#### run in development with manage command

```./manage.py runserver --settings configs.django.development```


#### run in production with manage command

```./manage.py runserver --settings configs.django.production```


#### run with gunicorn in production
```DJANGO_SETTINGS_MODULE=configs.django.production gunicorn configs.wsgi:application --bind 0.0.0.0:8000 --workers 3```

#### run with docker

```docker-compose -p local -f compose/local.yml up --build -d```

