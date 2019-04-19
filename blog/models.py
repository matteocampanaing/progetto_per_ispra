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

    genere = models.CharField(max_length=200)
    specie = models.CharField(max_length=200)
    autore = models.CharField(max_length=200)
    var_f = models.CharField(max_length=200)
    autore_var = models.CharField(max_length=200)
    data_verifica = models.CharField(max_length=200)
    comune_provincia = models.CharField(max_length=200)
    localita = models.CharField(max_length=200)
    Altezza_slm = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    principali_specie_vegetali = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    tipologia_di_terreno = models.CharField(max_length=200)
    raccolto_da_legit = models.CharField(max_length=200)
    determinato_da_determinavit = models.CharField(max_length=200)
    indicazione_cartografica_igm = models.CharField(max_length=200)





