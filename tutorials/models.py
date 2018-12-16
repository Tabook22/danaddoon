from django.db import models
from datetime import datetime

## the way we create a model is with a class

class Tutorial (models.Model):
    cat_choices=(
        ('Programming','Programming'),
        ('Graphic Design','Graphic Design'),
        ('Networking','Networking'),
        ('Database','Database'),
        ('Web Design','Web Design'),
        ('REST API','REST API'),
        ('Linux','Linux'),
        ('Photography','Photography'),
        ('Geranal', 'General')
    )
    #getting auto increment filed, by taking the last value and add one to it
    title=models.CharField(max_length=300)
    cat=models.CharField(max_length=60, choices=cat_choices)
    date_published=models.DateTimeField(default=datetime.now)
    s_desc=models.TextField(blank=True)
    l_desc=models.TextField(blank=True)
    is_published=models.BooleanField(default=True)
    photo_main=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_1=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title
    

