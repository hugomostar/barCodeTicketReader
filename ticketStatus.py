import requests
import json
class ticketStatus():

    def checkTicketNumber(ticketNumber):

        r = requests.get('http://localhost:8080/api/tickets/'+ticketNumber)
        data = json.loads(r.text)
        res = data['response']

        return res