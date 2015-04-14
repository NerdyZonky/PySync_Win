# -*- coding: utf-8 -*-
__author__ = 'marco'


class rsync:

    def __init__(self, source, target, modus):
        self.__source = source
        self.__target = target
        self.__modus = modus

    def Sync(self):

        import os

        if self.__modus == '-d':
            print('Default Sync wird gestartet')
            os.system('rsync.exe -av ' + self.__source + " " + self.__target+' --exclude=exdir.txt')

        elif self.__modus == '-i':
            print('Inkrementeller Sync wird gestartet')
            os.system('rsync.exe -av --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt')

        elif self.__modus == '-s':
            print('Safe Sync wird gestartet')
            os.system('rsync.exe -avb --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt --backup-dir='+self.__target+'/deleted')

        elif self.__modus == '-p':
            print('Playback-Sync wird gestartet')
            os.system('rsync  -av '+ self.__target + " " + self.__source)

        elif self.__modus == '--try -d':
            print('Teste Default Sync')
            os.system('rsync.exe -nav ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt')

        elif self.__modus == '--try -i':
            print('Teste Inkrementellen Sync')
            os.system('rsync.exe -nav --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt')

        elif self.__modus == '--try -s':
            print('Teste Safe SSH-Sync')
            os.system('rsync.exe -avb --delete ' + self.__source + " " + self.__target+ ' --exclude=exdir.txt --backup-dir='+self.__target+'/deleted')

        elif self.__modus == '--try -p':
            print('Teste Playback SSH-Sync')
            os.system('rsync  -nav '+ self.__target + " " + self.__source)

        else:
            print ('Falscher Parameter in mode')
            print('Default SSH-Sync wird gestartet')
            exit()

