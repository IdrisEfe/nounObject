import pandas as pd

picnicItems = {'eggs': '2', 'milk': '1 liter'}
#picnicItems['hamburger'] = '2'  
picnicItems.keys()

picnicParticipants = ['İdris', 'Efe']

picnicObjects=[]

for i in picnicItems.keys():
    j=picnicItems[i]
    picnicObjects.append(f'{j} {i}')
    

liist = pd.Series(picnicObjects, picnicParticipants)

print(liist)

file=open('picnic.txt', 'a')
open('picnic.txt', 'r+')
file.truncate(0)
file.write(f'{liist}')
open('picnic.txt', 'r')