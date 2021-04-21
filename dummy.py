import requests
r = requests.get('https://hackathon.brigosha.com', auth=('admin@brigosha.com', '1234'))
print( r.status_code)
print (r.headers['content-type'])