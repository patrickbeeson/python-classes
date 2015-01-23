"""
Program to create a message that's stored in a database.
"""
import settings
from database import login_info
import mysql.connector as msc
from email import message_from_string
from email.utils import make_msgid
from datetime import timedelta

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE IF NOT EXISTS message(
    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
    msgMessageID VARCHAR(128),
    msgDate DATETIME,
    msgSenderName VARCHAR(128),
    msgSenderAddress VARCHAR(128),
    msgText LONGTEXT
    )"""

def create_message(recipients, startdate, daycount):
    """
    Creates an email message using data from settings.
    """
    curs.execute(TBLDEF)
    conn.commit()
    # Loop through our days
    for day in range(daycount):
        d = startdate + timedelta(days=day)
        # Create our message
        for name, recipient in recipients:
            msg = message_from_string(name + ', \n' + 'Moment of Zen')
            msg['To'] = recipient
            msg['Subject'] = 'Moment of zen for ' + str(d.date())
            msg['Date'] = d.strftime('%d %b %Y %H:%M:%S - 0600')
            msg['From'] = settings.SENDER
            msg['Message-ID'] = make_msgid()
            # Store our messages in the database
            curs.execute("INSERT INTO message (msgMessageID, msgDate, msgSenderName, msgSenderAddress, msgText) VALUES (%s, %s, %s, %s, %s)",
                         (msg['Message-ID'], msg['Date'], name, msg['To'], msg.as_string()))
            conn.commit()
