from django import forms
from .models import Course, Section, Instructor, Degree, EvaluatorObjective


class QueryCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, label='Course')
    year = forms.ChoiceField(choices=[(year, year) for year in range(2024, 2027)], required=True, label='Year')
    semester = forms.ChoiceField(choices=Section.SEMESTER_CHOICES, required=True, label='Semester')

    def __init__(self, *args, **kwargs):
        super(QueryCourseForm, self).__init__(*args, **kwargs)
        self.fields['course'].label_from_instance = lambda obj: obj.name


class QueryInstructorForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(), required=True, label='Instructor')
    year = forms.ChoiceField(choices=[(year, year) for year in range(2024, 2027)], required=True, label='Year')
    semester = forms.ChoiceField(choices=Section.SEMESTER_CHOICES, required=True, label='Semester')

    def __init__(self, *args, **kwargs):
        super(QueryInstructorForm, self).__init__(*args, **kwargs)
        self.fields['instructor'].label_from_instance = lambda obj: obj.name


class DegreeQueryForm(forms.Form):
    degree = forms.ModelChoiceField(
        queryset=Degree.objects.all().order_by('name', 'level'),
        required=True,
        label='Degree',
    )
    def __init__(self, *args, **kwargs):
        super(DegreeQueryForm, self).__init__(*args, **kwargs)
        self.fields['degree'].label_from_instance = lambda obj: f"{obj.name} ({obj.level})"
