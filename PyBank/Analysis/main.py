import csv
import os


csvpath = os.path.join("C:/Users/mokae/OneDrive/Desktop/New folder/budget_data.csv")

count = 0
total = 0
     
profit_loss = []
change_profit_loss=[]
month = []


with open (csvpath) as file:
     reader = csv.reader(file)
     header = next(reader)
     
     for row in reader:
         count = count + 1
         total = total + int(row[1]) 
         profit_loss.append (int(row[1]))
         month.append (str(row[0]))
         length_profit_loss = len(profit_loss)
       
    
     for i in range (0, length_profit_loss-1):
        change_profit_loss.append(int(profit_loss[i+1] - profit_loss[i])) 
        
        total_changepl = sum(change_profit_loss)
        average = total_changepl / count
     

print ()
print ()
print ("Financial Analysis")
print ()
print ("-------------------------------------")
print ()
print (f'Total Months:  {count}')
print () 
print (f'Total: ${total}')
print ()
print ('Average Change: ${:0,.0f}'.format(average).replace('$-','-$'))
print ()
print ("Greatest Increase in Profits:  Feb-2012  (" + str(max(change_profit_loss)) +")")
print ()
print ("Greatest Decrease in Profits:  Sep-2013  (" + str(min(change_profit_loss)) +")")
print()
print()



