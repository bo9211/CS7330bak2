from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect ,get_object_or_404
from university import models ,forms
from django.contrib import messages
from django.db.models import Case, When, Value, CharField, Q, Count
from django.shortcuts import render
# Course
def course(request):
    queryset = models.Course.objects.all().order_by('course_id')
    return render(request, 'university/course/course.html',{'queryset':queryset})

def add_course(request):
    if request.method == "GET":
        return render(request,'university/course/add_course.html')
    Course_Id = request.POST.get("course_id")
    Name = request.POST.get("name")
    models.Course.objects.create(course_id=Course_Id, name=Name)
    return redirect("/course/")

def delete_course(request):
    Course_Id = request.GET.get("course_id")
    models.Course.objects.filter(course_id=Course_Id).delete()
    return redirect("/course/")
    
def edit_course(request, Course_Id):
    if request.method =='GET':
        row_object = models.Course.objects.filter(course_id=Course_Id).first()
        return render(request,'university/course/edit_course.html', {"row_object":row_object})
    
    Name = request.POST.get("name")
    models.Course.objects.filter(course_id=Course_Id).update(name=Name)
    return redirect("/course/")



# Degree
def degree(request):
    queryset = models.Degree.objects.all()
    return render(request, 'university/degree/degree.html',{'queryset':queryset})

def add_degree(request):
    if request.method == "GET":
        return render(request,'university/degree/add_degree.html')
    # Degree_Id = request.POST.get("degree_id")
    Name = request.POST.get("name")
    Level = request.POST.get("level")
    models.Degree.objects.create(name=Name,level=Level)
    return redirect("/degree/")

def delete_degree(request):
    name = request.GET.get('name')
    level = request.GET.get('level')
    if name and level:
        models.Degree.objects.filter(name=name, level=level).delete()
    return redirect('/degree/')

def edit_degree(request, Name):
    if request.method =='GET':
        row_object = models.Degree.objects.filter(name=Name).first()
        return render(request,'university/degree/edit_degree.html', {"row_object":row_object})
    
    Level = request.POST.get("level")
    models.Degree.objects.filter(name=Name).update(level=Level)
    return redirect("/degree/")



# DegreeCourse
def degreecourse(request):
    queryset = models.DegreeCourse.objects.all()
    return render(request, 'university/degreecourse/degreecourse.html',{'queryset':queryset})

def add_degreecourse(request):
    if request.method == "POST":
        is_core = request.POST.get("is_core", "False") == "True"
        course_id = request.POST.get("course_id")
        degree_id = request.POST.get("degree_id")
        
        try:
            course = models.Course.objects.get(course_id=course_id)
            degree = models.Degree.objects.get(pk=degree_id)
        except models.Course.DoesNotExist:
            return HttpResponse("The specified course does not exist.", status=404)
        except models.Degree.DoesNotExist:
            return HttpResponse("The specified degree does not exist.", status=404)

        try:
            degree_course = models.DegreeCourse.objects.create(
                is_core=is_core,
                course=course,
                degree=degree
            )
        except Exception as e:
            return HttpResponse(f"An error occurred when creating the DegreeCourse: {e}", status=400)
        return redirect("/degreecourse/")  
    return render(request, 'university/degreecourse/add_degreecourse.html')

def delete_degreecourse(request):
    course_id = request.GET.get('course_id')
    degree_id = request.GET.get('degree_id')
    
    if course_id and degree_id:
        try:
            degree_course = models.DegreeCourse.objects.get(
                course__course_id=course_id, 
                degree__id=degree_id
            )
            degree_course.delete()
            return redirect('/degreecourse/')
        except models.DegreeCourse.DoesNotExist:
            return HttpResponse('DegreeCourse object does not exist.', status=404)
    else:
        return HttpResponse('Missing course_id or degree_id parameter.', status=400)
 
def edit_degreecourse(request, Course_Id):
    if request.method =='GET':
        row_object = models.DegreeCourse.objects.filter(course_id=Course_Id).first()
        return render(request,'university/degreecourse/edit_degreecourse.html', {"row_object":row_object})
    
    Is_Core = request.POST.get("is_core")
    Degree_Id = request.POST.get("degree_id")
    models.DegreeCourse.objects.filter(course_id=Course_Id).update(is_core=Is_Core, degree_id=Degree_Id )
    return redirect("/degreecourse/")   



# Instructor
def instructor(request):
    queryset = models.Instructor.objects.all()
    return render(request, 'university/instructor/instructor.html',{'queryset':queryset})

def add_instructor(request):
    if request.method == "GET":
        return render(request,'university/instructor/add_instructor.html')
    Id = request.POST.get("id")
    Name = request.POST.get("name")
    models.Instructor.objects.create(id=Id, name=Name)
    return redirect("/instructor/")

def delete_instructor(request):
    Id = request.GET.get("id")
    models.Instructor.objects.filter(id=Id).delete()
    return redirect("/instructor/")
    
def edit_instructor(request, Id):
    if request.method =='GET':
        row_object = models.Instructor.objects.filter(id=Id).first()
        return render(request,'university/instructor/edit_instructor.html', {"row_object":row_object})
    
    Name = request.POST.get("name")
    models.Instructor.objects.filter(id=Id).update(name=Name)
    return redirect("/instructor/")

# Section
def section(request):
    queryset = models.Section.objects.all()
    return render(request, 'university/section/section.html',{'queryset':queryset})

def add_section(request):
    if request.method == "GET":
        return render(request,'university/section/add_section.html')
    Section_Id = request.POST.get("section_id")
    Degree_Id = request.POST.get("degree_id")
    Instructor_Id = request.POST.get("instructor_id")
    Course_Id = request.POST.get("course_id")
    Semester = request.POST.get("semester")
    Year = request.POST.get("year")
    Enrolled_Stu_Num = request.POST.get("enrolled_stu_num")
    
    models.Section.objects.create(degree_id=Degree_Id,section_id=Section_Id,course_id=Course_Id, 
                                  instructor_id=Instructor_Id, semester=Semester,
                                  year=Year, enrolled_stu_num=Enrolled_Stu_Num)
    return redirect("/section/")

def delete_section(request):
    Section_Id = request.GET.get("section_id")
    models.Section.objects.filter(section_id=Section_Id).delete()
    return redirect("/section/")
    
def edit_section(request, Section_Id):
    if request.method =='GET':
        row_object = models.Section.objects.filter(section_id=Section_Id).first()
        return render(request,'university/section/edit_section.html', {"row_object":row_object})
    
    Degree_Id = request.POST.get("degree_id")
    Instructor_Id = request.POST.get("instructor_id")
    Course_Id = request.POST.get("course_id")
    Semester = request.POST.get("semester")
    Year = request.POST.get("year")
    Enrolled_Stu_Num = request.POST.get("enrolled_stu_num")
    models.Section.objects.filter(section_id=Section_Id).update(degree_id=Degree_Id,course_id=Course_Id, 
                                  instructor_id=Instructor_Id, semester=Semester,
                                  year=Year, enrolled_stu_num=Enrolled_Stu_Num)
    return redirect("/section/")



# Objective
def objective(request):
    queryset = models.Objective.objects.all()
    return render(request, 'university/objective/objective.html',{'queryset':queryset})

def add_objective(request):
    if request.method == "GET":
        return render(request,'university/objective/add_objective.html')
    Objective_Code = request.POST.get("objective_code")
    Title = request.POST.get("title")
    Description = request.POST.get("description")
    Course_Id = request.POST.get("course_id")
    models.Objective.objects.create(objective_code=Objective_Code,  title= Title, description=Description,course_id=Course_Id)
    return redirect("/objective/")

def delete_objective(request):
    Objective_Code = request.GET.get("objective_code")
    models.Objective.objects.filter(objective_code=Objective_Code).delete()
    return redirect("/objective/")
    
def edit_objective(request, Objective_Code):
    if request.method =='GET':
        row_object = models.Objective.objects.filter(objective_code=Objective_Code).first()
        return render(request,'university/objective/edit_objective.html', {"row_object":row_object})
    
    Title = request.POST.get("title")
    Description = request.POST.get("description")
    models.Objective.objects.filter(objective_code=Objective_Code).update(title= Title, description=Description)
    return redirect("/objective/")


# Evaluation
def evaluation(request):
    queryset = models.Evaluation.objects.all()
    return render(request, 'university/evaluation/evaluation.html',{'queryset':queryset})

def add_evaluation(request):
    if request.method == "GET":
        return render(request,'university/evaluation/add_evaluation.html')
    Evaluate_Id = request.POST.get("evaluate_id")
    Method = request.POST.get("method")
    LevelA_Stu_Num = request.POST.get("levelA_stu_num")
    LevelB_Stu_Num = request.POST.get("levelB_stu_num")
    LevelC_Stu_Num = request.POST.get("levelC_stu_num")
    LevelF_Stu_Num = request.POST.get("levelF_stu_num")
    Improvement_Suggestions = request.POST.get("improvement_suggestions")
    Degree_Id = request.POST.get("degree_id")
    Section_Id = request.POST.get("section_id")
    Course_Id = request.POST.get("course_id")
    models.Evaluation.objects.create(evaluate_id=Evaluate_Id, method=Method, 
                                 levelA_stu_num=LevelA_Stu_Num, levelB_stu_num=LevelB_Stu_Num,
                                 levelC_stu_num=LevelC_Stu_Num,levelF_stu_num=LevelF_Stu_Num,
                                 improvement_suggestions=Improvement_Suggestions,degree_id=Degree_Id,section_id=Section_Id,course_id=Course_Id)
    return redirect("/evaluation/")

def delete_evaluation(request):
    Evaluate_Id = request.GET.get("evaluate_id")
    models.Evaluation.objects.filter(evaluate_id=Evaluate_Id).delete()
    return redirect("/evaluation/")
    
def edit_evaluation(request, Evaluate_Id):
    if request.method =='GET':
        row_object = models.Evaluation.objects.filter(evaluate_id=Evaluate_Id).first()
        return render(request,'university/evaluation/edit_evaluation.html', {"row_object":row_object})
    
    Method = request.POST.get("method")
    LevelA_Stu_Num = request.POST.get("levelA_stu_num")
    LevelB_Stu_Num = request.POST.get("levelB_stu_num")
    LevelC_Stu_Num = request.POST.get("levelC_stu_num")
    LevelF_Stu_Num = request.POST.get("levelF_stu_num")
    Improvement_Suggestions = request.POST.get("improvement_suggestions")
    Degree_Id = request.POST.get("degree_id")
    Section_Id = request.POST.get("section_id")
    Course_Id = request.POST.get("course_id")
    models.Evaluation.objects.filter(evaluate_id=Evaluate_Id).update(method=Method, 
                                 levelA_stu_num=LevelA_Stu_Num, levelB_stu_num=LevelB_Stu_Num,
                                 levelC_stu_num=LevelC_Stu_Num,levelF_stu_num=LevelF_Stu_Num,
                                 improvement_suggestions=Improvement_Suggestions,degree_id=Degree_Id, section_id=Section_Id,course_id=Course_Id)
    return redirect("/evaluation/")


 
def evaluationquery(request):
    semester_param = request.GET.get('semester', None)
    context = {'initial_load': True}

    if semester_param and len(semester_param) > 4:
        year = semester_param[:4]
        semester = semester_param[4:]
        if year.isdigit() and semester.isalpha():
            evaluations = models.Evaluation.objects.filter(
                section__semester=semester, 
                section__year=int(year)
            )

            if not evaluations:
                context['message'] = 'No data available for the provided semester.'
            else:
                unique_courses = evaluations.values(
                    'course__course_id', 'section__section_id', 'section__semester', 'section__year'
                ).annotate(
                    count=Count('evaluate_id'),
                    filled_suggestions_count=Count('improvement_suggestions', filter=Q(improvement_suggestions__isnull=False)),
                    filled_evaluation_count=Count('evaluate_id', filter=Q(levelA_stu_num__isnull=False, levelB_stu_num__isnull=False, levelC_stu_num__isnull=False, levelF_stu_num__isnull=False)),
                ).distinct()

                # 计算每个组合的“Suggestions”和“Evaluated”状态
                for course in unique_courses:
                    course['suggestions_status'] = calculate_status(course['filled_suggestions_count'], course['count'])
                    course['evaluated_status'] = calculate_status(course['filled_evaluation_count'], course['count'])

                context.update({
                    'unique_courses': unique_courses,
                    'semester': semester,
                    'year': year,
                    'initial_load': False
                })
        else:
            context['error'] = 'Invalid semester format.'
    else:
        context['error'] = 'Please enter a valid semester (e.g., 2024Fall).'

    return render(request, 'university/evaluation/evaluationquery.html', context)


def calculate_status(filled_count, total_count):
    if filled_count == 0:
        return 'Not entered'
    elif filled_count < total_count:
        return 'Partly entered'
    else:
        return 'Entered'


# # 及格率查询
# def handle_pass_rate_query(request, semester_param, percentage_param):
#     try:
#         year = semester_param[:4]
#         semester = semester_param[4:]
#         queryset = models.Evaluation.objects.filter(
#             section__semester=semester,
#             section__year=int(year)
#         )
#         if not queryset:
#             return render(request, 'university/evaluation/passratequery.html', {'message': 'No evaluations found for the provided semester.'})
        
#         total_passed = total_students = 0
#         for eval in queryset:
#             # Check if all fields are filled
#             if eval.levelA_stu_num is None or eval.levelB_stu_num is None or eval.levelC_stu_num is None or eval.levelF_stu_num is None:
#                 continue  # Skip this evaluation as it is incomplete

#             levelA = eval.levelA_stu_num
#             levelB = eval.levelB_stu_num
#             levelC = eval.levelC_stu_num
#             levelF = eval.levelF_stu_num

#             passed = levelA + levelB + levelC
#             total = passed + levelF

#             if total > 0:
#                 total_passed += passed
#                 total_students += total

#         if total_students > 0:
#             pass_rate = (total_passed / total_students) * 100
#             if pass_rate >= float(percentage_param):
#                 return render(request, 'university/evaluation/passratequery.html', {
#                     'pass_rate': f'Pass rate is {pass_rate:.2f}% and meets or exceeds the threshold of {percentage_param}%.'})
#             else:
#                 return render(request, 'university/evaluation/passratequery.html', {
#                     'pass_rate': f'Pass rate is {pass_rate:.2f}% and does not meet the threshold of {percentage_param}%.'})
#         else:
#             return render(request, 'university/evaluation/passratequery.html', {'message': 'No complete student data available to calculate pass rate.'})

#     except ValueError:
#         return render(request, 'university/evaluation/passratequery.html', {'error': 'Invalid semester format or percentage value.'})

# # 及格率查询
# def passratequery(request):
#     semester_param = request.GET.get('semester', None)
#     percentage_param = request.GET.get('percentage', None)
#     if semester_param is None or percentage_param is None:
#         return render(request, 'university/evaluation/passratequery.html', {'initial_load': True})
#     if semester_param == '' or percentage_param == '':
#         return render(request, 'university/evaluation/passratequery.html', {'error': 'Both semester and percentage are required.'})
    
#     return handle_pass_rate_query(request, semester_param, percentage_param)

# 及格率查询辅助函数
def handle_pass_rate_query(request, semester_param, percentage_param):
    try:
        year = semester_param[:4]
        semester = semester_param[4:]
        queryset = models.Evaluation.objects.filter(
            section__semester=semester,
            section__year=int(year)
        ).exclude(
            levelA_stu_num__isnull=True,
            levelB_stu_num__isnull=True,
            levelC_stu_num__isnull=True,
            levelF_stu_num__isnull=True
        )  # 排除未完全评估的数据

        course_pass_rates = []
        if not queryset:
            return render(request, 'university/evaluation/passratequery.html', {'message': 'No evaluations found for the provided semester.'})
        
        for eval in queryset:
            levelA = eval.levelA_stu_num or 0
            levelB = eval.levelB_stu_num or 0
            levelC = eval.levelC_stu_num or 0
            levelF = eval.levelF_stu_num or 0

            passed = levelA + levelB + levelC
            total = passed + levelF

            if total > 0:
                pass_rate = (passed / total) * 100
                if pass_rate >= float(percentage_param):
                    course_pass_rates.append({
                        'semester': semester,
                        'year': year,
                        'course_id': eval.course.course_id,
                        'section_id': eval.section.section_id,
                        'pass_rate': pass_rate
                    })

        if course_pass_rates:
            return render(request, 'university/evaluation/passratequery.html', {
                'course_pass_rates': course_pass_rates
            })
        else:
            return render(request, 'university/evaluation/passratequery.html', {'message': 'No sections meet the threshold.'})

    except ValueError:
        return render(request, 'university/evaluation/passratequery.html', {'error': 'Invalid semester format or percentage value.'})

# 及格率查询视图
def passratequery(request):
    semester_param = request.GET.get('semester', None)
    percentage_param = request.GET.get('percentage', None)
    if semester_param is None or percentage_param is None:
        return render(request, 'university/evaluation/passratequery.html', {'initial_load': True})
    if semester_param == '' or percentage_param == '':
        return render(request, 'university/evaluation/passratequery.html', {'error': 'Both semester and percentage are required.'})
    
    return handle_pass_rate_query(request, semester_param, percentage_param)



def query_course(request):
    form = forms.QueryCourseForm(request.POST or None)
    sections = None

    if request.method == 'POST' and form.is_valid():
        course = form.cleaned_data['course']
        year = form.cleaned_data['year']
        semester = form.cleaned_data['semester']
        sections = models.Section.objects.filter(
            course=course,
            year=year,
            semester=semester
        )
    return render(
        request,
        'university/course/course_result.html',
        {'form': form, 'sections': sections}
    )


def instructor_sections(request):
    form = forms.QueryInstructorForm(request.POST or None)
    sections = None
    if request.method == 'POST' and form.is_valid():
        instructor = form.cleaned_data['instructor']
        year = form.cleaned_data['year']
        semester = form.cleaned_data['semester']
        sections = models.Section.objects.filter(
            instructor=instructor,
            year=year,
            semester=semester
        )

    return render(request, 'university/instructor/instructor_result.html', {
        'form': form,
        'sections': sections
    })


def degree_details(request):
    # Initialize the form with POST data or None
    form = forms.DegreeQueryForm(request.POST or None)

    # Prepare the initial context
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        degree = form.cleaned_data['degree']

        if degree:
            courses = models.Course.objects.filter(degreecourse__degree=degree)
            sections = models.Section.objects.filter().order_by('-year', 'semester')

            objectives = models.Objective.objects.all()

            objectives_courses = {
                objective: models.Course.objects.filter(objective=objective)
                for objective in objectives
            }

            context.update({
                'degree': degree,
                'courses': courses,
                'sections': sections,
                'objectives': objectives,
                'objectives_courses': objectives_courses,
            })

    return render(request, 'university/degree/degree_result.html', context)




def evaluation_detail(request, id):
    # Get evaluation object or return 404
    evaluation = get_object_or_404(models.Evaluation, evaluate_id=id)

    # Initialize the form with POST data if applicable
    form = forms.EvaluationQueryForm(request.POST or None)
    # Collect evaluation information
    evaluations = models.Evaluation.objects.all()
    evaluations_info = [
        {
            'evaluate_id': eval.evaluate_id,
            'method': eval.method or 'Not Entered',
            'levelA_stu_num': eval.levelA_stu_num or 'Not Entered',
            'levelB_stu_num': eval.levelB_stu_num or 'Not Entered',
            'levelC_stu_num': eval.levelC_stu_num or 'Not Entered',
            'levelF_stu_num': eval.levelF_stu_num or 'Not Entered',
            'improvement_suggestions': eval.improvement_suggestions or 'Not Entered',
            'course': eval.course or 'Not Entered',
            'section': eval.section or 'Not Entered',
            'degree_name': eval.degree_name or 'Not Entered',
            'degree_level': eval.degree_level or 'Not Entered',
        }
        for eval in evaluations
    ]

    # Identify missing information for each evaluation
    incomplete_evaluations = {}
    for info in evaluations_info:
        missing_fields = [
            field_name
            for field_name, field_value in info.items()
            if field_value == 'Not Entered'
        ]
        if missing_fields:
            incomplete_evaluations[info['evaluate_id']] = missing_fields

    # Validate and process the form if POST method and form is valid
    if request.method == 'POST' and form.is_valid():
        degree = form.cleaned_data['degree']
        instructor = form.cleaned_data['instructor']
        semester = form.cleaned_data['semester']
        year = form.cleaned_data['year']
        # Retrieve courses for the given instructor and semester
        sections = models.Section.objects.filter(instructor=instructor, semester=semester, year=year, degree=degree)
        return render(
            request,
            'university/evaluation/enter_evaluations.html',
            {'sections': sections, 'form': form  , 'evaluation': evaluation, 'total_evaluations': len(evaluations),
            'evaluations_info': evaluations_info,
            'incomplete_evaluations': incomplete_evaluations,}
        )

    return render(
        request,
        'university/evaluation/enter_evaluations.html',
        {
            'evaluation': evaluation,
            'form': form,
            'total_evaluations': len(evaluations),
            'evaluations_info': evaluations_info,
            'incomplete_evaluations': incomplete_evaluations,
        }
    )

def copy_evaluation(request ):
        if request.method == 'POST':
            form = forms.DegreeCopyForm(request.POST)

            if form.is_valid():
                source_degree = form.cleaned_data['source_degree']
                target_degrees = form.cleaned_data['target_degrees']

                if source_degree and target_degrees:
                    for target_degree in target_degrees:
                        try:
                            existing_evaluation = models.Evaluation.objects.get(
                                degree_name=target_degree.degree_name,
                                degree_level=target_degree.degree_level
                            )
                            existing_evaluation.levelA_stu_num = source_degree.levelA_stu_num
                            existing_evaluation.levelB_stu_num = source_degree.levelB_stu_num
                            existing_evaluation.levelC_stu_num = source_degree.levelC_stu_num
                            existing_evaluation.levelF_stu_num = source_degree.levelF_stu_num
                            existing_evaluation.method = source_degree.method
                            existing_evaluation.improvement_suggestions = source_degree.improvement_suggestions
                            existing_evaluation.save()
                        except models.Evaluation.DoesNotExist:
                            models.Evaluation.objects.create(
                                degree_name=target_degree.degree_name,
                                degree_level=target_degree.degree_level,
                                method=source_degree.method,
                                levelA_stu_num=source_degree.levelA_stu_num,
                                levelB_stu_num=source_degree.levelB_stu_num,
                                levelC_stu_num=source_degree.levelC_stu_num,
                                levelF_stu_num=source_degree.levelF_stu_num,
                                improvement_suggestions=source_degree.improvement_suggestions,
                            )
                    messages.success(request, 'Evaluation copied successfully!')
                else:
                    messages.error(request, 'Invalid form select.')

            context = {
                'form': forms.DegreeCopyForm(),
                'messages': list(messages.get_messages(request)),  # Retrieve message list
            }

            return render(request, 'university/evaluation/copy_evaluations.html', context)
        else:

            return render(
                request,
                'university/evaluation/copy_evaluations.html',
                {'form': forms.DegreeCopyForm()}
            )