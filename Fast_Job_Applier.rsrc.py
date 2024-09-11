{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'MainForm',
          'title':'Fast Job Applier',
          'position':(29, 25),
          'size':(853, 424),
          'statusBar':1,
          'icon':'jobapplier16.ico',
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuAddResumes',
             'label':'Add Resumes',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuAddResumesHowTo',
                   'label':'How To',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuOptions',
             'label':'Options',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuOptionsSettings',
                   'label':'Settings',
                  },
                  {'type':'MenuItem',
                   'name':'menuOptionsAutoPasteMode',
                   'label':'Auto-Paste Mode',
                   'checkable':1,
                  },
                  {'type':'MenuItem',
                   'name':'menuOptionsTestingMode',
                   'label':'Testing Mode',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':'Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuAbout',
                   'label':'About',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'Start', 
    'position':(1000, 10), 
    'label':'Start', 
    },

{'type':'Button', 
    'name':'btn_batchapply', 
    'position':(4, 290), 
    'size':(831, 58), 
    'label':'Send off the emails', 
    },

{'type':'StaticText', 
    'name':'lbl_resume', 
    'position':(610, 20), 
    'text':'Resume', 
    },

{'type':'StaticText', 
    'name':'lbl_coverletter', 
    'position':(480, 20), 
    'text':'Cover Letter', 
    },

{'type':'StaticText', 
    'name':'lbl_url', 
    'position':(340, 20), 
    'text':'Job url', 
    },

{'type':'StaticText', 
    'name':'lbl_employername', 
    'position':(240, 20), 
    'text':'Employer Name', 
    },

{'type':'StaticText', 
    'name':'lbl_emailaddr', 
    'position':(120, 20), 
    'text':'Email Address', 
    },

{'type':'StaticText', 
    'name':'lbl_position', 
    'position':(0, 20), 
    'text':'Position/Title', 
    },

] # end components
} # end background
] # end backgrounds
} }
