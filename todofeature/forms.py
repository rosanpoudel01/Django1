from django import forms
from todofeature.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = ("image",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["name"].widget.attrs["class"] = "form-control"   this is used to customize single field
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.isdigit():
            raise forms.ValidationError("Name cannot be a number")
        return name
