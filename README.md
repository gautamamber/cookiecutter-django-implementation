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

### Clone the project

```
https://github.com/gautamamber/cookiecutter-django-implementation.git

cd cookcookiecutter-django-implementation
```

### Install all the requirements

```
pip install -r requirements.txt
```

### Come out from directory

```
cd ..
```

### Run cookiecutter

```
cookiecutter cookiecutter-django-implementation
```

### It will ask your project name and app name

```
project_name [Hello_world]: ----
app_name [hello_world_app]: ----
```
### Migrate and Run

```
python manage.py migrate
python manage.py runserver
```




