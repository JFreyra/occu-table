#Julius Freyra + Jiaqi Gao
import csv, random

def whichOcc():

    with open("occupations.csv", mode="r") as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)

    return mydict
    
    #data = open("occupations.csv").read()
    #data = data.replace(', ', '+')
    #data = data.replace(',', '\n').split('\n')
    #for x in range(0, len(data)):
    #    data[x] = data[x].replace('+', ', ')
    #total = int(float(data[len(data)-2]))*10
    #data = data[2:len(data)-3]
   # 
   # occ = []
   # per = []
   # while len(data) > 1:
   #     occ.append(data[0])
   #     per.append(data[1])
   #     data = data[2:]
    
    #selectjob = float(random.randint(1,total))
    #counter = 0.0;
    #for x in range(0, len(occ)):
    #    counter+=float(per[x])*10
    #    if(selectjob<=counter):
    #        return(occ[x])

print whichOcc()
