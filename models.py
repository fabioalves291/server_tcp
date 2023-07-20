import os,sys 


def dir_list(self):
    resulted_dir_listed       =   str()
    cont_dir        =   0
    filelist        =   os.listdir(self)
    for file in filelist:
        cont_dir += 1
        file        =   str(file)
        wordspace   =   ((48-len(file))*' ')
        resulted_dir_listed   =  resulted_dir_listed    +   (file + wordspace + (str(os.path.getsize(fr'{self}/{file}'))) + ' Bytes'+'\n')
    
    return (resulted_dir_listed,cont_dir)
