# plus-perth-2019-spikey-forest-dog-api
# Petter <br>
What is it about:
<br>
Petter is all about connecting people who want pets with pets needing a furever home. 
Sometimes it can be too hard to find the one, ergo we created Petter. 
To make sure that adoption stays a joyful journey Petter gives users the option of sharing their success stories with other users.
<br>
# Branches  <br>
When you are working on a feature you need to be working on your own branch - to avoid merge conflict <br>
When you finish working you need to create a pull request from your branch into a master<br>
Pull request needs to be reviewed by a team member<br>
Any code that needs to be changed needs to be fixed <br>
After it's reviewed it needs to be approved <br>
Once it's been approved it needs to be merged into master <br>
# Rules <br>
<li>No one is allowed to push to master</li>
<li>No one should work in master ( because if you work in the master branch our history will be nill</li>
<li>When you are creating a new branch file you will need to be created from master ( we are thinking of implementing the dev branch) </li>
<li>BackEnd and FrontEnd have seperate repos

TO GET STARTED:
CREATE VIRTUAL ENVIRONMENT AND ACTIVATE IT

```bash
petterenv\Scripts\activate
```

INSTALL REQURIEMENTS

```bash
pip install -r requirements.txt
```

MIGRATE DATABASE

```bash
python manage.py makemigrations 
python manage.py migrate
```

CREATE SUPERUSER

```bash
python manage.py createsuperuser
```

LOAD DATA FIXTURES

```bash
python manage.py loaddata pet_mockdata.json
```

RUN THE SERVER

```bash
python manage.py runserver
```

You can then see an example of the API endpoints at: <br>
profiles: "http://localhost:8000/profiles/ <br>
users: "http://localhost:8000/users/ <br>
pets: "http://localhost:8000/pets/
