import os
import sys

if len(sys.argv) >= 2:
    mot_cle = " ".join(sys.argv[1:])
else:
    mot_cle = input("Mot à chercher ? : ")

def dirl(path):
    global files
    listdir = os.listdir(path)
    for item in listdir:
        if os.path.isdir(item):
            dirl(path + "/" + item)
        elif item.endswith(".py"):
            files.append(path + "/" + item)


files = list()
py_mot = list()
dirl(".")

print("%d fichiers python ont été trouvés dans le répertoire courant" % len(files))
# print(len(files))
for file in files:
    # print(file)
    # print("Opening %s" % file)
    fo = open(file, "r", encoding = "utf8")
    for line in fo.readlines():
        if mot_cle in line:
            py_mot.append(file)
            break

if len(py_mot) == 0:
    print("Aucun fichier .py contient \"%s\"" % mot_cle)
else:
    print("Les fichiers suivants contiennent \" %s\" (%d)" % (mot_cle, len(py_mot)))
    print("%s : " % [file for file in py_mot])
    req = input("Quoi ouvrir ? : ")
    print([req])
    if req.isnumeric():
        for i,file in enumerate(py_mot):
            if i == int(req):
                break
            os.system("atom " + file)
    for file in py_mot:
        if req in file:
            print("Ouverture de", file)
            os.system("atom \"%s\"" % file)
