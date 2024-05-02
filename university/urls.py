from django.urls import path
from university import views

app_name ='university'
urlpatterns = [
    # Degree
    path('degree/', views.degree, name='degree'),
    path('degree/add_degree/', views.add_degree, name='add_degree'),
    path('degree/delete_degree/', views.delete_degree, name='delete_degree'),
    path('degree/<str:Name>/edit_degree/', views.edit_degree, name='edit_degree'),
    
     # DegreeCourse
    path('degreecourse/', views.degreecourse, name='degreecourse'),
    path('degreecourse/add_degreecourse/', views.add_degreecourse, name='add_degreecourse'),
    path('degreecourse/delete_degreecourse/', views.delete_degreecourse, name='delete_degreecourse'),
    path('degreecourse/<str:Course_Id>/edit_degreecourse/', views.edit_degreecourse, name='edit_degreecourse'),
    
    # Course
    path('course/', views.course, name='course'),
    path('course/add_course/', views.add_course, name='add_course'),
    path('course/delete_course/', views.delete_course, name='delete_course'),
    path('course/<str:Course_Id>/edit_course/', views.edit_course, name='edit_course'),
    
    # Instructor
    path('instructor/', views.instructor, name='instructor'),
    path('instructor/add_instructor/', views.add_instructor, name='add_instructor'),
    path('instructor/delete_instructor/', views.delete_instructor, name='delete_instructor'),
    path('instructor/<str:Id>/edit_instructor/', views.edit_instructor, name='edit_instructor'),
    
    # Section
    path('section/', views.section, name='section'),
    path('section/add_section/', views.add_section, name='add_section'),
    path('section/delete_section/', views.delete_section, name='delete_section'),
    path('section/<str:Section_Id>/edit_section/', views.edit_section, name='edit_section'),
    
    
    # Objective
    path('objective/', views.objective, name='objective'),
    path('objective/add_objective/', views.add_objective, name='add_objective'),
    path('objective/delete_objective/', views.delete_objective, name='delete_objective'),
    path('objective/<str:Objective_Code>/edit_objective/', views.edit_objective, name='edit_objective'),
    
    
    
    # Evaluation
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluation/add_evaluation/', views.add_evaluation, name='add_evaluation'),
    path('evaluation/delete_evaluation/', views.delete_evaluation, name='delete_evaluation'),
    path('evaluation/<str:Evaluate_Id>/edit_evaluation/', views.edit_evaluation, name='edit_evaluation'),
    # Queries involving evaluations
    path('evaluationquery/', views.evaluationquery, name='evaluationquery'),
    path('passratequery/', views.passratequery, name='passratequery'),

    # queryDetail
    path('course_result/', views.query_course, name='course_result'),
    path('instructor_result/', views.instructor_sections, name='instructor_result'),
    path('degree_result/', views.degree_details, name='degree_result'),

    path('enter_evaluations/', views.evaluation_detail, name='enter_evaluations'),
    path('copy_evaluations/', views.copy_evaluation, name='copy_evaluations'),

]