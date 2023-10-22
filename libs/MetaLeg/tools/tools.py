import os
    
####################################################    
def saveLog(filename, text):
    filename = 'data/log/' + filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w+') as destination:
        destination.write(text)
    return True
#######################################################

####################################################    
def saveProjectLog(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+') as destination:
        destination.write(text)
    return True
#######################################################