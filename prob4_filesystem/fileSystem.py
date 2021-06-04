import os
#importing os library
def cd(a):
   if a.startswith(".."):
      os.chdir("..")
      res = a.replace("..",'')
      os.chdir(res)
   else:
      os.chdir(a)
   print("Current working directory :",os.getcwd())

val = raw_input("Enter the path: ")
cd(val)
