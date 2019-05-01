import numpy as np
import csv
mon_fichier = open("test mot 1.txt", "r")
text=mon_fichier.read()
LL=text.split(' ')
text = text.replace('\n', ' ')
Lk=text.split(' ')
Ln=[]
Lc=[]
for v in range(0,len(Lk),2):
 
    Ln.append(Lk[v]+'.png')
    Lc.append(Lk[v+1])
mylist = list(dict.fromkeys(Lc))
mat=np.zeros((len(Lc),len(mylist)))
for i in range (mat.shape[0]):
 for j in range (mat.shape[1]):
    if(mylist[j]==Lc[i]):
     mat[i,j]=1
    else:
     mat[i, j] = 0
col=[]
col.append('filenames')
col= col +mylist

with open('mycsv.csv','w',newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(col)
    for i in range (len(Ln)):
        liste=[]
        liste.append(Ln[i])
        p=mat[i,:]
        for l in range (len(p)):
            liste.append(int(p[l]))
        thewriter.writerow(liste)


