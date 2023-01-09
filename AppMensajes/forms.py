from django import forms

class FormMensajes(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea(attrs = {
            
            "class": "formulario_ms", 
            "placeholder": "Escribe tu mensaje",
            "cols" : "50",
            "rows": "4",

        }))
