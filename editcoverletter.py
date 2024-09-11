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
__version__ = "$Revision: 37 $"
__date__ = "$Date: 2005/12/20 21:51:50 $"
__modified__= "$Modified: Modified $"
"""
import os
from PythonCard import model,dialog
from PythonCard.components import button,image,staticbox,statictext,textarea,textfield,combobox,checkbox

class MyDialog(model.CustomDialog):
    def __init__(self, parent, txt=''):
        model.CustomDialog.__init__(self, parent)        
        self.parent = self.GetParent()
        self.components.txt_coverletter.text = txt
    def on_chk_saveas_mouseClick(self,event):
        self.components.txt_savetoname.enabled=not self.components.txt_savetoname.enabled
        event.skip()
        
def myDialog(parent, txt, filepath, generic=False,windowcaption='Edit Cover Letter'):
    dlg = MyDialog(parent, txt)
    if len(filepath)<2:dlg.components.chk_save.enabled=False
    if generic:
        #Hide extraneous stuff
        dlg.title="Settings"
        dlg.components["chk_saveas"].visible=False
        dlg.components["chk_save"].visible=False
        dlg.components["txt_savetoname"].visible=False  
    #set window caption
    result = dlg.showModal()
    if result.accepted:
        # stick your results into the result dictionary here
        # example from samples/dialogs/minimalDialog.py
        result.text = dlg.components.txt_coverletter.text
        if dlg.components.chk_save.checked==True or generic==True:        
            os.remove(filepath) #remove old file        
            saveto=file(filepath,'w') #make new file of the same name         
            saveto.write(result.text) #put in new text        
            saveto.close() #close file
            if generic:
                result = dialog.alertDialog(dlg, 'New settings will take effect after you restart the program', 'Settings Saved')
        if dlg.components.chk_saveas.checked==True:
            #make new filename:
            dircovletter=os.path.dirname(filepath)
            newfilepath=os.path.join(dircovletter,dlg.components.txt_savetoname.text)+'.txt'
            newfile=file(newfilepath,'w') #make new file of the same name   
            newfile.write(result.text) #put in new text        
            newfile.close() #close file
    dlg.destroy()
    return result
