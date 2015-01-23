import unittest
from email_send import create_message
import email
import tempfile
import os

class EmailTest(unittest.TestCase):
    
    def setUp(self):
        # Create arguments
        self.message = 'Hello, world!'
        self.recipient = 'patrickbeeson@gmail.com'
        # Create attachments
        self.attachment_1 = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        self.attachment_1.close()
        self.attachment_2 = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        self.attachment_2.close()

    def test_create_message_output(self):
        output = create_message(self.recipient, self.message, self.attachment_1.name, self.attachment_2.name)
        expected = 'patrickbeeson@gmail.com'
        self.assertEqual(output['to'], expected)

    def teardown(self):
        os.remove(self.attachment_1)
        os.remove(self.attachment_2)

if __name__ == "__main__":
    unittest.main()