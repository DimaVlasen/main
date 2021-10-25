import json
import os
import csv 
import sys

'fd = open(filename, "w")'
'str = Fin.readline().split()'

filename = "first_group.txt"
lines = ["Sasha",72, "Borya",26, "Vova",33, "Nastya", 90, "Vasya",123]
with open (r"C:\ICS-6_VlasDimawork\main\first_group.txt","w") as file:
  json.dump(lines , file)
file.close()

'пошук файлів у каталозі'
for filename in os.listdir("C:\ICS-6_VlasDimawork\main"): 
 print(filename)


'Виведення змісту файлу'
filename = "first_group.txt"
fd = open(filename, "r") 
reader = csv.reader(fd, delimiter="\t") 
for row in reader: 
 print(row)
fd.close()


'пошук даних у файлі'

