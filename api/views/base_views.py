from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


# dev_28
# def hello_world(request):
#     response_data = {}
#     response_data["hello"] = "hello"
#     response_data["world"] = "world"

#     return HttpResponse(json.dumps(response_data))  # json으로 바꿔서 응답하라.


# def hello_world_json(request):

#     response_data = {}
#     response_data["hello"] = "hello"
#     response_data["world"] = "world"

#     return JsonResponse(
#         response_data, status=400
#     )  # 400은 배드 리퀘스트 출력하는 실패 메세지.


# @api_view(["GET"])
# def hello_world_drf(request):
#     return Response({"message": "Hello World!"})  # rest framework 전용 response
