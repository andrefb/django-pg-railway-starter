from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        label="Tell us a bit about yourself"
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.bio = self.cleaned_data.get('bio')
        user.save()
        return user
