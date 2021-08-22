import os
import shutil
import time

days=time.timne()
path=input('Enter file path...')
gpath=os.path.exists(path)

if(gpath==True):
    list=os.walk(path)
    desiredtime=int(input('Enter the number of dasys you want your file to stay...'))
    ctime=int(os.start(path).st_ctime)

    if(ctime> desiredtime):
        isFile=os.path.isfile(path)
        isdirectory=os.path.isdir(path)

        if(isFile):
            os.remove(path)

        if(isdirectory):
            shutil.rmtree(path)

        print('Files and folders deleted succesfully!')
        
else:
    print('Path does not exists')            
    

    