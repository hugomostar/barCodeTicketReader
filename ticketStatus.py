import requests
import json
import _mssql
from config import *

class ticketStatus():

    def checkTicketNumber(ticketNumber):
        if (config['Default']['mode'] == "express"):
            result = ticketStatus.checkTicketNumberExpressJS(ticketNumber)
        if (config['Default']['mode'] == "sql"):
            result = ticketStatus.checkTicketNumberSql(ticketNumber)
        return result

    def checkTicketNumberExpressJS(ticketNumber):

        r = requests.get(config['ExpressJS']['getRequest']+ticketNumber)
        data = json.loads(r.text)
        print(data)
        res = data['response']

        return res

    def checkTicketNumberSql(ticketNumber):

        conn = _mssql.connect(server=config['SQL']['server'], user=config['SQL']['username'],  \
                          password=config['SQL']['password'], database='eGate15Sql')
        sqlcmd = """
            DECLARE
                @res varchar,
                @ticketNumber varchar(13) = %s
            EXEC
                [dbo].[sp_setTicketNumberToValidForExit]
                @res = @res OUTPUT,
                @ticketNumber = @ticketNumber
            SELECT @res
            """

        res = conn.execute_scalar(sqlcmd, ticketNumber)
        return res