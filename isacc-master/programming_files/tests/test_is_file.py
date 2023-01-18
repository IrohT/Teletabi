import os


clone_dir_name = os.path.dirname("../.")
clone_things = os.listdir(clone_dir_name)


for file in clone_things:
    path = clone_dir_name + "/" + file
    print(path)
    if os.path.isdir(path):
        print(f"{file} egy file")
    else:
        print(f"{file} nem egy file")

