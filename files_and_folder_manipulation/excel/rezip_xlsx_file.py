#!/usr/bin/env python
import os
import zipfile

def zipdir(path, ziph):
    os.chdir(path)
    # ziph is zipfile handle
    for root, dirs, files in os.walk("."):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('tc_insert.xlsx', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./fichero_excel/', zipf)
    zipf.close()

    print("Excel file generated with individual files in '/fichero_excel'.\n")

    input('Press ENTER to exit...')