import sys
import pandas
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, Dropdown
from datetime import date

print("test")


def beautify(stringo):
    stringo=stringo.split("-")
    return str(int(stringo[2]))+"/"+str(int(stringo[1]))

def showresults(fl):
        x=[]
        y=[]
        x1=[]
        c = []
        handle = fl.readlines()

        for fl in handle:
            z=fl.split(";")
            x1.append(beautify(z[0]))
            x.append(z[0])
            print(z[0])
            y.append(int(z[1]))
            c.append("green") if z[2]=="True" else c.append("red")
        
        plot_types = {"classic":"classic","deviation":"deviation"}
        dropdown = Dropdown(ax=ax, labels=list(plot_types.keys()))
        plt.bar(x, y, color = c, label = "Freethrows")
        plt.ylim([20,70])
        plt.xlim(["2023-02-16",str(date.today())])
        plt.xlabel('Date')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels(x1)
        plt.ylabel('Attempts')
        plt.title('Your progress')
        plt.legend()
        plt.show()
def runadder(input,fl):
    print(input)
    stringtoadd=str(date.today()) +";"+ ";".join(input) + "\n"
    print(stringtoadd)
    fl.write(stringtoadd)
    print("worked")

command = sys.argv[1]
if command == "add":
    with open("/home/schulzkilian/meinzeug/Code/python/basketball/basketball.txt","a+") as fl:
        runadder(sys.argv[2::],fl)
elif command == "show":
    with open("/home/schulzkilian/meinzeug/Code/python/basketball/basketball.txt","r") as fl:
        showresults(fl)



    



