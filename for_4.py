import requests

url = 'https://api.raise3d.com/webtest/user/login'

body = {
    'email': 'zihaoxujob@163.com',
    'password':	'0c6d47a02431f6d346dc9cbce7219174cf1a47d8'
}

h = {
    'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url=url,data=body,headers=h)
print(r.json())


