from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from .models import Routine, RoutineDay, RoutineResult
from .serializers import CreateUpdateRoutineSerializer, RoutineDetailSerializer, RoutineSerializer
from datetime import datetime

class RoutineCreateView(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CreateUpdateRoutineSerializer
    def post(self, request):
        serializer = CreateUpdateRoutineSerializer(data=request.data)
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


class RoutineListView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=RoutineSerializer
    
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
        queryset=Routine.objects.prefetch_related('result').prefetch_related('days').filter(days__day=CHOICES[day])
        serializer=RoutineSerializer(queryset, many=True)
        return Response({"data": serializer.data, "message": {"msg": "Routine lookup was successful.", "status": "ROUTINE_LIST_OK"}}, status=status.HTTP_200_OK)

# class RoutineRetrieveDestroyUpdateView(generics.)
class RoutineView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoutineDetailSerializer
    
    def get(self, request, pk):
        queryset = Routine.objects.prefetch_related('result').filter(
            account=request.user, pk=pk).first()

        if not queryset:
            return Response({"message": {"msg": "Routine not extists.", "status": "ROUTINE_DETAIL_FAIL"}}, status=status.HTTP_204_NO_CONTENT)

        serializer = RoutineDetailSerializer(queryset)
        return Response({"data": serializer.data, "message": {"msg": "Routine lookup was successful.", "status": "ROUTINE_DETAIL_OK"}}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Routine.objects.filter(account=request.user, pk=pk).delete()
        return Response({"data":  {"routine_id": pk}, "message": {"msg": "The routine has been deleted.", "status": "ROUTINE_DELETE_OK"}}, status=status.HTTP_200_OK)

class RoutineUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateUpdateRoutineSerializer

    def put(self, request, pk):
        routine = Routine.objects.get(account=request.user,pk=pk)
        serializer = CreateUpdateRoutineSerializer(data=request.data)
        
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
        return Response({"data":  {"routine_id": pk}, "message": {"msg": "The routine has been modified.", "status": "ROUTINE_UPDATE_OK"}}, status=status.HTTP_201_CREATED)
