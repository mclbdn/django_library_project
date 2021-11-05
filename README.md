# django_library_project

### <a href="https://mclbdn-library.herokuapp.com">Try running this app here.</a>

Django library app using Django-tables and Semantic UI(+ REST API provided by django_rest_framework)


## Challenges I faced
* I have to say that Django-tables documentation wasn't the most complete piece of documentation, but thanks to a bit of digging on Google and StackOverflow it turned out the way I wanted.
* I don't know if this is unusual(probably not), but I feel that deployment is the most frustrating part of the whole process. Anyway, I made it and deployed this Django app on Heroku and later also set up automatic deploys from the main branch here on GitHub.

## Usage

* First, clone the repo:
```
git clone https://github.com/mclbdn/django_library_project
```
* Then, install python packages from requirements.txt:
```
pip install -r requirements.txt
```
* Set your own environment variables.
* Run `python3 mmanage.py makemigrations`.
* Run `python3 mmanage.py migrate`.
* Run `python3 mmanage.py runserver`.

## Screenshots
<img src="https://raw.githubusercontent.com/mclbdn/django_library_project/main/Screenshot-1.png" width="700" height="600">
<img src="https://raw.githubusercontent.com/mclbdn/django_library_project/main/Screenshot-2.png" width="700" height="600">
<img src="https://raw.githubusercontent.com/mclbdn/django_library_project/main/Screenshot-3.png" width="700" height="600">
