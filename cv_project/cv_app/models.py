from django.db import models


# Create an Address on DB
class Contact(models.Model):
    first_name = models.CharField('Prenom', max_length=100)
    last_name = models.CharField('Nom', max_length=100)
    phone_number = models.IntegerField('Telephone')
    email = models.EmailField(max_length=50)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_name
