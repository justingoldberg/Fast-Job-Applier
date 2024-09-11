"""
Created by Greg Pinero 2005 (gregpinero@gmail.com)


This file is part of Fast Job Applier.

Fast Job Applier is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Fast Job Applier is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Fast Job Applier; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

--------------------------------------------
simple_email.py
Greg Pinero 1/3/2005
Your basic email sending functionality, messages and attachments.
--------------------------------------------
__version__ = "$Revision: 37 $"
__date__ = "$Date: 2005/12/20 21:51:50 $"
__modified__= $"Modified: Modified $"
"""
import os
import sys
import smtplib
import mimetypes
from email.Encoders import encode_base64
from email.MIMEAudio import MIMEAudio
from email.MIMEBase import MIMEBase
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
curdir=os.path.dirname(sys.argv[0])
sys.path.insert(0,curdir) #read usersettings.py from main dir, not libraryfrom usersettings import *
from usersettings import *

def __getAttachment(path, filename):
    """ """
    ctype, encoding = mimetypes.guess_type(path)  #mimetypes guesses the type of file and stores it in ctype
    if ctype is None or encoding is not None:     # example: ctype can equal "application/pdf"
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)    #We do a split on "/" to store "application" in maintype and "pdf" in subtype
    fp = open(path, 'rb')           #open the file
    if maintype == 'text':
        attach = MIMEText(fp.read(),_subtype=subtype) #check for maintype value and encode and return according to
    elif maintype == 'message':                       #the type of file.
        attach = email.message_from_file(fp)
    elif maintype == 'image':
        attach = MIMEImage(fp.read(),_subtype=subtype)
    elif maintype == 'audio':
        attach = MIMEAudio(fp.read(),_subtype=subtype)
    else:
        #print maintype, subtype  #if it does not equal any of the above we print to screen and encode and return
        attach = MIMEBase(maintype, subtype) #the encoded value
        attach.set_payload(fp.read())
        encode_base64(attach)
    fp.close
    attach.add_header('Content-Disposition', 'attachment',filename=filename)
    return attach

def just_send_an_email(ToAddr,Subject,Body,AttachmentFilePath=None,AttachmentName="Attachment1",BccAddr=None):
    """
    Send emails with normal parameters so I can just shoot off emails from
    another script.
    """
    #Here we set up our email
    To = ToAddr
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = Subject
    body = MIMEText(Body) #Here is the body
    msg.attach(body)
    if AttachmentFilePath:
        ext=os.path.splitext(AttachmentFilePath)[1]
        path=AttachmentFilePath
        attach = __getAttachment(path, AttachmentName+ext) #We call our getAttachment() function here
        msg.attach(attach)  #We create our message both attachment and the body
    #send to toaddr
    send_engine(From,To,msg)
    #send to bcc
    if BccAddr:send_engine(From,BccAddr,msg)

def send_engine(From,To,MIMEMultipart_Msg):
    #Send the email
    sent=False
    iter=1
    while sent==False:
        try:
            smtpresult = session.sendmail(From, To, MIMEMultipart_Msg.as_string())
        except:
            smtpresult="error"
        if smtpresult: #mail had error
            if iter>3:return False
            iter+=1
            reset_session()
        else:
            return True

def reset_session():
    print 'resetting email session'
    global session
    try:session.quit()
    except:pass
    try:session.close()
    except:pass
    session = smtplib.SMTP(host=smtpserver)
    #session.set_debuglevel(1)
    #below is neccesary for GMAIL, but doesn't seem to hurt otherwise
    session.ehlo()
    session.starttls()
    session.ehlo()
    if AUTHREQUIRED:
        session.login(smtpuser,smtppass)

#Set up smtp server
#session = smtplib.SMTP(smtpserver)
#if AUTHREQUIRED:
#    session.login(smtpuser,smtppass)

#----------------------------
#testing:
if __name__ == '__main__':
    #try sending 3 emails
    print 'start test procedure'
    for i in range(2):
        #just_send_an_email('testperson@comcast.net','subject:test'+str(i),'body:test1',
        #'simple_email.py','attach:test1','testperson@comcast.net')
        just_send_an_email('testperson@comcast.net','subject:test'+str(i),'body:test1')

    pause=raw_input('press enter to exit')
    session.quit() #build into "on reload" dealy?