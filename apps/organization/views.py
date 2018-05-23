from django.shortcuts import render

from django.views.generic.base import View


class TeachersList(View):
    def get(self, request):
        return render(request, 'teachers_list.html', {})


class OrgList(View):
    def get(self, request):
        return render(request, 'org_list.html', {})
