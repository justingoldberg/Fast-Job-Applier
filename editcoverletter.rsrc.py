{'type':'CustomDialog',
    'name':'editcoverletter',
    'title':'Edit your cover letter',
    'position':(199, 114),
    'size':(600, 600),
    'components': [

{'type':'TextField', 
    'name':'txt_savetoname', 
    'position':(385, 525), 
    'size':(177, -1), 
    'enabled':False, 
    'toolTip':'name for file', 
    },

{'type':'CheckBox', 
    'name':'chk_saveas', 
    'position':(315, 530), 
    'size':(63, -1), 
    'label':'Save as', 
    },

{'type':'CheckBox', 
    'name':'chk_save', 
    'position':(315, 515), 
    'label':'Save', 
    'toolTip':'Make modifications to this cover letter permanent.', 
    },

{'type':'TextArea', 
    'name':'txt_coverletter', 
    'position':(0, 0), 
    'size':(590, 500), 
    },

{'type':'Button', 
    'id':5100, 
    'name':'btnOK', 
    'position':(112, 515), 
    'label':'OK', 
    'toolTip':'Save modifications for this session only.', 
    },

{'type':'Button', 
    'id':5101, 
    'name':'btnCancel', 
    'position':(213, 515), 
    'label':'Cancel', 
    'toolTip':"Don't save", 
    },

] # end components
} # end CustomDialog
