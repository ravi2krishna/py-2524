# External Module

import requests # ModuleNotFoundError: No module named 'requests'
r = requests.get('https://www.python.org/')
print(r.status_code)

r = requests.get('https://www.python.org/ravi')
print(r.status_code)

if r.status_code != 200:
    print("API Not Found")
else:
    print("API Found")
    print("Processing Data With API")