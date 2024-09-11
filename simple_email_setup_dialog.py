
"""
__version__ = "$Revision: 37 $"
__date__ = "$Date: 2005/12/20 21:51:50 $"
"""

import os,sys
from PythonCard import model,dialog
from PythonCard.components import button,image,staticbox,statictext,textarea,textfield,combobox,checkbox,passwordfield,staticline
import editcoverletter
import gregutils
#curdir=os.path.dirname(sys.argv[0])
curdir=gregutils.getAppPrefix()
sys.path.insert(0,curdir) #read usersettings.py from main dir, not library
from usersettings import *

class MyDialog(model.CustomDialog):
    def __init__(self, parent, txt=''):
        model.CustomDialog.__init__(self, parent)        
        self.components.txt_ResumeName.text = resume_name
        self.components.txt_YourEmailAddress.text = From
        self.components.txt_OutgoingMailServer.text = smtpserver
        self.components.txt_UserName.text = smtpuser
        self.components.txt_pwd_Password.text = smtppass
        if  bcc_addr:
            self.components.chk_BCC_me.checked=True
        else:
            self.components.chk_BCC_me.checked=False
        if  avoid_sending_multiple_emails_to_same_addr:
            self.components.chk_AvoidSameAddress.checked=True
        else:
            self.components.chk_AvoidSameAddress.checked=False
            
    def on_btn_Advanced_mouseClick(self,event):
        """Edit Settings"""
        filepath='usersettings.py'
        settingsfile=file(filepath,'r')
        text=settingsfile.read()
        settingsfile.close()
        result = editcoverletter.myDialog(self,text,filepath,True)
        if event:event.skip()
        
    def on_btn_TestAccountSettings_mouseClick(self,event):
        """ """
        result = dialog.alertDialog(self,
        """Not yet implemented."""
        ,'Missing')
        
#def myDialog(parent, txt):
def myDialog(parent):
    dlg = MyDialog(parent)
    result = dlg.showModal()
    if result.accepted:
        # stick your results into the result dictionary here
        # example from samples/dialogs/minimalDialog.py
        # result.text = dlg.components.field1.text
        result.resume_name = dlg.components.txt_ResumeName.text
        result.From = dlg.components.txt_YourEmailAddress.text
        result.smtpserver = dlg.components.txt_OutgoingMailServer.text
        result.smtpuser = dlg.components.txt_UserName.text
        result.smtppass = dlg.components.txt_pwd_Password.text
        if dlg.components.chk_BCC_me.checked:     
            result.bcc_addr = result.From
        else:
            result.bcc_addr = ""
        if dlg.components.chk_AvoidSameAddress.checked:
            result.avoid_sending_multiple_emails_to_same_addr = "True"
        else:
            result.avoid_sending_multiple_emails_to_same_addr = "False"    
    dlg.destroy()
    return result

#----------------------------
#Utitily Functions:
def getfirstsafely(alist):
    if len(alist)>0:return alist[0]
    else: return None
def find(StringToFind,ListToLookIn):
    """find index of first list member to contain this string"""
    for member in ListToLookIn:
        if member.upper().strip().find(StringToFind.upper().strip())>-1:
            return ListToLookIn.index(member)
    return -1