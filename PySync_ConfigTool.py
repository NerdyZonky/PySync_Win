# -*- coding: utf-8 -*-
__author__ = 'NerdyZonky'

import os
from files import GetFiles
from files import ReadFiles
from files import WriteFiles
from files import ReadFilesRsync
from Output import Menu


get = GetFiles()
directory = ReadFiles(get.GetDir())
mode = ReadFiles(get.GetMode())
menu = Menu()

menu.GetLicence()

while True:

    menu.GetMainMenu()

    choose = raw_input()

    if choose == "1":
        print"Folgende Verzeichnisse sind aktuell gespeichert:"
        print"................................................"
        directory.ReadFile()
        print"................................................\n"
        print"Möchten Sie die Verzeichnisse wirklich ändern?"
        print"j/n"
        choose = raw_input()

        if choose == "n":
            pass

        if choose == "j":
            i = 0
            SRC = []
            DST = []

            while True:
                print "Bitte geben Sie das Quellverzeichnis",i+1, "ein:"
                put = raw_input()
                put2 = put.split(":")
                put3 = put2[0].lower()
                put4 = put2[1].replace("\\","/")
                put5 = "/cygdrive/"+put3+put4
                SRC.append(put5)
                print "Bitte geben Sie das Zielverzeichnis", i+1, "ein:"
                put = raw_input()
                put2 = put.split(":")
                put3 = put2[0].lower()
                put4 = put2[1].replace("\\","/")
                put5 = "/cygdrive/"+put3+put4
                DST.append(put5)
                print "Möchten Sie weitere Verzeichnisse angeben?"
                print "j/n"
                choose = raw_input()
                if choose == "j":
                     i=i+1

                if choose == "n":
                    print"Folgende Verzeichnisse wurden angegeben:"
                    print"................................................"
                    for i in range (len(SRC)):
                        print("Quelle: %r  Ziel: %r" %(SRC[i],DST[i]))
                    print"................................................\n"
                    print("Sind die Verzeichnisse korrekt?")
                    print"j/n/q"
                    choose = raw_input()
                    if choose == "n":
                        SRC = []
                        DST = []
                        continue
                    if choose == "j":
                        pass

                    if choose == "q":
                        break

                    fobj = open(get.GetDir(),"w")
                    print"Schreibe Änderungen...\n"
                    for i in range(len(SRC)):
                        fobj.write(str(SRC[i]) + ":" + DST[i])
                        fobj.write("\n")
                    fobj.close()

                    print"Verzeichnisse wurden Geändert!"
                    break



    if choose == "2":
            print"Aktueller Modus:"
            print"....................."
            mode.ReadFile()
            print".....................\n"

            print"Möchten Sie den Modus wirlich ändern?"
            print"j/n"
            choose = raw_input()
            if choose == "n":
                print"Beende Programm"
                exit()

            if choose =="j":
                while True:
                    print"Geben Sie den neuen Modus ein:"
                    menu.ModeMenu()
                    mode = raw_input()
                    print"Neuer Modus: %r \n" % mode
                    print"Ist der neue Modus korrekt?"
                    print"j/n/q"
                    choose = raw_input()
                    if choose == "j":
                        WriteMode = WriteFiles(get.GetMode(),mode)
                        WriteMode.WriteFile()
                        print 'Modus wurde geändert!'
                        break
                    if choose == "n":
                        continue

                    if choose == "q":
                        break

    if choose == "3":
        print"VERZEICHNISSE:"
        print"................................................"
        directory.ReadFile()
        print"................................................"
        print"MODUS:"
        mode.ReadFile()
        print "\n"
        print"zurück zum Menü = beliebige Taste"
        q = raw_input()
        if q == " ":
            pass

    if choose == "4":
        swap = ReadFilesRsync(get.GetMode())
        swap2 = swap.ReadFile()

        fobj = open(get.GetMode(),"w")
        fobj.write("--try " + swap2 )
        fobj.close()
        os.system("C:\Python27\python.exe main.py")
        fobj = open(get.GetMode(),"w")
        fobj.write(swap2)
        fobj.close()
        print"Synchronisationstest abgeschlossen. Zurück zum Menu?"
        print"j/n"
        z = raw_input()
        if z == "j":
            pass

        if z == "n":
            print"Beende Sync"
            print"Ciao!"
            exit()

    if choose == "5":
        os.system("C:\Python27\python.exe main.py")
        print"Manuelle Synchronisation abgeschlossen.Zurück zum Menü?"
        print"j/n"
        z = raw_input()
        if z == "j":
            pass

        if z == "n":
            print"Beende PySync"
            print"Ciao!"
            exit()


    if choose == "6":
        swap = ReadFilesRsync(get.GetMode())
        swap2 = swap.ReadFile()
        fobj = open(get.GetMode(),"w")
        fobj.write("-p")
        fobj.close()
        os.system("C:\Python27\python.exe main.py")
        fobj = open(get.GetMode(),"w")
        fobj.write(swap2)
        fobj.close()
        print"Daten wurden zurück gespielt. Zurück zum Menü?"
        print"j/n"
        if z == "j":
            pass

        if z == "n":
            print"Beende PySync"
            print"Ciao!"
            exit()

    if choose == "8":
        print"Beende PySync"
        print"Ciao"
        exit()

