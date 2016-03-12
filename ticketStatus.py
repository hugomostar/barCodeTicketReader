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

        return data

    def checkTicketNumberSql(ticketNumber):

        conn = _mssql.connect(server=config['SQL']['server'], user=config['SQL']['username'],  \
                          password=config['SQL']['password'], database='eGate15Sql')
        sqlcmd = """
            DECLARE
                @res varchar(150),
                @ticketNumber varchar(13) = %s
            EXEC
                [dbo].[sp_setTicketNumberToValidForExit]
                @res = @res OUTPUT,
                @ticketNumber = @ticketNumber
            SELECT @res
            """

        res = conn.execute_scalar(sqlcmd, ticketNumber)
        data = json.loads(res)

        return data