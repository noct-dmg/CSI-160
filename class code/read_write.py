'''
The code in this file will allow a user to do the following:
1. Create a file and then write data to it.
2. Append data to an existing file.
3. Read data from a file.
'''

'''
path = directory
data = file name
ext = file extension (.txt)
'''
def manage_process(path, data, ext):
    try:
        message = input('Enter your message:')
        with open(path + '/' + data + ext, 'a') as f:
            f.write(message + '\n')
        print("Your file has been saved.")
    except Exception as e:  # Exception captures the interpreter's error name
        print(e)


def manage_start():
    data = input('File name to read:')
    ext = input('Enter the file extension:')
    path = input("Enter a path:") # relative path to the sub-directory
    #path = path+'/'
    try:
        with open(path + '/' + data + ext, 'r') as r:  # as r, all methods drop into 'r'
            if(r.read()):
                print("File exists, do you want to append data to it?")
                choice = input('Please enter y/n:')
                if choice == 'y':
                    manage_process(path, data, ext)
                else:
                    pass
            else:
                pass
    except:
        print('File does not exist. Do you want to create')
        print('it and add data?')
        ans = input('Enter "y" or "n".')
        if (ans == 'y'):
            manage_process(path,data, ext)
        else:
            print('Good-bye')
            try:
                exit()  # Quits a Python function without a Traceback
            except Exception as e:
                print(e)

manage_start()