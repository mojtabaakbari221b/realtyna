python ./manage.py collectstatic --no-input
python ./manage.py migrate
python ./manage.py runserver