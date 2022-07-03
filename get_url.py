import requests

url = 'https://www.google.com/'
#url='https://www.youtube.com/watch?v=h3sxUR6i8tc'
response = requests.get(url)        # To execute get request
print(response.status_code)     # To print http response code
#print(response.text)