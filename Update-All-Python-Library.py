import os

os.system('pip freeze > req.txt')

file=open('req.txt','r')
data=file.readlines()

for i in data:
	libName=i.replace('\n','')
	try:
		os.system(f'pip install --upgrade {libName}')
	except:
		pass