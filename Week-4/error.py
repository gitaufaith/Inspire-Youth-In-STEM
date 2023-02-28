filename='test.txt'

try:
  for file in filename:
   with open(filename,'r+w',encoding=None)as f_obj:
    contents=f_obj.read()
    print(contents)
except FileNotFoundError:
  msg="sorry.the file"+filename+"does not  exist"
print(msg)#
