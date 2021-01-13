from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'username': {
                'required': True,
                # 'min_length': 2,
                'max_length': 8,
            },
            'password': {
                'required': True,
                'max_length': 16,
                'min_length': 6,
            },
            'real_name': {
                'required': True,
            },
            'gender': {
                'required': True,
            },
        }

    def validate_username(self, data):
        print(data)

        value__first = User.objects.filter(username=data).first()
        if value__first:
            raise serializers.ValidationError('用户名重复无法注册')
        return data


class EmployeesModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        # 'id', 'emp_name', 'salary', 'full_img', 'age', 'img'
        fields = ('id', 'emp_name', 'salary', 'full_img', 'age', 'img')

        extra_kwargs = {
            'full_img': {
                'read_only': True
            },
            'img': {
                'write_only': True
            }
        }
