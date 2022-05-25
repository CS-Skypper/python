import requests

url = "https://currency-converter5.p.rapidapi.com/currency/convert"

querystring = {"format":"json","from":"AUD","to":"CAD","amount":"1"}

headers = {
	"X-RapidAPI-Host": "currency-converter5.p.rapidapi.com",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)