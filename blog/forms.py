from django import forms

from .models import Post , Comment , Fungo , CsvFile

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
            'specie_genere' ,
            'specie_specie' ,
            'specie_autore' ,
            'specie_var_f' ,
            'specie_autore_var' ,

            'current_name_di_index_fungorum_genere' ,
            'current_name_di_index_fungorum_specie' ,
            'current_name_di_index_fungorum_autore' ,
            'current_name_di_index_fungorum_var_f' ,
            'current_name_di_index_fungorum_autore_var' ,

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


class CsvFileForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ('csv_file',)