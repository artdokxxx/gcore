from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from app.services.project_info import ProjectInfoService


class ProjectInfoView(APIView):
    def get(self, request):
        info_handler = ProjectInfoService()

        res = info_handler.get_info()
        res['started'] = settings.START_TIME.strftime('%Y-%m-%dT%H:%M:%SZ')
        res['uptime_seconds'] = (datetime.now() - settings.START_TIME).seconds

        return Response(res)
