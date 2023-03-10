from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from defense.models import Defense 



class DefenseView(APIView):

    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        url_full = request.get_full_path()
        
        Defense.objects.create(ip=ip, route=url_full)

        return Response(status=status.HTTP_403_FORBIDDEN)


    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        url_full = request.get_full_path()    

        Defense.objects.create(ip=ip, route=url_full)

        return Response(status=status.HTTP_403_FORBIDDEN) 
    


class PingView(APIView):

    def get(self, request):

        return Response(status=status.HTTP_200_OK)