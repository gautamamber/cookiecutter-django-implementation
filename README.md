# cookiecutter-django-implementation

## Cookiecutter creates projects from project template. [For more](https://cookiecutter.readthedocs.io/en/latest/)


### Create virtualenv

```
virtualenv --python=python3.4 myvenv 
```

### Start virtualenv

```
source myenv/bin/activate
```

### Install cookiecutter

```
pip install cookiecutter
```

### Run

```
cookiecutter https://github.com/gautamamber/cookiecutter-django-implementation.git
```

### It will ask your project name and app name

```
project_name [Hello_world]: ----
app_name [hello_world_app]: ----

cd project_name

```

### Install all the requirements

```
pip install -r requirements.txt
```

### Migrate and Run

```
python manage.py migrate
python manage.py runserver
```






