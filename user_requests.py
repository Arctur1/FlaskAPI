import requests


resp = requests.get('http://127.0.0.1:5000/health').json()
print(resp)

resp = requests.post('http://127.0.0.1:5000/posts/',
                     json={
                         'id': 1,
                         'title': 'test',
                         'author': 'test@test.test'
                     }).json()

resp = requests.get('http://127.0.0.1:5000/posts/1').json()
print(resp)

resp = requests.delete('http://127.0.0.1:5000/posts/1').json()
print(resp)

