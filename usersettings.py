#!/usr/bin/python
import re
"""
These are the settings you need to fill in.
Change them to your own settings accordingly.
--------------------------------------------
__version__ = "$Revision: 37 $"
__date__ = "$Date: 2005/12/20 21:51:50 $"
__modified__= $"Modified: Modified $"
"""
#----------------------------
#Standard User Settings:
#Send a copy of each email to yourself:
bcc_addr = ''
resume_name = 'MyResume'
#----------------------------
#Email Settings:
From = ''
smtpserver = ''
AUTHREQUIRED = 1        # if you need to use SMTP AUTH set to 1
smtpuser = ''
smtppass = ''
#----------------------------
#Advanced:
isFirstUse = True
resume_folder_path = 'resumes'
cover_letter_folder_path = 'coverletters'
job_descs_folder_path = 'jobdescs'
log_file_name = 'jobsappliedto.txt'
urlsanitization_pattern = re.compile(r'[^\w]')       #Chars to remove from url's named when saved
urlsafechar = '_'      #url safe replacement char
avoid_sending_multiple_emails_to_same_addr = True
