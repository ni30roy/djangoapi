from rest_framework import serializers
from courses.models import Courses

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Courses
        fields=("id","name","url","lang","price")