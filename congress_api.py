"""
URL Parameters

Parameter	Description
congress	105-115
chamber	house or senate
type	introduced, updated, passed or major
"""

import json
import requests
import ApiKey as AK

def proAPI():
	key = AK.key
	#url = "https://api.propublica.org/congress/v1/115/senate/members.json"
	# get recent bills
	url = "https://api.propublica.org/congress/v1/115/house/bills/introduced.json"
	r = requests.get(url,headers={"X-API-KEY":key})
	return r.content
	#return r.content

def print_data(data):
	r = json.loads(data)
	bills = r['results'][0]['bills']
	for i in range(len(bills)):
		print bills[i]['number']
		print bills[i]['introduced_date']
		print bills[i]['title']
		print bills[i]['latest_major_action']
		print bills[i]['latest_major_action_date']
		print ""

if __name__ == '__main__':
	data = proAPI()
	print_data(data)