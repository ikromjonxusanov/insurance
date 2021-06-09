from django.forms import *
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext as _

class ContactForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput(), label="")
    phone = CharField(max_length=20, widget=TextInput(), label="")
    description = CharField(max_length=500, widget=Textarea(), label="")

    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class PostForm(ModelForm):
    title = CharField(max_length=255, widget=TextInput(attrs={'placeholder':"title"}))
    description = CharField(max_length=5000, widget=Textarea(attrs={'placeholder':"Message..."})) 
    class Meta:
        model = Post
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].label = ''
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        self.fields['postImage'].label = ''
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class ServiceClassForm(ModelForm):
    title = CharField(max_length=255, widget=TextInput(attrs={'placeholder':"Post title", 'class':"post-title"}))
    description = CharField(max_length=5000, widget=Textarea(attrs={'placeholder':"Post message", 'class':"post-message"})) 
    class Meta:
        model = ServiceClass
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        self.fields['image'].label = ''

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

regions = (
        (1, _("Toshkent shahri")),
        (2, _("Toshkent viloyati")),
        (3, _("Sirdaryo viloyati")),
        (4, _("Jizzax viloyati")),
        (5, _("Samarqand viloyati")),
        (6, _("Qashqadaryo viloyati")),
        (7, _("Surxondaryo viloyati")),
        (8, _("Buhoro viloyati")),
        (9, _("Navoiy viloyati")),
        (10, _("Xorazm viloyati")),
        (11, _("Andijon viloyati")),
        (12, _("Farg'ona viloyati")),
        (13, _("Namangan viloyati")),
        (14, _("Qoraqalpog'iston Respublikasi")),
    )
class LocationForm(ModelForm):

    name = CharField(max_length=255, widget=TextInput(), label="Filial name")
    address = CharField(max_length=255, widget=TextInput(), label="Filial address")
    workDate = CharField(max_length=500, widget=TextInput(), label="Filial Working days")
    workClock = CharField(max_length=255, widget=TextInput(), label="Filial Working hours")
    mapLocation = CharField(max_length=5000, widget=Textarea(), label="Filial address embed code")
    class Meta:
        model = Location
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))