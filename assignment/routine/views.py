from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Routine, RoutineDay, RoutineResult
from .serializers import CreateRoutineSerializer, RoutineListSerializer, RoutineRetrieveSerializer
from datetime import datetime


class RoutineCreateView(APIView):
    def post(self, request):
        serializer = CreateRoutineSerializer(data=request.data)
        if serializer.is_valid():
            routine = Routine.objects.create(
                account=request.user,
                title=serializer.data['title'],
                category=serializer.data['category'],
                goal=serializer.data['goal'],
                is_alarm=serializer.data['is_alarm']
            )
            for i in serializer.data['days']:
                RoutineDay.objects.create(
                    day=i,
                    routine=routine
                )
            RoutineResult.objects.create(
                routine=routine
            )
            return Response({"data": {"routine_id": routine.id}, "message": {"msg": "You Have successfully created the routine.", "status": "ROUTINE_CREATE_OK"}}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)


class RoutineListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        CHOICES = (
            ('MON'),
            ('TUE'),
            ('WED'),
            ('THU'),
            ('FRI'),
            ('SAT'),
            ('SUN'),
        )
        day = datetime.today().weekday()
        queryset = RoutineResult.objects.select_related('routine').filter(
            routine__account=request.user, routine__day__day=CHOICES[day]).all()
        serializer = RoutineListSerializer(queryset, many=True)
        return Response({"data": serializer.data, "message": {"msg": "Routine lookup was successful.", "status": "ROUTINE_LIST_OK"}}, status=status.HTTP_200_OK)


class RoutineView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoutineRetrieveSerializer
    queryset = RoutineResult.objects.select_related('routine').all()

    def get(self, request, pk):
        queryset = RoutineResult.objects.select_related('routine').filter(
            routine__account=request.user, routine__id=pk).first()

        if not queryset:
            return Response({"message": {"msg": "Routine not extists.", "status": "ROUTINE_DETAIL_FAIL"}}, status=status.HTTP_204_NO_CONTENT)

        serializer = RoutineRetrieveSerializer(queryset)
        return Response({"data": serializer.data, "message": {"msg": "Routine lookup was successful.", "status": "ROUTINE_DETAIL_OK"}}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Routine.objects.filter(account=request.user, pk=pk).delete()
        return Response({"data":  {"routine_id": pk}, "message": {"msg": "The routine has been deleted.", "status": "ROUTINE_DELETE_OK"}}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = CreateRoutineSerializer(data=request.data)
        routine = Routine.objects.get(pk=pk)

        if serializer.is_valid():
            routine.title = serializer.data['title']
            routine.category = serializer.data['category']
            routine.goal = serializer.data['goal']
            routine.is_alarm = serializer.data['is_alarm']
            routine.modified_at = datetime.now()
            routine.save()
            RoutineDay.objects.filter(routine=routine).delete()
            RoutineResult.objects.filter(routine=routine).delete()
            for i in serializer.data['days']:
                RoutineDay.objects.create(
                    day=i,
                    routine=routine,
                    modified_at=datetime.now()
                )
            RoutineResult.objects.create(
                routine=routine,
                modified_at=datetime.now()
            )
        return Response({"data":  {"routine_id": pk}, "message": {"msg": "The routine has been modified.", "status": "ROUTINE_UPDATE_OK"}}, status=status.HTTP_200_OK)
