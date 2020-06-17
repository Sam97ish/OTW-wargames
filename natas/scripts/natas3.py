import requests
import sys
username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

response = requests.get("http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt", auth=(username, password))

sys.stdout = open("results.html", "w")
print(response.text)
sys.stdout.close()

#found pass is Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ