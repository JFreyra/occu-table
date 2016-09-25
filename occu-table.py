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
    counter = 0.0;
    for key in occDict:
        counter+=float(occDict[key])
        if(selectjob<=counter):
            return(key)

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
                           varD = occDict,
                           randOcc = randOcc())

if(__name__ == "__main__"):
    app.debug = True
    app.run()
