import sys,traceback
# all about system
# get info about system
# about stream: sys.stdin, sys.stdout, sys.stderr


# print(sys.path)

# print(sys.modules)

def raise_err(x):
    raise TypeError('already got one')

try:
    # sys.exit()
    # exit and end the program directly
    raise_err('grail')
except:
    exc_info=sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
    # print(sys.exc_info())
    # using traceback to find the error line

