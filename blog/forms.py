from django import forms

from .models import Post , Comment , Fungo

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

    
class FungoForm(forms.ModelForm):

    class Meta:
        model = Fungo
        fields = (
            'genere' ,
            'specie' ,
            'autore' ,
            'var_f' ,
            'autore_var' ,
            'data_verifica',
            'comune_provincia', 
            'localita' ,
            'Altezza_slm' ,
            'data' ,
            'principali_specie_vegetali' , 
            'note' ,
            'tipologia_di_terreno' , 
            'raccolto_da_legit' , 
            'determinato_da_determinavit' ,
            'indicazione_cartografica_igm' ,)