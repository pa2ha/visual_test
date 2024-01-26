from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from .forms import CustomUserForm
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(CreateModelMixin,
                        DestroyModelMixin,
                        viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        return render(request, 'user_list.html', {'users': users})

    return HttpResponseNotAllowed(['GET'])


def user_detail(request, pk):
    if request.method == 'GET':
        user = get_object_or_404(CustomUser, pk=pk)
        return render(request, 'user_detail.html', {'user': user})

    return HttpResponseNotAllowed(['GET'])


def user_create(request):
    form = CustomUserForm
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан!')
            return redirect('user_list')

    return render(request, 'user_form.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST' or request.method == 'DELETE':
        user.delete()
        messages.success(request, 'Пользователь успешно удален!')
        return redirect('user_list')

    return HttpResponseNotAllowed(['POST'])
