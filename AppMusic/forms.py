from django import forms

class Formulario(forms.Form):
    correo= forms.CharField(max_length=25, required=True)
    contraseña = forms.CharField(max_length=8, required=True)

    def clean_field(self):
        correo = self.cleaned_data.get["correo"]
        if correo != "pipedj12@hotmail.es":
            raise forms.ValidationError("correo incorrecto")
        else:
            return correo
    
