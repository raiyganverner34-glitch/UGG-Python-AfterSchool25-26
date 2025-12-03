#Program Desctiption: checking multiples of 5 from no.s 1-20

#Creating list called numbers

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#for loop check numbers divible by 5
for i in number:
    if i % 5 == 0:
       print(i)