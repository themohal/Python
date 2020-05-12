import csv

with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\mycsvfile.csv") as f:
    content_file = csv.reader(f) #this is object now we need for loop to extract data

    for data in content_file:
        print(data)

with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\mycsvfile2.csv","w") as file:
    file_writer= csv.writer(file)
    #u will need to pass list
    file_writer.writerow(["2019","CW19","ENG"])
