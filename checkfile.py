# import required module
import os
import time
from datetime import date

today = date.today()
# dd/mm/YY
dt = today.strftime("%d/%m/%Y")
# assign directory
directory = ''

f = open("log.txt", "w+")
 
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        modTimesinceEpoc = os.path.getmtime(filename)
        modifiedtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
        file = str(filename.path) + " " + str(modifiedtime)
        f.write(file)
        f.close()