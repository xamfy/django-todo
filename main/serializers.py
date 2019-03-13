from rest_framework import serializers
from .models import Schedule
from django.contrib.auth.models import User


class ScheduleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Schedule
        fields = ('id', 'user', 'name', 'date', 'completed')


class UserSerializer(serializers.ModelSerializer):
    schedules = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Schedule.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'schedules')
