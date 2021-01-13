from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializer import UserModelSerializer, EmployeesModelSerializer
from rest_framework.generics import GenericAPIView, DestroyAPIView

from api.models import User, Employee


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # print(request.GET, request.query_params)
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        # print(username, password)

        objects_filter = User.objects.filter(username=username, password=password).first()
        # print(objects_filter)
        if objects_filter:
            data = UserModelSerializer(objects_filter).data
            # print(data)
            return Response({
                'results': data, 'message': True
            }, status=status.HTTP_200_OK)
        return Response({
            'results': '登录参数有误', 'message': False
        }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer_save = serializer.save()
        return Response({'results': UserModelSerializer(serializer_save).data})


class EmployeesAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       GenericAPIView,
                       ):
    queryset = Employee.objects.all()
    serializer_class = EmployeesModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        print(request.data)
        print(kwargs.get('id'))
        if kwargs.get('id'):
            first = Employee.objects.filter(pk=kwargs.get('id')).first()
            print(first)
            return Response({
                'results': EmployeesModelSerializer(first).data
            })
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print(request.data)
        # print(kwargs.get('id'))
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print(request.data.get('img'))
        return self.partial_update(request, *args, **kwargs)
