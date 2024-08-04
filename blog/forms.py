from django import forms


class InputForm(forms.Form):
    
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_numbers = forms.IntegerField(
        help_text="enter 6 digit roll numbers "
    )
    password = forms.CharField(widget=forms.PasswordInput())

    email = forms.EmailField(max_length=20,
     help_text="ex: freddydjouaka@gmail.com")
    date = forms.DateField( help_text= "jj/mm/aa"
        
    )
    time = forms.TimeField()
