import requests
import sys
username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

response = requests.get("http://natas1.natas.labs.overthewire.org", auth=(username, password))

sys.stdout = open("results.html", "w")
print(response.text)
sys.stdout.close()

#pass is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi