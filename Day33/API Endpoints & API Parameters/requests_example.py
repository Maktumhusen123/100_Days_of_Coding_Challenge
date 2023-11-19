import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)
response.raise_for_status()     # instead of raising individual exception for status code this will do that for us.
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

'''
1XX : Hold on
2XX : Here you go
3XX : Go away
4XX : You screwed up
5XX : I(server) screwed up
'''
