from django.shortcuts import render

# Create your views here.


def home(request):
	import json
	import requests

	if request.method =="POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zipcode+"&date=2020-11-10&distance=5&API_KEY=2B77F126-B706-4488-9132-4BB6BA5B8D23")


		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api ="Error..."


		if api[0]['Category']['Name'] =="Good":
			color = "good"
		elif api[0]['Category']['Name']=="Moderate":
			color = "Moderate"
		elif api[0]['Category']['Name'] =="Unhealthy for Sensitive Groups":
			color = "usg"
		elif api[0]['Category']['Name'] =="Unhealthy":
			color = "unhealthy"
		elif api[0]['Category']['Name'] =="Very Unhealthy":
			color = "veryunhealthy"
		elif api[0]['Category']['Name'] =="Hazardous":
			color = "hazardous"
		elif api[0]['Category']['Name'] =="Unavailable":
			color = "Unavailable"

		if api[1]['Category']['Name'] =="Good":
			color1 = "good"
		elif api[1]['Category']['Name']=="Moderate":
			color1 = "Moderate"
		elif api[1]['Category']['Name']=="Unhealthy for Sensitive Groups":
			color1 = "usg"
		elif api[1]['Category']['Name'] =="Unhealthy":
			color1 = "unhealthy"
		elif api[1]['Category']['Name'] =="Very Unhealthy":
			color1 = "veryunhealthy"
		elif api[1]['Category']['Name'] =="Hazardous":
			color1 = "hazardous"
		elif api[1]['Category']['Name'] =="Unavailable":
			color1 = "Unavailable"

		if api[2]['Category']['Name'] =="Good":
			color2 = "good"
		elif api[2]['Category']['Name']=="Moderate":
			color2 = "Moderate"
		elif api[2]['Category']['Name'] =="Unhealthy for Sensitive Groups":
			color2 = "usg"
		elif api[2]['Category']['Name'] =="Unhealthy":
			color2 = "unhealthy"
		elif api[2]['Category']['Name'] =="Very Unhealthy":
			colo1r = "veryunhealthy"
		elif api[2]['Category']['Name'] =="Hazardous":
			color2 = "hazardous"
		elif api[2]['Category']['Name'] =="Unavailable":
			color2 = "Unavailable"





		#https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-11-10&distance=5&API_KEY=2B77F126-B706-4488-9132-4BB6BA5B8D23
		return render (request,'home.html',{'api':api,'color1':color1,'color2':color2,'color':color})
		


	else:



		api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-11-10&distance=5&API_KEY=2B77F126-B706-4488-9132-4BB6BA5B8D23")


		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api ="Error..."


		if api[0]['Category']['Name'] =="Good":
			color = "good"
		elif api[0]['Category']['Name']=="Moderate":
			color = "Moderate"
		elif api[0]['Category']['Name'] =="Unhealthy for Sensitive Groups":
			color = "usg"
		elif api[0]['Category']['Name'] =="Unhealthy":
			color = "unhealthy"
		elif api[0]['Category']['Name'] =="Very Unhealthy":
			color = "veryunhealthy"
		elif api[0]['Category']['Name'] =="Hazardous":
			color = "hazardous"
		elif api[0]['Category']['Name'] =="Unavailable":
			color = "Unavailable"

		if api[1]['Category']['Name'] =="Good":
			color1 = "good"
		elif api[1]['Category']['Name']=="Moderate":
			color1 = "Moderate"
		elif api[1]['Category']['Name']=="Unhealthy for Sensitive Groups":
			color1 = "usg"
		elif api[1]['Category']['Name'] =="Unhealthy":
			color1 = "unhealthy"
		elif api[1]['Category']['Name'] =="Very Unhealthy":
			color1 = "veryunhealthy"
		elif api[1]['Category']['Name'] =="Hazardous":
			color1 = "hazardous"
		elif api[1]['Category']['Name'] =="Unavailable":
			color1 = "Unavailable"

		if api[2]['Category']['Name'] =="Good":
			color2 = "good"
		elif api[2]['Category']['Name']=="Moderate":
			color2 = "Moderate"
		elif api[2]['Category']['Name'] =="Unhealthy for Sensitive Groups":
			color2 = "usg"
		elif api[2]['Category']['Name'] =="Unhealthy":
			color2 = "unhealthy"
		elif api[2]['Category']['Name'] =="Very Unhealthy":
			colo1r = "veryunhealthy"
		elif api[2]['Category']['Name'] =="Hazardous":
			color2 = "hazardous"
		elif api[2]['Category']['Name'] =="Unavailable":
			color2 = "Unavailable"





		#https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-11-10&distance=5&API_KEY=2B77F126-B706-4488-9132-4BB6BA5B8D23
		return render (request,'home.html',{'api':api,'color1':color1,'color2':color2,'color':color})


def about(request):
	return render (request,'about.html',{})



