from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from asset import core
# Create your views here.

@csrf_exempt
def asset_with_no_asset_id(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        res = ass_handler.get_asset_id_by_sn()

        # return render(request,'assets/acquire_asset_id_test.html',{'response':res})
        return HttpResponse(json.dumps(res))
