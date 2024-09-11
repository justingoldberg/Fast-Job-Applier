#!/usr/bin/python
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

"""
__version__ = "$Revision: 37 $"
__date__ = "$Date: 2005/12/20 21:51:50 $"
__modified__= "$Modified: Modified $"

import os,sys,time,urllib2,urlparse
from PythonCard import model,dialog,timer,clipboard
from PythonCard.components import button,image,staticbox,statictext,textarea,textfield,combobox,checkbox,passwordfield,staticline
import wx
import gregutils
import editcoverletter
import simple_email_setup_dialog
import simple_email
#curdir=os.path.dirname(sys.argv[0])
curdir=gregutils.getAppPrefix()
sys.path.insert(0,curdir) #read usersettings.py from main dir, not library
#file('maincurdir.txt','w').write(curdir)
from usersettings import *

class MyBackground(model.Background):

    def on_initialize(self, event):
        self.numrows=10
        ypos=40
        self.rowTarget=0
        self.colTarget=0
        self.lstresumes=[fil for fil in os.listdir(os.path.join(curdir,resume_folder_path)) if 
            os.path.isfile(os.path.join(curdir,resume_folder_path,fil))] #get list of resumes
        self.lstcoverletters=[fil for fil in os.listdir(os.path.join(curdir,cover_letter_folder_path)) if 
            os.path.isfile(os.path.join(curdir,cover_letter_folder_path,fil))] #get list of cover_letters
        self.editedcoverletters={}
        self.lastText = clipboard.getClipboard()
        self.timer = timer.Timer(self.components.Start, -1)
        self.do_StartOrStop(self.menuBar.getChecked('menuOptionsAutoPasteMode'))
        #Set up fields:
        for i in range(self.numrows):
            #make a row
            num=str(i)
            self.components['txt_position'+num]={'text':'','type':'TextField','name':'txt_position'+num,'position':(0,ypos),'size':(120,21),}
            self.components['txt_emailaddr'+num]={'text':'','type':'TextField','name':'txt_emailaddr'+num,'position':(120,ypos),'size':(120,21),}
            self.components['txt_employername'+num]={'text':'','type':'TextField','name':'txt_employername'+num,'position':(240,ypos),'size':(-1,21),'text':'Sir or Madam',}
            self.components['txt_url'+num]={'text':'','type':'TextField','name':'txt_url'+num,'position':(340,ypos),'size':(140,21),}
            self.components['cmbbox_coverletter'+num]={'type':'ComboBox','name':'cmbbox_coverletter'+num,'position':(480,ypos),'size':(130,20),'items':self.lstcoverletters,'stringSelection':getfirstsafely(self.lstcoverletters),}
            self.components['cmbbox_resume'+num]={'type':'ComboBox','name':'cmbbox_resume'+num,'position':(610,ypos),'size':(130,20),'items':self.lstresumes,'stringSelection':getfirstsafely(self.lstresumes),}
            self.components['btn_editcoverletter'+num]={'type':'Button','name':'btn_editcoverletter'+num,'position':(740,ypos),'size':(90,20),'label':'EditCoverLetter',}
            ypos+=20 + 4
        if isFirstUse:
            result = dialog.alertDialog(self,
"""You will need to set up a couple things.
Simply put your information into this screen that comes up in a second."""
            ,'Getting Started')
            self.on_menuOptionsSettings_select()

    def refresh(self):
        #>refresh email server??
        self.numrows=10
        self.rowTarget=0
        self.colTarget=0
        self.lstresumes=[fil for fil in os.listdir(os.path.join(curdir,resume_folder_path)) if 
            os.path.isfile(os.path.join(curdir,resume_folder_path,fil))] #get list of resumes
        self.lstcoverletters=[fil for fil in os.listdir(os.path.join(curdir,cover_letter_folder_path)) if 
            os.path.isfile(os.path.join(curdir,cover_letter_folder_path,fil))] #get list of cover_letters
        self.editedcoverletters={}
        for i in range(self.numrows):
            #make a row
            num=str(i)
            self.components['cmbbox_resume'+num].items=self.lstresumes
            self.components['cmbbox_coverletter'+num].items=self.lstcoverletters
            self.components['cmbbox_resume'+num].stringSelection=getfirstsafely(self.lstresumes)
            self.components['cmbbox_coverletter'+num].stringSelection=getfirstsafely(self.lstcoverletters)
            self.components['cmbbox_coverletter'+num].backgroundColor=(255, 255, 255)
            self.components['txt_url'+num].text=''
            self.components['txt_employername'+num].text='Sir or Madam'
            self.components['txt_emailaddr'+num].text=''
            self.components['txt_position'+num].text=''

    def on_btn_batchapply_mouseClick(self,event):
        dowait = wx.wx.BusyCursor() #>make hourglass
        self.statusBar.text = "Sending Emails.  Please stand by."        
        lstemailstosend=[]
        fields=self.components #just a nickname for here
        #Get info from all filled in rows:
        for i in range(self.numrows):
            num=str(i)
            curraddr=fields['txt_emailaddr'+num].text
            if ('@' in curraddr) and (r'.' in curraddr):#crude valid-email check
                email={}
                #read in info:
                email['resume']=os.path.join(resume_folder_path,fields['cmbbox_resume'+num].text)
                email['url']=fields['txt_url'+num].text
                email['name']=fields['txt_employername'+num].text
                email['toaddr']=fields['txt_emailaddr'+num].text
                email['position']=fields['txt_position'+num].text
                
                #url handling / get file:
                try:
                    urlfile=urllib2.urlopen(email['url'])
                    jobdescription=urlfile.read()
                    urlfile.close()
                except Exception, inst:
                    jobdescription="unopenable url"
                    print "unopenable url:" + email['url']
                    print inst # __str__ allows args to printed directly
                #make safe file name:
                if len(email['url'])<77:urlstring=email['url']
                else:
                    try:
                        urlstring=urlparse.urlparse(email['url'])[1]
                    except Exception, inst:
                        urlstring=email['url']
                        print "unparsable url:" + email['url']
                        print inst # __str__ allows args to printed directly
                savepathtemp=email['position']+urlstring
                savepath=urlsanitization_pattern.sub(urlsafechar,savepathtemp)+'.html'
                #save webpage:
                savedurlpath=os.path.join(curdir,job_descs_folder_path,savepath)
                savedurl=file(savedurlpath,'w')
                savedurl.write(jobdescription)
                email['savedurl']=savedurlpath
                #make customized coverletter:
                if self.editedcoverletters.has_key(num):#was cover letter edited?
                    rawtext=self.editedcoverletters[num]
                else:
                    rawtext=file(os.path.join(cover_letter_folder_path,fields['cmbbox_coverletter'+num].stringSelection)).read()
                rawtext=rawtext.replace("<url>",urlstring)
                rawtext=rawtext.replace("<name>",email['name'])
                rawtext=rawtext.replace("<position>",email['position'])
                email['coverletter']=rawtext[:]
                lstemailstosend.append(email)
        #send all emails:
        print 'sending emails, please stand by'
        for email in lstemailstosend:
            print 'sending message \"' + email['position'] + '\"'
            #--Check if already sent to address--#
            if (
            dct_prevemailed.has_key(email['toaddr']) and
            not dialog.messageDialog(self,'You have already sent an email to '
            + email['toaddr'] + '\nPress OK to send anyway or press Cancel to skip.',
            'Caution').accepted
            ):
                print 'skipping'
            else:
                simple_email.just_send_an_email(email['toaddr'],
                email['position'],email['coverletter'],email['resume'],
                resume_name,bcc_addr)
                #Write to log file
                loggingcoverletter=email['coverletter'].replace('\n','<p>')
                loggingcoverletter=loggingcoverletter.replace('\t','    ')
                #'datetime\turl\tposition\temployername\temail\tcoverletter\tresume(filename)\tjobdescription(filename)\n'
                logfile.write(time.ctime()+'\t'+email['url']+'\t'+email['position']+'\t'+email['name']+'\t'+email['toaddr']+'\t'+loggingcoverletter+'\t'+email['resume']+'\t'+email['savedurl']+'\n')
        print 'Done sending messages'
        #Refresh things as needed for next batch.
        dowait = None #>put mouse back
        self.statusBar.text = ""    
        result = dialog.alertDialog(self,"""Emails sent""",'Status')
        self.refresh()
        event.skip()

    def on_close(self, event):
        event.skip()

    def on_size(self, event):
        event.skip()
        
    def on_btn_mouseClick(self,event):
        event.skip()
    
    #Redirect buttons to editcoverletter function:
    def on_btn_editcoverletter0_mouseClick(self,event):self.editcoverletter(0)
    def on_btn_editcoverletter1_mouseClick(self,event):self.editcoverletter(1)
    def on_btn_editcoverletter2_mouseClick(self,event):self.editcoverletter(2)
    def on_btn_editcoverletter3_mouseClick(self,event):self.editcoverletter(3)
    def on_btn_editcoverletter4_mouseClick(self,event):self.editcoverletter(4)
    def on_btn_editcoverletter5_mouseClick(self,event):self.editcoverletter(5)
    def on_btn_editcoverletter6_mouseClick(self,event):self.editcoverletter(6)
    def on_btn_editcoverletter7_mouseClick(self,event):self.editcoverletter(7)
    def on_btn_editcoverletter8_mouseClick(self,event):self.editcoverletter(8)
    def on_btn_editcoverletter9_mouseClick(self,event):self.editcoverletter(9)
    def on_btn_editcoverletter10_mouseClick(self,event):self.editcoverletter(10)
    def on_btn_editcoverletter11_mouseClick(self,event):self.editcoverletter(11)

    def editcoverletter(self,num):
        num=str(num)
        filepath=""
        #find selected cover letter:
        if self.editedcoverletters.has_key(num):
            text=self.editedcoverletters[num]
        else:            
            filepath=os.path.join(cover_letter_folder_path,self.components['cmbbox_coverletter'+num].stringSelection)
            coverletterfile=file(filepath)
            text=coverletterfile.read()
            coverletterfile.close()
            #except:
            #    text="No cover letter was selected or file had problems, cancel and select anew, or write your own here and now."
        #self.editwindow = model.childWindow(self, editcoverletter.myDialog)
        result = editcoverletter.myDialog(self,text,filepath)
        if result.accepted:
            self.editedcoverletters[num]=result.text #save/track changes
            #change color of button
            self.components['cmbbox_coverletter'+num].backgroundColor=(255, 0, 128)#reddish

    def getNextAutoPasteTarget(self,lastWidgetName=None):
        acceptableTargets=['txt_position','txt_emailaddr','txt_employername','txt_url']
        if lastWidgetName:
            strRowTarget=''.join([char for char in lastWidgetName[-3:]
            if char.isdigit()])#find all numbers at end of string
            self.rowTarget=int(strRowTarget)
            self.colTarget=acceptableTargets.index(lastWidgetName.replace(strRowTarget,""))
        retref=self.components[acceptableTargets[self.colTarget]+str(self.rowTarget)]
        self.colTarget+=1
        if self.colTarget>=len(acceptableTargets):
            self.colTarget=0
            self.rowTarget+=1
            if self.rowTarget>=self.numrows:
                self.rowTarget=0
        return retref   

    def do_StartOrStop(self, start):
        #self.components.Start.enabled = not start
        #self.components.Stop.enabled = start
        if start:
            self.timer.start(100)
        else:
            self.timer.stop()
            
    def on_Start_timer(self, event):
        #self.childWindow.Raise() #<breaks without children
        #self.Raise() #<doesn't work with Firefox
        #lastfocus=self.findFocus() #no focus when window isn't on top :-(
        newText = str(clipboard.getClipboard())
        if newText <> self.lastText:
            self.lastText = newText
            #print newText
            #if lastfocus:
            #    pasteTarget=lastfocus
            #else:
            pasteTarget=self.getNextAutoPasteTarget()
            pasteTarget.text=newText #todo: trim, sanitize
            #self.getNextAutoPasteTarget() # move focus to next field
           
    def on_mnuExit_select(self, event):
        self.close()

    def on_menuAbout_select(self,event):
        txtAbout="""
        Fast Job Applier
        Copyright Blended Technologies LLC 2005
        
        A program designed to help automate the job application process.
        
        Visit http://www.blendedtechnologies.com/projects/job-applier-mark-ii/
        for help and feature requests.
        
        Version 0.5 (%s)
        Last modified: %s
        """ % (__version__,__date__)
        dialog.scrolledMessageDialog(self, txtAbout, 'About')
        
    def on_menuOptionsTestingMode_select(self, event):
        for i in range(self.numrows):
            num=str(i)
            self.components['txt_emailaddr'+num].text=simple_email.From
        event.skip()
        
    def on_menuOptionsAutoPasteMode_select(self, event):
        print 'menuOptionsAutoPasteMode'
        print str(self.menuBar.getChecked('menuOptionsAutoPasteMode'))
        self.do_StartOrStop(self.menuBar.getChecked('menuOptionsAutoPasteMode'))
        event.skip()
        
    def on_menuOptionsSettings_select(self, event=None):
        """Edit Settings"""
        result=simple_email_setup_dialog.myDialog(self)
        if result.accepted:
            usersettings=file('usersettings.py','r').readlines()
            #save stuff to usersettings.py
            usersettings[find("bcc_addr = ",usersettings)]="bcc_addr = '%s'\n" % result.bcc_addr
            usersettings[find("resume_name = ",usersettings)]="resume_name = '%s'\n" % result.resume_name
            usersettings[find("From = ",usersettings)]="From = '%s'\n" % result.From
            usersettings[find("smtpserver = ",usersettings)]="smtpserver = '%s'\n" % result.smtpserver
            usersettings[find("smtpuser = ",usersettings)]="smtpuser = '%s'\n" % result.smtpuser
            usersettings[find("smtppass = ",usersettings)]="smtppass = '%s'\n" % result.smtppass
            usersettings[find("avoid_sending_multiple_emails_to_same_addr = ",usersettings)]="avoid_sending_multiple_emails_to_same_addr = " + result.avoid_sending_multiple_emails_to_same_addr + '\n'
            usersettings[find("isFirstUse =",usersettings)]="isFirstUse = %s\n" % "False"
            file('usersettings.py','w').write(''.join(usersettings))
            result = dialog.alertDialog(self,
            """You will need to restart this application for the changes to take effect."""
                ,'Restart Application')
        
    def on_menuAddResumesHowTo_select(self,event):
        """how to add resumes"""
        print 'on_menuAddResumes_select'
        resumefolder=os.path.abspath(resume_folder_path)
        print 'resumefolder:',resumefolder
        result = dialog.alertDialog(self,'To add a resume simply put the file in the folder %s.' % resumefolder,'Adding Resumes')
        event.skip()
        
class Job:
    """class to orgainze job info read from log file"""
    def __init__(self,str_linefromlogfile):
        varlist=str_linefromlogfile.split('\t')
        self.time=varlist[0]
        self.url=varlist[1]
        self.position=varlist[2]
        self.name=varlist[3]
        self.toaddr=varlist[4]
        self.coverletter=varlist[5]
        self.resume=varlist[6]
        self.savedwebsite=varlist[7]

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

#Main Program:
if __name__ == '__main__':
    oldjobs=[] #jobs applied to from previous sessions
    dct_prevemailed={} #toaddr's from previous and current sessions
    #handle logging:
    if gregutils.file_exists(os.path.join(curdir,log_file_name)):
        if avoid_sending_multiple_emails_to_same_addr:
            existinglogfile=file(os.path.join(curdir,log_file_name),'r')
            #parse logfile into objects #>wasteful method w two loops but is just tempory
            for line in existinglogfile.readlines()[1:]:#[1:] to ignore first line with labels
                if len(line)>4: #kinda big num to ignore blank lines
                    ajob=Job(line)
                    oldjobs.append(ajob)
            existinglogfile.close()
            for job in oldjobs:
                dct_prevemailed[job.toaddr]=True
            #print dct_prevemailed.items()
            #print oldjobs
        #print 'file exists somehow?'
        logfile=file(os.path.join(curdir,log_file_name),'a') #open for appending
    else:
        #print 'file doesnt exist yet?'
        logfile=file(os.path.join(curdir,log_file_name),'w') #open for writing
        logfile.write('datetime\turl\tposition\temployername\temail\tcoverletter\tresume(filename)\tjobdescription(filename)\n')
    #start GUI:
    app = model.Application(MyBackground)
    app.MainLoop()
