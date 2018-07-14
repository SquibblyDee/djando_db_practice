from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField("Random String to Fill Preexisting Rows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Ninja(models.Model):
    #Our Many to One link is the line below
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# 1: Create 3 dojos
    # Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")

# 2: Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
    # Dojo.objects.get(id=1).delete()

# 3: Create 3 additional dojos by using Dojo.objects.create
    # Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")

# 4: Create 3 ninjas that belong to the first dojo you created.
    # Ninja.objects.create(first_name="Ted", last_name="Cruz")

# 5: Create 3 more ninjas and have them belong to the second dojo you created.
    # Ninja.objects.create(first_name="Homer", last_name="Simpson", dojo_id=2)

# 6: Create 3 more ninjas and have them belong to the third dojo you created.
    # Ninja.objects.create(first_name="Homer", last_name="Simpson", dojo_id=3)

# 7: Be able to retrieve all ninjas that belong to the first Dojo
    # Ninja.objects.get(dojo_id=1)

# 8: Be able to retrieve all ninjas that belong to the last Dojo
    # Ninja.objects.get(dojo_id=3)

    

