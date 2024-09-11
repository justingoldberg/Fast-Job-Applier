{'type':'CustomDialog',
    'name':'Template',
    'title':'E-mail Account Setup',
    'position':(26, 86),
    'size':(580, 519),
    'components': [

{'type':'Button', 
    'id':5100, 
    'name':'btnOK', 
    'position':(139, 440), 
    'default':1, 
    'label':'Save Settings', 
    },

{'type':'Button', 
    'id':5101, 
    'name':'btnCancel', 
    'position':(241, 440), 
    'label':'Cancel', 
    },

{'type':'StaticText', 
    'name':'lbl_ResumeName', 
    'position':(311, 371), 
    'size':(143, 31), 
    'text':'What to call your resume when attached to an email: ', 
    },

{'type':'TextField', 
    'name':'txt_ResumeName', 
    'position':(455, 380), 
    'text':'MyResume', 
    },

{'type':'StaticText', 
    'name':'lblOtherSettings', 
    'position':(25, 354), 
    'font':{'style': 'bold', 'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 10}, 
    'text':'Other Settings', 
    },

{'type':'CheckBox', 
    'name':'chk_AvoidSameAddress', 
    'position':(25, 406), 
    'checked':True, 
    'label':'Avoid sending multiple emails to the same address', 
    },

{'type':'CheckBox', 
    'name':'chk_BCC_me', 
    'position':(25, 379), 
    'checked':True, 
    'label':'BCC me on all applications', 
    },

{'type':'Button', 
    'name':'btn_Advanced', 
    'position':(442, 440), 
    'label':'Advanced Settings', 
    },

{'type':'StaticText', 
    'name':'lbl_OutgoingMailServer', 
    'position':(311, 160), 
    'text':'Outgoing mail server (SMTP):', 
    },

{'type':'StaticText', 
    'name':'lbl_IncomingMailServer', 
    'position':(311, 115), 
    'text':'Incoming mail server (POP3):', 
    },

{'type':'StaticText', 
    'name':'lbl_Password', 
    'position':(25, 290), 
    'text':'Password:', 
    },

{'type':'StaticText', 
    'name':'lbl_UserName', 
    'position':(25, 250), 
    'text':'User Name:', 
    },

{'type':'StaticText', 
    'name':'lbl_EmailAddress', 
    'position':(25, 160), 
    'text':'E-mail Address:', 
    },

{'type':'StaticText', 
    'name':'lbl_YourName', 
    'position':(25, 115), 
    'text':'Your Name:', 
    },

{'type':'Button', 
    'name':'btn_TestAccountSettings', 
    'position':(304, 300), 
    'label':'Test Account Settings ...', 
    },

{'type':'StaticText', 
    'name':'lbl_TestSettings', 
    'position':(307, 250), 
    'size':(171, 37), 
    'text':'After filling out the information, I reccomend you test the account by clicking the button below.', 
    },

{'type':'PasswordField', 
    'name':'txt_pwd_Password', 
    'position':(103, 290), 
    },

{'type':'TextField', 
    'name':'txt_UserName', 
    'position':(103, 250), 
    },

{'type':'TextField', 
    'name':'txt_OutgoingMailServer', 
    'position':(455, 160), 
    },

{'type':'TextField', 
    'name':'txt_IncomingMailServer', 
    'position':(455, 115), 
    'enabled':False, 
    'text':'not needed', 
    },

{'type':'TextField', 
    'name':'txt_YourEmailAddress', 
    'position':(100, 160), 
    },

{'type':'TextField', 
    'name':'txt_YourName', 
    'position':(100, 115), 
    'enabled':False, 
    'text':'not needed', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(4, 343), 
    'size':(579, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'lblTestSettings', 
    'position':(307, 225), 
    'font':{'style': 'bold', 'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 10}, 
    'text':'Test Settings', 
    },

{'type':'StaticText', 
    'name':'lblServer Information', 
    'position':(309, 90), 
    'font':{'style': 'bold', 'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 10}, 
    'text':'Server Information', 
    },

{'type':'StaticText', 
    'name':'lblLogonInformation', 
    'position':(25, 225), 
    'font':{'style': 'bold', 'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 10}, 
    'text':'Logon Information', 
    },

{'type':'StaticText', 
    'name':'lblUserInformation', 
    'position':(25, 90), 
    'font':{'style': 'bold', 'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 10}, 
    'text':'User Information', 
    },

{'type':'StaticBox', 
    'name':'bxHeaderBackground', 
    'position':(0, 0), 
    'size':(579, 70), 
    'backgroundColor':(255, 255, 255), 
    'foregroundColor':(255, 255, 255), 
    },

{'type':'StaticText', 
    'name':'lblHeader2', 
    'position':(43, 37), 
    'backgroundColor':(255, 255, 255), 
    'font':{'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 10}, 
    'text':'Each of these settings are required to get your e-mail working.', 
    },

{'type':'StaticText', 
    'name':'lblHeader', 
    'position':(22, 13), 
    'backgroundColor':(255, 255, 255), 
    'font':{'style': 'bold', 'faceName': 'Times New Roman', 'family': 'sansSerif', 'size': 12}, 
    'text':'E-mail Settings (POP3)', 
    },

{'type':'StaticText', 
    'name':'lblHeaderBackground', 
    'position':(2, 8), 
    'size':(579, 60), 
    'backgroundColor':(255, 255, 255), 
    'text':'   ', 
    },

] # end components
} # end CustomDialog
