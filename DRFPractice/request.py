import requests
import config

#print(config.users())
url=config.users()
r=requests.get(url)
#print(r) #<Response [200]>
#print(r.text,f'\n',r.json(),f'\n',r.content)

name=input('enter name:')
email=input('mail:')
status=input('status:')
gender=input('gender:')

data=dict()
data['name']=name
data['email']=email
data['status']=status
data['gender']=gender

header=dict()
header['Authorization']='Bearer'+config.access_token()
r=requests.post(url, data=data, headers=header)

print(r.json())#return value after post