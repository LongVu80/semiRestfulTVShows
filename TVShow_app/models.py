from django.db import models

class ShowManager(models.Manager):
    def createValidate(self, form):
        errors = {}
        if len(form['title']) < 2:
            errors['title'] = "Title of the show must be at lease 2 characters!!"
        titleCheck = self.filter(title=form['title'])
        if titleCheck:
            errors['title'] = 'That Show title is already in the system, please choose a new title.'

        if len(form['network']) < 3:
            errors['network'] = "Network has to be 3 characters!!"

        if len(form['description']) < 10:
            errors['description'] = "Description of the show must be greater than 10 characters!!"

        if len(form['release_date']) < 7:
            errors['release_date'] = "Enter the correct Released Date of the show!!"

            return errors

    def editValidate(self, form):
        errors = {}
        if len(form['title']) < 2:
            errors['title'] = "Title of the show must be at lease 2 characters!!"

        if len(form['network']) < 3:
            errors['network'] = "Network has to be 3 characters!!"

        if len(form['description']) < 10:
            errors['description'] = "Description of the show must be greater than 10 characters!!"

        if len(form['release_date']) < 7:
            errors['release_date'] = "Enter the correct Released Date of the show!!"

            return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()
