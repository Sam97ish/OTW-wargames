import requests
import sys
username = "natas0"
password = "natas0"

response = requests.get("http://natas0.natas.labs.overthewire.org", auth=(username, password))

sys.stdout = open("results.html", "w")
print(response.text)
sys.stdout.close()

#pass is  gtVrDuiDfck831PqWsLEZy5gyDz1clto