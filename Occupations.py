#Julius Freyra + Jiaqi Gao
import csv, random

def occDict():
    with open("occupations.csv", mode="r") as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)
    for key in mydict:
        try:
            float(mydict[key])
        except ValueError:
            mydict.pop(key, mydict[key])
            break
    return mydict

occDict = occDict()

def randOcc():
    selectjob = random.random()*float(occDict["Total"])
    print(selectjob)
    counter = 0.0;
    for key in occDict:
        counter+=float(occDict[key])
        if(selectjob<=counter):
            return(key)

    
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

print(randOcc())
