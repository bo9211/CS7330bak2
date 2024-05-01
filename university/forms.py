from django import forms
from .models import Course, Section, Instructor, Degree, Evaluation, DegreeCourse


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
        queryset=Degree.objects.all(),
        label="Source Degree",
        # Customize the display of each degree instance in the dropdown
        to_field_name="id",  # Assuming 'id' is what you want to use to identify each instance
    )
    target_degrees = forms.ModelMultipleChoiceField(
        queryset=Degree.objects.all(),
        label="Target Degrees",
        # Customize the display for multiple select
        to_field_name="id",  # Assuming 'id' is what you want to use to identify each instance
    )

    def __init__(self, *args, **kwargs):
        super(DegreeCopyForm, self).__init__(*args, **kwargs)
        self.fields['source_degree'].label_from_instance = self._format_label
        self.fields['target_degrees'].label_from_instance = self._format_label

    def _format_label(self, obj):
        # Custom format for displaying the degree in the form field
        return f"{obj.name} - {obj.level}"


