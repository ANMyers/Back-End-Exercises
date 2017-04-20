from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import *


class HockeyTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyTeam
        fields = ('url', 'teamname', 'city', 'coach', 'mascot')

class HockeyPlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyPlayer
        exclude = ()
        depth = 1

class TornadoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tornadoes
        fields = ('url', 'classification', 'color', 'radius', 'speed', 'direction', 'date')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')