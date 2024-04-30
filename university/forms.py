from django import forms
from .models import Course, Section, Instructor, Degree, Evaluation


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
class EvaluationQueryForm(forms.Form):
    degree = forms.ModelChoiceField(
        queryset=Degree.objects.all().order_by('name', 'level'),
        required=True,
        label='Degree',
    )
    year = forms.ChoiceField(choices=[(year, year) for year in range(2024, 2027)], required=True, label='Year')
    semester = forms.ChoiceField(choices=Section.SEMESTER_CHOICES, required=True, label='Semester')
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(), required=True, label='Instructor')
    def __init__(self, *args, **kwargs):
        super(EvaluationQueryForm, self).__init__(*args, **kwargs)
        self.fields['degree'].label_from_instance = lambda obj: f"{obj.name} ({obj.level})"

class DegreeCopyForm(forms.Form):
    source_degree = forms.ModelChoiceField(
        queryset=Evaluation.objects.all().order_by('degree_name', 'degree_level'),
        required=True,
        label="Select Source Degree",
    )

    target_degrees = forms.ModelMultipleChoiceField(
        queryset=Evaluation.objects.all().order_by('degree_name', 'degree_level'),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label="Select Target Degrees",
    )

    def __init__(self, *args, **kwargs):
        super(DegreeCopyForm, self).__init__(*args, **kwargs)
        self.fields['source_degree'].label_from_instance = lambda obj: f"{obj.degree_name} ({obj.degree_level})"
        self.fields['target_degrees'].label_from_instance = lambda obj: f"{obj.degree_name} ({obj.degree_level})"