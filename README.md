# candidate-testing


## Getting started

```
git clone https://github.com/mirzomumin/candidate-testing.git
```


## Create project environment

```
cd candidate-testing
python -m venv env (Create environment with any title. In my case it is "env")
```

## Install necessary dependencies

```
pip install -r requirements.txt
```

## Create DB

```
python manage.py makemigrations
python manage.py migrate
```


## Run project

```
python manage.py runserver
```