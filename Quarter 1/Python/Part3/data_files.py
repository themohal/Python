with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myfile.txt","w") as fileWrite:
    fileWrite.write("This is first line")

with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myfile.txt","r") as fileRead:
    content = fileRead.read()
    print(content)
 
with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myfile.txt","a") as fileAppend:
    fileAppend.write("\nThis is 2nd line")
    
with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myfile.txt","r") as fileRead:
    content = fileRead.read()
    print(content)
  # w+ and r+ modes allow to read and write at the sametime
  # use file.seek(0) to read and write at same time before printing otherwise it will print blank