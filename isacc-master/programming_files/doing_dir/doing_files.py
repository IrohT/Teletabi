from programming_files.doing_dir.clone import *


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!doings és fügvényei!!!!!!!!!!!!!!!!!!!!!!!
def doings():

    # _____________________help a doinghoz_____________________
    def help_doings():
        help_th = ["clone", "make_dir", "make_txt"]
        return [print(f"{count} = {word}") for count, word in enumerate(help_th)]

    # ________________mappa létrehozás___________________
    # TODO a mappa létrhozó v1.0 tovább fejleszteni

    def mk_directory():
        mk_kerdes = input("a mappa nevét alsó vonallal kezdve irja le: ")

        if start_with_under_line(mk_kerdes):
            os.mkdir(mk_kerdes)
            success(f"{mk_kerdes} nevű mappa létre hozva")
        else:
            warning("nem alsóvonallal kezdődik")

    # ________________doing kérdés motor________________
    while True:
        doi_kerdes = input(f"mit szeretne csinálni?(help): ")

        if doi_kerdes == "help": help_doings()
        elif doi_kerdes == "0": clone()
        elif doi_kerdes == "1": mk_directory()
        elif doi_kerdes == "2": print("készül")

        else:
            f_u("ha nagyon agyhalott vagy nem véletlenül van ott a help a zárójelben")
            f_u("még egy kis segítség a számok sem véletlenül vannak ;)")

