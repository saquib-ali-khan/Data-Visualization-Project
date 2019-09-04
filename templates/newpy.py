f = open("/Users/saquibalikhan/Downloads/dash/templates/new.txt",'r')

arr = []
for line in f:
    arr.append("#"+line.strip().strip('"'))

print (arr)