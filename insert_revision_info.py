"""
Greg Pinero (gregpinero@gmail.com)

A simple script to get the latest revision info from your working copy
and insert it into each of your files (except this one)

Usage:
Just write $Name: $ patterns shown below anywhere in each file and they will 
be filled in with the correct revision information when you run this script.
--------------------------------------------
$Revision: $
$Date: $
$Modified: $
"""

import os,sys
import re

#-----------------------------------------------------------------------------
#   USER SETTINGS:

#The location of SubWCRev.exe
#You can download it at http://tortoisesvn.tigris.org/download.html
SubWCRev_Path=r"C:\Program Files\TortoiseSVN\bin\SubWCRev.exe" 
#What types of files you want this script to run on by file extension
filetypes2lookat=['.py','.txt','.bat','.cmd','.in','.iss']

#-----------------------------------------------------------------------------

#Call SubWCRev.exe which will create a Python source file called
# revisioninfo.py
print os.system('"%s" . revisioninfo.in revisioninfo.py' % SubWCRev_Path)
#Import revisioninfo.py to access the new revision values just updated by
# SubWCRev.exe
from revisioninfo import * #simply holds revision variables

#make regexes:
#What to look for and replace in each file
reRevision=re.compile(r'\$Revision:[^\$\+]*\$') #'+' lets us ignore lines below
reDate=re.compile(r'\$Date:[^\$\+]*\$')
reModified=re.compile(r'\$Modified:[^\$\+]*\$')
 
#main section of script:
#Below we read in all the files in this script's own directory
# and then filter them to only include file extensions from filetypes2lookat
listfiles=[fil for fil in os.listdir(os.path.dirname(sys.argv[0])) 
            if os.path.splitext(fil)[1] in filetypes2lookat and 
            fil<>os.path.basename(sys.argv[0])]
for fil in listfiles:
    #We look at each file and replace in the new revision info.
    content=file(fil,'r').read()
    content=reRevision.sub(r'$Revision: '+WCREV+r' $',content)
    content=reDate.sub(r'$Date: '+WCDATe+r' $',content)
    content=reModified.sub(r'$Modified: '+WCMODS+r' $',content)
    file(fil,'w').write(content)
