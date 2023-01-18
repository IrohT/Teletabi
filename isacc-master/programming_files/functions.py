import os
import shutil
import getpass

def introduction():
    print("___________________________")
    print("A nevem IsACC ;)")
    print("A te személyi asszisztensed és legjobb barátod (ha már igaziak nincsenek xd)")
    print("feladatom problémáid megoldása")
    print("___________________________ \n")

# pontos veszzővel van elvászatvainátor
def is_with_pontos(words : str):
    num_pontos = words.count(";")
    if num_pontos > 0:
        return True
    return False

def start_with_under_line(word : str):
    if word[0] == "_":
        return True
    return False



def is_files():
    def is_data():
        the_main_d = os.listdir('./')
        if "data" in the_main_d:
            return None
        os.mkdir("data")

    def is_txt():
        data = os.listdir('./data/')
        if "_felhasznalonevek.txt" in data:
            return None
        with open(".\data\_felhasznalonevek.txt", "w") as w:
            w.write("")

    is_data()
    is_txt()


# bejelentkezés
def log_in():
    global r
    while True:
        kerdes = (input("kérem a felhasználónevet és a jelszót pontos vesszővel el választva(;): ")).lower()
        if is_with_pontos(kerdes):
            with open(".\data\_felhasznalonevek.txt") as r:
                f_and_p = [sor for sor in r]
                if kerdes in [sor.strip() for sor in f_and_p if sor.strip() == kerdes]:
                    print("üdvözlünk! <3")
                    return True
                else:
                    print("A felhasználónév vagy jelszó hibás")
                    is_user()
        print("nem tartalmaz pontosveszzőt(;)!!")
        continue


# felhasználó készítés
def mk_user():
    while True:
        kerdes = (input("kérem a felhasználónevet és a jelszót pontos vesszővel el választva(;): ") + "\n").lower()
        if is_with_pontos(kerdes):
            with open(".\data\_felhasznalonevek.txt", "a") as a:
                a.write(kerdes)
                break
        print("nem tartalmaz pontosveszzőt(;)!!")
        continue


# elosztó
def is_user():
    while True:
        kerdes = input("van már felhasználói fiókod(i/n): ").lower()
        if kerdes == "i":
            return log_in()
        elif kerdes == "n":
            mk_user()
        else:
            print("szövegértés eggyes")
            continue


def doings():
# ----------------------------------help a doinghoz-----------------------
    def help_doings():
        help_th = ["clone", "make_dir", "make_txt"]
        return [print(f"{count} = {word}") for count, word in enumerate(help_th)]
# ______________________________Funkciók____________________
# --------------clonozó--------------------------------
# TODO: továnn fejleszteni a v1.0 verziot nagyob körű adat eléréshez
    def clone_file():
        print('isacc csak az anya könyvtárat clonozza le')
        the_main_c = os.listdir("./")
        if "clones" in the_main_c:
            clone_name = os.path.dirname("../isacc")
            clone_things = os.listdir(clone_name)

            for file in clone_things:
                file_th = file.split(".")
                file_copy = "(copy)."

                if file != "isacc":

                    try:
                        shutil.copyfile(clone_name + '/' + file, f'./clones/{file_th[0] + file_copy + file_th[1]}')

                    except:
                        try:
                            print(f"hozzá férés kérése a mappához: {file} \n")
                            shutil.copytree(clone_name + '/' + file, f'./clones/{file_th[0] + file_copy}')
                        except:
                            pass
        else:
            os.mkdir("clones")
            print("clones nevű mappa nem volt létrehozva most probálja meg")
# -----------------------------mappa létrehozás ------------------
#TODO a mappa létrhozó v1.0 tovább fejleszteni
    def mk_directory():
        kerdes = input("a mappa nevét alsó vonallal kezdve irja le: ")
        os.mkdir(kerdes)
        print(f"{kerdes} nevű mappa létre hozva")



# ---------------------doing_kérdés motor--------------
    while True:
        kerdes = input(f"mit szeretne csinálni?(help): ")

        if kerdes == "help":    help_doings()
        elif  kerdes == "0":  clone_file()
        elif kerdes == "1": mk_directory()

        else:
            print("ha nagyon agyhalott vagy nem véletlenül van ott a help a zárójelben 8===>")
            print("még egy kis segítség a számok sem véletlenül vannak ;)")



