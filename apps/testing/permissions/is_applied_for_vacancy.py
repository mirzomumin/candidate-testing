from rest_framework import permissions


class IsAppliedForVacancy(permissions.BasePermission):
    message = 'You are not allowed to start this test'
    message += ', because You didn\'t apply for the vacancy.'
    def has_permission(self, request, view):
        user_applied_vacancies = request.user.vacancies.all()
        if user_applied_vacancies is not None:
            test = view.kwargs.get('test_id')
            return any([vacancy.test.id == test for vacancy in user_applied_vacancies])
        return False