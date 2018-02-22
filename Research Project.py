import csv

f=open('riskfactors.csv')
csv_f=csv.reader(f)
factor1=[]
factor2=[]
factor3=[]
factor4=[]
factor5=[]
states=[]

for row in csv_f:
    states.append(row[0])
    factor1.append(row[1])
    factor2.append(row[5])
    factor3.append(row[7])
    factor4.append(row[11])
    factor5.append(row[13])


title1=factor1[5]
title2=factor2[5]
title3=factor3[5]
title4=factor4[5]
title5=factor5[5]

del states[0:6]
del factor1[0:6]
del factor2[0:6]
del factor3[0:6]
del factor4[0:6]
del factor5[0:6]

state1=0
state2=0
state3=0
state4=0
state5=0
state6=0
state7=0
state8=0
state9=0
state10=0

index1=0
index2=0
index3=0
index4=0
index5=0
index6=0
index7=0
index8=0
index9=0
index10=0

mydict1={}
mydict2={}
mydict3={}
mydict4={}
mydict5={}

new_factor1=[]
for x in factor1:
    new_factor1.append(float(x))
    factor1Max=max(new_factor1)
    factor1Min=min(new_factor1)

    index1=new_factor1.index(factor1Max)
    index2=new_factor1.index(factor1Min)
    state1=states[index1]
    state2=states[index2]
    
new_factor2=[]
for x in factor2:
    new_factor2.append(float(x))
    factor2Max=max(new_factor2)
    factor2Min=min(new_factor2)

    index3=new_factor2.index(factor2Max)
    index4=new_factor2.index(factor2Min)
    state3=states[index3]
    state4=states[index4]
  
new_factor3=[]
for x in factor3:
    new_factor3.append(float(x))
    factor3Max=max(new_factor3)
    factor3Min=min(new_factor3)

    index5=new_factor3.index(factor3Max)
    index6=new_factor3.index(factor3Min)
    state5=states[index5]
    state6=states[index6]
    
new_factor4=[]
for x in factor4:
    new_factor4.append(x.replace("%", ""))
    factor4Max=max(new_factor4)
    factor4Min=min(new_factor4)

    index7=new_factor4.index(factor4Max)
    index8=new_factor4.index(factor4Min)
    state7=states[index7]
    state8=states[index8]
    
new_factor5=[]
for x in factor5:
    new_factor5.append(x.replace("%", ""))
    factor5Max=max(new_factor5)
    factor5Min=min(new_factor5)

    index9=new_factor5.index(factor5Max)
    index10=new_factor5.index(factor5Min)
    state9=states[index9]
    state10=states[index10]

print ("The Max value of ", title1, "is ", factor1Max," from", state1, ".")
print ("The Min value of ", title1, "is ", factor1Min," from", state2, ".")

print ("The Max value of ", title2, "is ", factor2Max," from", state3, ".")
print ("The Min value of ", title2, "is ", factor2Min," from", state4, ".")

print ("The Max value of ", title3, "is ", factor3Max," from", state5, ".")
print ("The Min value of ", title3, "is ", factor3Min," from", state6, ".")

print ("The Max value of ", title4, "is ", factor4Max, "% from", state7, ".")
print ("The Min value of ", title4, "is ", factor4Min, "% from", state8, ".")

print ("The Max value of ", title5, "is ", factor5Max, "% from", state9, ".")
print ("The Min value of ", title5, "is ", factor5Min, "% from", state10, ".")



    


