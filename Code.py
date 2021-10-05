import os
import requests
import ast
from pathlib import Path 
pyton_directory=os.getcwd()
content ={}
file_loc=Path((pyton_directory)+"//api_data.txt")
flg=0
if file_loc.exists():
    file=open("api_data.txt",'r')
    content=ast.literal_eval(file.read())
    file.close()
    file=open("api_data.txt",'w+')
    flg=1
else:    
    file=open("api_data.txt",'w+')
while True:
    try:    
        address=input("Enter api address : ")
        result=requests.get(address)
    except:
            print("Enter valid api address")
    else:
        break
file.write(str(result.json()))
if flg==0:
    print("This is the first execution")
for item,index in result.json().items():
    if item!= 'categories':
      if flg==0:
          print(str(item)+' is '+str(index))
      else:
           print(str(item)+' has changed from '+ str(content.get(item)) +' to '+str(index))
file.close()