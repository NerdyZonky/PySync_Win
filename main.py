# -*- coding: utf-8 -*-
__author__ = 'NerdyZonky'
from rsync import rsync
from files import GetFiles
from files import ReadFilesRsync

get = GetFiles()
mode = ReadFilesRsync(get.GetMode())

print"Hole Verzeichnisse"
directory = []
i = 0
fobj = open(get.GetDir())
for line in fobj:
    directory.append(line.rstrip())
    i = i+1
fobj.close()

SRC = []
DST = []

check = mode.ReadFile()

if check == "-p":
    for i in range (len(directory)):
        tmp = directory[i].split(":")
        tmp1 = tmp[0]
        tmp2 = tmp1.split("/")
        tmp3 = "/%s" % tmp2[-1]
        tmp4 = tmp[1]
        tmp2.pop()
        tmpSRC = ("/").join(tmp2)
        tmpDST = tmp[1] + tmp3
        DST.append(tmpDST)
        SRC.append(tmpSRC)

else:
    for i in range (len(directory)):
        tmp = directory[i].split(":")
        SRC.append(tmp[0])
        DST.append(tmp[1])

print "Starte Sync..."

for i in range (len(SRC)):
    print "DST: %s SRC: %s" % (SRC[i], DST[i])
    sync = rsync(SRC[i], DST[i], mode.ReadFile())
    sync.Sync()

exit()

