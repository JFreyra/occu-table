from flask import Flask, render_template
import csv, random

app = Flask(__name__)

linksT = ["Jobs!",
          "Tables!",
          "Occupation Table!"]

def occDict():
    with open("occupations.csv", mode="r") as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)
    for(key in mydict):
        try:
            float(mydict[k])
        except ValueError:
            popitem(key, mydict[k])
    return mydict

def randOcc():
    selectjob = float(random.randint(1,total))
    counter = 0.0;
    for x in range(0, len(occ)):
        counter+=float(per[x])*10
        if(selectjob<=counter):
            return(occ[x])

occDict = occDict()
            
@app.route("/")
def home():
    links = ["jobs",
            "tables",
            "occupations"]
    return render_template("basic.html",
                           title = "Homepage",
                           heading = "Links: jobs, tables, occupation table!",
                           links = True,
                           varL = links)

@app.route("/jobs")
def jobs():
    return "hello"
    #return render_template

@app.route("/tables")
def tables():
    return "hello"

@app.route("/occupations")
def occupations():
    return render_template("table.html",
                           title = "Occupation Table",
                           heading = "Occupations; Percentage of Workforce",
                           varD = occDict)

if(__name__ == "__main__"):
    app.debug = True
    app.run()
