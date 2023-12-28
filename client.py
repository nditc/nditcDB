import requests as r

url = 'http://127.0.0.1:8000/api/year/'
token = '69175d82c8873d823a59bd713cb3c5242a4453ee'

res = r.get(
    url,
    headers={
        'Authorization':f'Token {token}'
    },
    data={
        'year':2025
    }
)
print(res.text)