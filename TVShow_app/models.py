from django.db import models
from datetime import date, datetime

class ShowManager(models.Manager):
    def createValidate(self, form):
        errors = {}
        if len(form['title']) < 2:
            errors['title'] = "Title of the show must be at lease 2 characters!!"
        titleCheck = self.filter(title=form['title'])
        if titleCheck:
            errors['title'] = 'Show title must be unique.'

        if len(form['network']) < 3:
            errors['network'] = "Network has to be 3 characters!!"

        if form['description'] != '' and len(form['description']) < 10:
            errors['description'] = "Description of the show must be greater than 10 characters!!"

        if form['release_date']:
            date_entered = form['release_date']
            reldate = datetime.strptime(date_entered, "%Y-%m-%d")
            today = datetime.now()
            if reldate >= today:
                errors['release_date'] = "The release date must be in the past."
            
            return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()
