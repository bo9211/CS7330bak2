from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Degree(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)

    class Meta:
        unique_together = ('name', 'level')


class Course(models.Model):
    course_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=255, unique=True)


class DegreeCourse(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_core = models.BooleanField(default=False)
    degree_name = models.CharField(max_length=255, default='Default Name')
    degree_level = models.CharField(max_length=50, default='Default Level')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.degree_name = self.degree.name
            self.degree_level = self.degree.level
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('degree', 'course')


class Instructor(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)


class Section(models.Model):
    SEMESTER_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    ]

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='sections')
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, related_name='sections')
    section_id = models.CharField(max_length=3)
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)
    year = models.IntegerField()
    enrolled_stu_num = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('course', 'section_id', 'semester', 'year')


class Objective(models.Model):
    objective_code = models.CharField(max_length=10)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'objective_code'),)


class Evaluation(models.Model):
    method = models.CharField(max_length=255)
    levelA_stu_num = models.IntegerField(null=True, blank=True)
    levelB_stu_num = models.IntegerField(null=True, blank=True)
    levelC_stu_num = models.IntegerField(null=True, blank=True)
    levelF_stu_num = models.IntegerField(null=True, blank=True)
    improvement_suggestions = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=255, default='Default Name')
    degree_level = models.CharField(max_length=50, default='Default Level')
    semester = models.CharField(max_length=6, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set semester and year from the associated section
        if not self.semester or not self.year:
            self.semester = self.section.semester
            self.year = self.section.year
        super().save(*args, **kwargs)


class EvaluatorObjective(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evaluation', 'objective')
