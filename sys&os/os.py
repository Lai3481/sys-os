import os,subprocess

# print(os.environ)
# shell environment variables

# print(dir(os))

print(os.getcwd())
# get current file path

print(os.getpid())
# get current process id

# os.chdir(r'C:\PythonStudy')
print(os.getcwd())
# change current file path

print(os.path.isdir(r'C:\PythonStudy'),os.path.isfile(r'C:\PythonStudy'))
# check current path dir and file

print(os.path.exists(r'C:\PythonStudy'))
print(os.path.getsize(r"C:\PythonStudy\课程使用软件.解压密码123\课程使用软件\python-3.11.4-amd64.exe"))

print(os.path.dirname(os.getcwd()),os.path.basename(os.getcwd()))

# like clicking into the file
# os.startfile('sys.py')

# about subprocess
# remember to add python to execute python file
pipe=subprocess.Popen('python sys.py',stdout=subprocess.PIPE)

# pipe.communicate()
pipe.stdout.read()
# these two are about the same
# connecting stdout and execute

pipe.returncode
# pipe.wait()
# use for returning or terminate the program after call

# actually
# os.popen().read() = subprocess.Popen().communicate()