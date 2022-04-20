from django import forms


class EmpresaFormulario(forms.Form):

    #Especificar los campos
    nombre_empresa = forms.CharField()


class AreaFormulario(forms.Form):   
    nombre_area= forms.CharField(max_length=30)
    cantidad_empleados= forms.IntegerField()

class TrabajadorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)