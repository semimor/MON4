from django import forms


class ProductsCreateForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(min_value=1, max_value=5)
    commentable = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'checked': True}),
        required=False)
#
#
class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=2)
#
