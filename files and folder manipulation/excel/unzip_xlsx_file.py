import zipfile
import os
import shutil

dirpath = "./fichero_excel/"
for filename in os.listdir(dirpath):
    filepath = os.path.join(dirpath, filename)
    try:
        shutil.rmtree(filepath)
    except OSError:
        os.remove(filepath)


zip_ref = zipfile.ZipFile("./tc_insert.xlsx", 'r')
zip_ref.extractall(dirpath)
zip_ref.close()

print("Files extracted from excel file.\n")

input('Press ENTER to exit...')