import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import SignalStrength

def show_dashboard(request):
  return render(request, 'dashboard.html')

@csrf_exempt
def add_to_database(request):
  if request.method == "POST":
    try:
      operator = request.POST["operatorName"]
      latitude = request.POST["latitude"]
      longitude = request.POST["longitude"]
      address = request.POST["address"]
      output = {
        "Operator": operator,
        "Latitude": latitude,
        "Longitude": longitude,
        "Address": address
      }
      # print(json.dumps(output, indent=2))
      SignalStrength.objects.create(operator_name=operator, latitude=latitude, longitude=longitude, address=address)
      print("Adding to database: " + operator)
      return HttpResponse("Success")
    except Exception as e:
      print('Error', e)
      return HttpResponse("Failure")