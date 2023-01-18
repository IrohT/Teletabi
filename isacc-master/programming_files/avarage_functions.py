import os
import shutil
import getpass
import subprocess

# !!!!!!!!!!!!!!!!!!!bemutatkozás!!!!!!!!!!!!!!!!!!!
def introduction():
    print(r"----/////////////////////////////////v0.2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----")
    print("A nevem IsACC ;)")
    print("A te személyi asszisztensed és legjobb barátod (ha már igaziak nincsenek xd)")
    print("feladatom problémáid megoldása")
    print("(Az alap verzió rendszergazdai jogosultsággal ajánlott)")
    print(r"----/////////////////////////////////v0.2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\----" + "\n")


# !!!!!!!!!!!pontos veszzővel van elvászatvainátor!!!!!!!!!
def is_with_pontos(words: str):
    num_pontos = words.count(";")
    if num_pontos > 0:
        return True
    return False


# !!!!!!!!!!!alsó vonallal kezdődik!!!!!!!!!
def start_with_under_line(word : str):
    if word[0] == "_":
        return True
    return False


# !!!!!!!!!!!!!!!!!!!!!!!!megvizsgálja hogy léteznek-e a szükséges fájlok!!!!!!!!!!!!!!!!!!!!!!!!!
def is_files():
    # _______________létezik-e (data)______________
    def is_data():
        the_main_d = os.listdir('./')
        if "data" in the_main_d:
            return None
        os.mkdir("data")

    # _______________létezik-e (fh.txt)______________
    def is_txt():
        data = os.listdir('./data/')
        if "_felhasznalonevek.i_s_c" in data:
            return None
        with open(r".\data\_felhasznalonevek.i_s_c", "w") as w:
            w.write("")

    # _______________létezik-e (clone)______________
    def is_clone_dir():
        the_main_dir = os.listdir("./")
        if "clones" in the_main_dir:
            return None
        os.mkdir("clones")

    is_clone_dir()
    is_data()
    is_txt()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!file_helyének_megnyitása!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def opener(path):
    browser_path= os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    
    copy_kerdes = input("szeretnéd megnyitni a fájl helyét? i/n: ")
    if copy_kerdes == "i":
        path = os.path.basename(path)

        if os.path.isdir(path):
            subprocess.run([browser_path, path])
        else:
            subprocess.run([browser_path, '/select,', path])    
    return None

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!____figyelem felhívók______!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# !!!!!!!!!!!!!!warning!!!!!!!!!!!!!!!
def warning(sentence: str):
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n {sentence} \n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")


# !!!!!!!!!!!!!!success!!!!!!!!!!!!!!!
def success(sentence: str):
    print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n {sentence} \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")


# !!!!!!!!!!!!!!f_u!!!!!!!!!!!!!!!
def f_u(sentence: str):
    print(f"8============================================================> \n {sentence} \n<=============================================================8 \n")
