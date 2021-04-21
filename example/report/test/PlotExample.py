import matplotlib.pyplot as plt
import csv

def analyzeBirths():
    #years = range(1880, 2012)
    pieces = []
    datafile = 'D:\\plotTest\\births.txt'
    with open(datafile, 'rt') as f :
        data = csv.reader(f, delimiter = ',')
        for d in data:
            pieces.append(d)
    
    x = [year for year, female, male in pieces]
    y1 = [female for year, female, male in pieces]
    y2 = [male for year, female, male in pieces]
    
    plt.plot(x, y1, 'r^--', label='female')
    plt.plot(x, y2, 'bs-', label='male')
    
    plt.legend()
    plt.title('Total')
    plt.xlabel('Year'), plt.ylabel('Births')
    plt.show()
    
if __name__== '__main__':
    analyzeBirths()