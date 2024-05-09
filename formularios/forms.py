from django import forms

#representar um formulario atraves de uma classe
class formularioCadastro(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()