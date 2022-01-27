import requests

#Making a GET request
r = requests.get('https://github.com/AdamMonahan')

#print(r)

#Print the request object
print(r.url)

#Print status code
print(r.status_code)