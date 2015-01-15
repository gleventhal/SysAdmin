#!/usr/bin/python
import httplib2
import sys
import datetime 
import smtplib
import re

from secrets import *
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

header = '''
Good Day,
The following events are scheduled for today:\n\n
'''

client_id = ARG1
client_secret = ARG2

scope = 'https://www.googleapis.com/auth/calendar'

flow = OAuth2WebServerFlow(client_id, client_secret, scope)

def main():

  storage = Storage('credentials.dat')

  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run(flow, storage)

  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('calendar', 'v3', http=http)
  today = str(datetime.date.today()) + 'T00:00:00-05:00'
  tomorrow = str(datetime.date.today() + datetime.timedelta(days=1)) + 'T00:00:00-05:00'
  myCalendar = 'Your Gmail Calendar ID Here'
  try:

    request = service.events().list(calendarId = myCalendar, timeMin = today, timeMax = tomorrow)
    
   
    while request != None:
      response = request.execute() 
      Message = []
      events =  []
     
      for event in response.get('items', []):
        
        res =  repr(event.get('summary')) 
        deunicode = re.sub(r'^u\'|\'', '\'', res)
        events.append(deunicode)
       
        Message = [e for e in events if not 'None' in e]
      request = service.events().list_next(request, response)

      if not Message or Message[0] == '':
        Message.append('There are currently no events on today\'s Calendar')    

      mail = {
      'sender'    :  'Sending Address Here',
      'recipient' :  ['Recipient Address 1','Recipient Address 2'],
      'message'   :   header + "\t" + "\t".join([str(num + 1) + ". " + "***"+entry.strip("'")+"***" for num,entry in enumerate(Message)])
      }


      try:
          for r in mail['recipient']:
	      smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	      smtpObj.set_debuglevel(True)
	      smtpObj.starttls()
	      smtpObj.login(mailCreds['user'], mailCreds['pass'])
	      smtpObj.sendmail(mail['sender'], r, mail['message'])
      except Exception as e:
              print "Message failed to send!\n%s" % (e)

  except AccessTokenRefreshError:
    
   
    print ('The credentials have been revoked or expired, please re-run'
           'the application to re-authorize')

if __name__ == '__main__':
  main()
