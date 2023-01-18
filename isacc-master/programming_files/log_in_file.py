from programming_files.avarage_functions import *


# !!!!!!!!!!!!!!!!!elosztó!!!!!!!!!!!!!!!!!
def is_user():
    # ______________bejelentkezés________________
    def log_in():
        while True:
            user_data = (input("kérem a felhasználónevet és a jelszót pontos vesszővel el választva(;): ")).lower()
            if is_with_pontos(kerdes):
                with open(r".\data\_felhasznalonevek.i_s_c") as r:
                    f_and_p = [sor for sor in r]
                    if user_data in [sor.strip() for sor in f_and_p if sor.strip() == user_data]:
                        print("üdvözlünk! <3")
                        return True
                    else:
                        print("A felhasználónév vagy jelszó hibás")
                        is_user()
            print("nem tartalmaz pontosveszzőt(;)!!")

    # _____________felhasználó készítés____________
    def mk_user():
        while True:
            user_data = (input("kérem a felhasználónevet és a jelszót pontos vesszővel el választva(;): ") + "\n").lower()
            if is_with_pontos(kerdes):
                with open(r".\data\_felhasznalonevek.i_s_c", "a") as ap:
                    ap.write(user_data)
                    print("a felhasználó létrehozva")
                    break
            else:
                print("nem tartalmaz pontosveszzőt(;)!!")

    # ________________elosztó a elhasználó készítés és bejelentkezés_________________
    while True:
        kerdes = input("van már felhasználói fiókod(i/n): ").lower()
        if kerdes == "i":
            return log_in()
        elif kerdes == "n":
            mk_user()
        else:
            print("szövegértés eggyes")

