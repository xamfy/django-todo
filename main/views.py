from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import path, reverse


from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Schedule
from .serializers import ScheduleSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from .forms import ScheduleUpdateForm, ScheduleCreateForm
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'schedules': reverse('schedule-list', request=request, format=format)
    })


class ScheduleListView(ListView):
    model = Schedule
    context_object_name = 'schedules'
    template_name = 'home.html'

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Schedule.objects.filter(user=self.request.user)


class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleUpdateForm
    # fields = ['name', 'date', 'completed']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('home')


class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleCreateForm
    # fields = ['name', 'date', 'completed']
    template_name = 'add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.user = Schedule.objects.get(user=self.request.user)
        return super(ScheduleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class ScheduleDeleteView(DeleteView):
    model = Schedule

    def get_success_url(self):
        return reverse('home')

    # def get_queryset(self):
    #     owner = self.request.user
    #     return self.model.objects.filter(user=owner)


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
