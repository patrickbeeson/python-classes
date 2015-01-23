"""
Tests to verify message creation and storage. Also performs profiling of these operations.
"""

import mysql.connector as msc
from database import login_info
from emailcreatestore import create_message
import settings
import unittest
import time

conn = msc.Connect(**login_info)
curs = conn.cursor()

#TBLDEF = """\
#CREATE TABLE message(
#    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
#    msgMessageID VARCHAR(128),
#    msgDate DATETIME,
#    msgSenderName VARCHAR(128),
#    msgSenderAddress VARCHAR(128),
#    msgText LONGTEXT
#    )"""

class TestEmail(unittest.TestCase):

#    def setUp(self):
#        """
#        Creates new message table if it doesn't exist.
#        """
#        curs.execute("DROP TABLE IF EXISTS message")
#        conn.commit()
#        curs.execute(TBLDEF)
#        conn.commit()

    def test_create(self):
        """
        Test message creation logic
        """
        create_message(settings.RECIPIENTS, settings.STARTTIME, settings.DAYCOUNT)
        expectedCount = len(settings.RECIPIENTS) * settings.DAYCOUNT
        curs.execute("SELECT COUNT(*) FROM message")
        observed = curs.fetchone()[0]
        self.assertEqual(expectedCount, observed, "Unexpected number of messages created")

    def test_profile(self):
        """
        Profiles email creation and storage as a function of day count
        """
        daycounts = (1, 10, 50, 100, 500)
        for days in daycounts:
            start = time.time()
            create_message(settings.RECIPIENTS, settings.STARTTIME, days)
            end = time.time()
            interval = end - start
            print('Days:{0}, Time:{1} '.format(days, round(interval,2)))

#    def tearDown(self):
#        pass

if __name__ == '__main__':
    unittest.main()
