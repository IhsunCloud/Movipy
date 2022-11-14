from django import forms


class AddMovieForm(forms.Form):
    title = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    trailer = forms.FileField(widget=forms.FileField)
    thumbnail = forms.ImageField(widget=forms.ImageField)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass