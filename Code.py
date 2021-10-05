import os
import requests
import ast
from pathlib import Path 
pyton_directory=os.getcwd()
content ={}
file_loc=Path((pyton_directory)+"//data.txt")
flg=0
if file_loc.exists():
    file=open("data.txt",'r')
    content=ast.literal_eval(file.read())
    file.close()
    file=open("data.txt",'w+')
    flg=1
else:    
    file=open("data.txt",'w+')
try:    
    address=input("Enter api address : ")
    result=requests.get(address)
except:
    address=input("Enter valid api address : ")
finally:
    file.write(str(result.json()))
    for item,index in result.json().items():
        if item!= 'categories':
            if flg==0:
                print(str(item)+' has changed from None to '+str(index))
            else:
                print(str(item)+' has changed from '+ str(content.get(item)) +' to '+str(index))
file.close()