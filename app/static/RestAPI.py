# Import packages
from urllib.request import urlopen, Request
from requests.auth import HTTPBasicAuth
import requests

class restClient(object):
 def getCurrentUserIssues(self, maxResults):

  # Specify the url
   url = "https://dttteams.deloitte.com/sites/ddigital/DDUSI/knowonthego/_api/web/lists/getbytitle('Team%20Details')/items?$select=TeamMembers/Title,TeamMembers/SipAddress,TeamMembers/JobTitle&$expand=TeamMembers&$filter=USIProjectName_x003a_ID%20eq%2014"

   # This packages the request
   # request = Request(url,)

   # Sends the request and catches the response: response
   requests.get(url, auth=('usiddsharepointSVC', 'D3l01TT3!'))

   response = urlopen(requests)

   # Extract the response: html
   html = response.read()

   # Print the html
   print(html)

   return html
# Be polite and close the response!
