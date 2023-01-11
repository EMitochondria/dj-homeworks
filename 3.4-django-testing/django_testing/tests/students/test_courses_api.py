import pytest
from rest_framework.test import APIClient
from students.models import Course, Student
from model_bakery import baker
from rest_framework import status
from django.urls import reverse
from django_testing.settings import MAX_STUDENTS_PER_COURSE

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return  baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return  baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_api_course_one(client, course_factory):
    """Проверка получения 1го курса"""
    courses = course_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data['name'] == courses[0].name

@pytest.mark.django_db
def test_api_courses_list(client, course_factory):
    """Проверка получения списка курсов"""
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name

@pytest.mark.django_db
def test_api_course_filter_by_id(client, course_factory):
    """Проверка фильтрации списка курсов по id"""
    courses = course_factory(_quantity=10)    
    id = courses[0].id
    response =  client.get(reverse('courses-list'), kwargs = {'id': id})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    for i, course in enumerate(data):
        assert course['id'] == courses[i].id

@pytest.mark.django_db
def test_api_course_filter_by_name(client, course_factory):
    """Проверка фильтрации списка курсов по name"""
    courses = course_factory(_quantity=10)  
    response =  client.get(reverse('courses-list'), kwargs= {'name': courses[1].name})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name

@pytest.mark.django_db
def test_create_course(client, student_factory):
    """Проверка успешного создания курса"""
    count_courses = Course.objects.count()
    students = student_factory(_quantity=1)
    list_students_id = []
    for student in students:
        list_students_id.append(student.id)
    response =  client.post('/api/v1/courses/', data = {'name': 'test', 'students': list_students_id})
    assert response.status_code == status.HTTP_201_CREATED
    assert count_courses+1 == Course.objects.count()

@pytest.mark.django_db
def test_courses_update(client, course_factory, student_factory):
    """Проверка успешного обновления курса"""    
    courses = course_factory(_quantity=1)    
    students = student_factory(_quantity=1)
    list_students_id = []
    for student in students:
        list_students_id.append(student.id)
    new_name = 'modified'
    data = {
        'name': new_name,
        'students': list_students_id
    }
    for course in courses:
        response = client.patch(reverse('courses-detail', args=[course.id]), data = data)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data['name'] == new_name

@pytest.mark.django_db
def test_courses_delete(client, course_factory):
    """Проверка успешного удаления курса"""    
    courses = course_factory(_quantity=1)
    for course in courses:
        response = client.delete(reverse('courses-detail', args=[course.id]))
        print(response.status_code)
        assert response.status_code == status.HTTP_204_NO_CONTENT
   
@pytest.mark.django_db
def test_max_student_count_on_course(client, course_factory, student_factory):
    """Проверка на максимальное число студентов на одном курсе 20 c student_factory"""    
    courses = course_factory(_quantity=1)
    students = student_factory(_quantity=20)
    list_students_id = []
    for student in students:
        list_students_id.append(student.id)
    for course in courses:
        response = client.patch(reverse('courses-detail', args=[course.id]), {'name': course.name, "students": list_students_id})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
