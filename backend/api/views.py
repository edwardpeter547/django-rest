import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body
    params = request.GET
    post = request.POST

    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(body)
    print(params)
    data["params"] = dict(params)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
