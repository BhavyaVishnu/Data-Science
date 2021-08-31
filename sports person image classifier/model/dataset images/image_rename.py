import os

path =  os.getcwd()   #get the current working directory
filenames = os.listdir(path + "//")
filenamenew = filenames[2:]

def increment():
    global COUNT
    COUNT = COUNT + 1

for i in filenamenew:
    pathnew= str(path) + '\\' + str(i)
    os.chdir(pathnew)  # changin the directory
    imagenames=os.listdir(pathnew)

    COUNT=1

    for f in imagenames:
        f_name, f_ext = os.path.splitext(f)
        f_name = i[0] +"_" + str(COUNT)
        increment()
        new_name = '{} {}'.format(f_name,f_ext)
        print(new_name)
        os.rename(f,new_name)
