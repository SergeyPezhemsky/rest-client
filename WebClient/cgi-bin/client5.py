import requests
import json


def DoRequest(method, cmd="", data=""):
	try:
		url = 'http://localhost:8080/cgi-bin/WEBClient.py'
		header = {"Content-type": 'text/html'}
		res = method(url+cmd, headers=header, data=json.dumps(data))
		if res.status_code == 200:
			return json.loads(res.content)
	except Exception as ex:
		print(ex)


def GetList(id):
	q = '?console=1&ClientID=' + str(id)
	res = DoRequest(requests.get, q)
	return res

def SendMsg(clientId, message, id):
	q = '?' + 'id='+ str(id) + '&message='+ message + '&console=' + '1' + '&ClientID=' + str(clientId)
	res = DoRequest(requests.get, q)
