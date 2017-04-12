from jira import JIRA
import json
import requests
import xml

url='https://dttteams.deloitte.com/sites/ddigital/DDUSI/knowonthego/_api/web/lists/getbytitle("Team Details")/items?$select=TeamMembers/Title,TeamMembers/SipAddress,TeamMembers/JobTitle&$expand=TeamMembers&$filter=USIProjectName_x003a_ID%20eq%2014'
head = {'Content-type':'application/json',
             'Accept':'application/json'}
# payload = {'name':'Saravanan',
#                'Designation':'Architect',
#                'Orgnization':'Cisco Systems'}

# payld = json.dumps(payload)
ret = requests.post(url,head)
ret.status_code
