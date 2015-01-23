"""
Function to return an email message to send.
"""
import os
import mimetypes
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def create_message(recipient, message, *args):
    """
    Function to create email for send
    based on arguments for recipient, message and attachments (optional)
    """
    msg = MIMEMultipart()
    msg['date'] = formatdate(localtime=True)
    msg['to'] = recipient
    msg['from'] = 'noreply@patrickbeeson.com'
    msg.attach(MIMEText(message))
    if len(args):
        for arg in args:
            ctype, encoding = mimetypes.guess_type(arg)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            part = MIMEBase(maintype, subtype)
            with open(arg, 'rb') as file:
                part.set_payload(file.read())
                encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(arg))
            msg.attach(part)
    
    return msg

if __name__ == "__main__":
    attachment_1 = os.path.join(os.getcwd(), 'emailtest.txt')
    attachment_2 = os.path.join(os.getcwd(), 'python-logo.png')
    output = create_message('patrickbeeson@gmail.com', 'This is my message', attachment_1, attachment_2)
    print(output.as_string())