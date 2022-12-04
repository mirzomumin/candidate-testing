# candidate-testing


## Getting started

```
git clone https://github.com/mirzomumin/candidate-testing.git
```


## Create project environment and activate it

```
cd candidate-testing

(Create environment with any title. In my case it is "env")

python -m venv env (for Windows)
env\Scripts\activate (for Windows)

virtualenv env (for Linux)
source env/bin/activate (for Linux)
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