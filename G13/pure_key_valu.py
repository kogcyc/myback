import json

def push(d,fn):
	with open(fn,'w') as fp:
		fp.write(json.dumps(d))

def pull(fn):
	with open(fn,'r') as fp:
		return json.loads(fp.read())

