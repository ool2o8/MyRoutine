from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Routine, RoutineDay, RoutineResult
from .serializers import CreateRoutineSerializer
class CreateRoutine(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=CreateRoutineSerializer
    queryset=Routine.objects.all()
    def post(self, request):
        serializer=CreateRoutineSerializer(data=request.data)
        if serializer.is_valid():
            routine=Routine.objects.create(
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
            return Response({"data":{"routine_id": routine.id},"message":{"msg": "You Have successfully created the routine.", "status":"ROUTINE_CREATE_OK"}}, status=status.HTTP_201_CREATED)
        else:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)