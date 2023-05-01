# PyBank

import os
import csv
import sys

ml = [] #dates by month
pl = [] #profit for each month
x = 0  # total profit
diff = 0 #sum of profit differences
t1 = 0
t2 = 0
GI = 0 #Greatest Profit Increase
LI = 0 #Greatest Profit Decrease
linecount = 0

# putting file path in a variable
budget_path = os.path.join('Resources','budget_data.csv')


# opening csv file and formatting for reading
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=',')
    
    # skipping headers
    for y in budget_reader:
        if linecount == 0:
            header_store = y #stores headers
            linecount += 1
        # placing items in python 'files'
        else:
            ml.append(y[0])
            pl.append(y[1])
        
months = len(ml) # total number of months

# Gets total profit, difference in profit month-to-month,
# and finds and locates date for largest profit increase and largest profit decrease
for i in range(months):
    t1 = int(pl[i])
    x = t1 + x

    if i == (months - 1):
        diff = diff
    else:
        subdiff = (int(pl[i+1]) - t1) #difference in profit from prior month
        diff = diff + subdiff 
# finds largest profit increas and largest profit decrease
        if subdiff > GI:
            GI = subdiff   # Largest increase
            GIplace = i + 1  #Largest increase month pointer
        elif subdiff < LI:
            LI = subdiff  #Largest decrease
            LIplace = i + 1 #Largest profit decrease month pointer
        
# finds the average profit difference month-to-month
AvgChg = round((diff/85), 2)

#stores original standard output
original_stdout = sys.stdout

# writes analysis to a text file
with open(os.path.join('analysis','analysis.txt'),"w") as file1:
    sys.stdout = file1

    print("Financial Analysis")
    print("--------------------------")
    print("Total Months:",months)
    print("Total: ${}".format(x))
    print("Average Change: ${}".format(AvgChg))
    print ("Greatest Increase in Profits:",ml[GIplace],"(${})".format(GI))
    print ("Greatest Decrease in Profits:",ml[LIplace],"(${})".format(LI))

    sys.stdout = original_stdout

# prints analysis on terminal
print("Financial Analysis")
print("--------------------------")
print("Total Months:",months)
print("Total: ${}".format(x))
print("Average Change: ${}".format(AvgChg))
print ("Greatest Increase in Profits:",ml[GIplace],"(${})".format(GI))
print ("Greatest Decrease in Profits:",ml[LIplace],"(${})".format(LI))
    
    




    