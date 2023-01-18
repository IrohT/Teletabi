from programming_files.avarage_functions import *


#  !!!!!!!!!!!!!!!!!!!!!!clonozó!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TODO: tovább fejleszteni a v1.0 verziot nagyob körű adat eléréshez
def clone():
    help_th = ["anya_könyvtár", "file_keresés", "könyvtár_keresés"]

    # ____clonozó parancsok_____
    def clone_help(f_list):
        return [print(f"{count} = {word}") for count, word in enumerate(f_list)]

    # ______könyvtár másoló_____
    def copy_dir(f_dir):
        dir_name = os.path.basename(f_dir)
        dir_copy = "(copy)"

        warning(f"mappa hozzáférés kérése: {dir_name}")
        try:
            shutil.copytree(f_dir, f'./clones/{dir_name + dir_copy}')
        except:
            warning("A könytár nem eléhető")
            return None
        
        #opener(f_dir)
        
    # ______file másoló_____
    def copy_file(f_file):
        file_name = os.path.basename(f_file)
        file_th = file_name.split(".")
        file_copy = "(copy)."

        warning(f"file hozzáférés kérése: {file_name}")
        try:
            shutil.copyfile(f_file, f'./clones/{file_th[0] + file_copy + file_th[1]}')
        except:
            warning("A fájl nem eléhető")
            return None
        
        #opener(f_file)

    # ______file kereső_____
    def file_finder():
        file_name = input("írd be a fájl nevét: ")
        for root, dirs, files in os.walk('C:/'):
            for name in files:
                if name == file_name:  
                    file_path = os.path.abspath(os.path.join(root, name))
                    print(file_path)
                    copy_file(file_path)

    # ______file kereső_____
    def dir_finder():
        warning("alapvető mappákat amit nem a felhasználó hozot létre nem érdemes ezzel másolni")
        dir_name = input("írd be a mappa nevét: ")
        for root, dirs, files in os.walk('C:/'):
            for name in dirs:
                if name == dir_name:  
                    dir_path = os.path.abspath(os.path.join(root, name))
                    print(dir_path)
                    copy_dir(dir_path)
                    continue

    # ____clone parent_____
    def parent_file():
        cur_dir_name = os.path.basename(os.getcwd())
        clone_dir_name = os.path.dirname("../")
        clone_things = os.listdir(clone_dir_name)
        for file in clone_things:
            file_path = clone_dir_name + "/" + file
            if file != cur_dir_name:
                if os.path.isdir(file_path):
                    copy_dir(file_path)

                else:
                    copy_file(file_path)

    while True:      
        kerdes = input("mit szeretnél csinálni clone(help): ")
         
        if kerdes == "help": clone_help(help_th)
        elif kerdes == "0": parent_file()
        elif kerdes == "1": file_finder()
        elif kerdes == "2": dir_finder()

        else:
            f_u("ha nagyon agyhalott vagy nem véletlenül van ott a help a zárójelben")
            f_u("még egy kis segítség a számok sem véletlenül vannak ;)")
         

