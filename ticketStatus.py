import _mssql

class ticketStatus():

    def checkTicketNumber(ticketNumber):
        conn = _mssql.connect(server='DESKTOP-OLVGNHU\SQLEXPRESS', user='sa', password='lozinka', \
                          database='eGate15Sql')
        sqlcmd = """
            DECLARE
                @res varchar(5),
                @ticketNumber varchar(13) = %s

            EXEC
                [dbo].[sp_setTicketNumberToValidForExit]
                @res = @res OUTPUT,
                @ticketNumber = @ticketNumber
            SELECT @res
            """

        res = conn.execute_scalar(sqlcmd, ticketNumber)
        return res