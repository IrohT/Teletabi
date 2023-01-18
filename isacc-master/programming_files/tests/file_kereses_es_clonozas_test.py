import os
import shutil
  

# _______________________file másoló__________________
def copy_file(f_file):
    file_name = os.path.basename(f_file)
    file_th = file_name.split(".")
    file_copy = "(copy)."

    shutil.copyfile(f_file, "ahova menteni akarod(útvonal)")
# -------------------------------------------------------


# _________________________file kereső_________________
def file_finder():

    file_name = input("írd be a fájl nevét: ")
    for root, dirs, files in os.walk("amin végig sétál(útonal)"):
        for name in files:
            if name == file_name:  
                file_path = os.path.abspath(os.path.join(root, name))
                copy_file(file_path)
# ----------------------------------------------------------


file_finder()
