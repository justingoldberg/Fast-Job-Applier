"""
Setup Script
--------------------------------------------
__version__ = "$Revision: 37 $"
__date__ = "$Date: 2005/12/20 21:51:50 $"
__modified__= $"Modified: Modified $"
"""
from distutils.core import setup
import py2exe

setup( name = "Fast Job Applier",
      windows = [
        {
            "script":"Fast_Job_Applier.py",
            "icon_resources":[(1,"jobapplier.ico")]   
        }   
      ],
      options = {"py2exe": {"packages": ["encodings"]}},
      data_files = [
      ("jobapplier16.ico"),
      ("jobapplier.ico"),
      ("MSVCIRT.dll"),
      ("MSVCP60.dll"),
      ("MSVCRT.dll"),
      ("usersettings.py"),
      ("Fast_Job_Applier.rsrc.py"),
      ("editcoverletter.rsrc.py"),
      ("simple_email_setup_dialog.rsrc.py"),
      ("COPYING"),
      ("coverletters",
      [r"coverletters\Sample.agile_prg.txt",r"coverletters\Sample.GIS.txt"]),
      ("resumes",
      [r"resumes\SampleResume.doc"]),
      ("jobdescs",
      [r"jobdescs\null.txt"])]
      )
      