import os,sys 


def dir_list(self):
    resulted_dir_listed       =   str()
    filelist        =   os.listdir(self)
    for file in filelist:
        file        =   str(file)
        wordspace   =   ((48-len(file))*' ')
        resulted_dir_listed   =   totallist    +   (file + wordspace + (str(os.path.getsize(fr'{self}/{file}'))) + ' Bytes'+'\n')
    return resulted_dir_listed
