import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','aklil.settings')

import django
django.setup()

##Fake pop script
from users_app.models import Users
from faker import Faker

fake = Faker()

def populate(N=5):
    for en in range(N):
        #create fake data for entry
        fname = fake.first_name()
        lname = fake.last_name()
        email = fake.email()

        #create record for Users entry
        usrs = Users.objects.get_or_create(first_name=fname, last_name=lname, e_mail=email)

if __name__=="__main__":
    print("Populating data!")
    populate(15)
    print("Populating complete!")
