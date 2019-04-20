from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Fungo(models.Model):

    id = models.AutoField(primary_key=True)
    
    specie_genere = models.CharField(max_length=200,default="")
    specie_specie = models.CharField(max_length=200,default="")
    specie_autore = models.CharField(max_length=200,default="")
    specie_var_f = models.CharField(max_length=200,default="")
    specie_autore_var = models.CharField(max_length=200,default="")

    current_name_di_index_fungorum_genere = models.CharField(max_length=200,default="")
    current_name_di_index_fungorum_specie = models.CharField(max_length=200,default="")
    current_name_di_index_fungorum_autore = models.CharField(max_length=200,default="")
    current_name_di_index_fungorum_var_f = models.CharField(max_length=200,default="")
    current_name_di_index_fungorum_autore_var = models.CharField(max_length=200,default="")

    data_verifica = models.CharField(max_length=200,default="")
    comune_provincia = models.CharField(max_length=200,default="")
    localita = models.CharField(max_length=200,default="")
    Altezza_slm = models.CharField(max_length=200,default="")
    data = models.CharField(max_length=200,default="")

    principali_specie_vegetali = models.CharField(max_length=200,default="")
    note = models.CharField(max_length=200,default="")
    tipologia_di_terreno = models.CharField(max_length=200,default="")

    raccolto_da_legit = models.CharField(max_length=200,default="")
    determinato_da_determinavit = models.CharField(max_length=200,default="")
    indicazione_cartografica_igm = models.CharField(max_length=200,default="")



class CsvFile(models.Model):

    id = models.AutoField(primary_key=True)
    csv_file = models.FileField()





