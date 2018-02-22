f=open ('body.dat')
mydict={}
for line in f:
    age=line[110:114]
    weight=line[115:120]
    height=line[121:126]
    print(age,' ',weight,'  ',height)
    bmi=float(weight)*100*100/(float(height)*float(height))
    print(bmi)
    mydict[age]=bmi

print('mydict is:')
print(mydict.items())

sumX=0
for key in mydict:
    sumX=sumX+float(key)
print('sumX is:', sumX)

sumY=0
for y in mydict:
    sumY=sumY+float(mydict[y])
print('sumY is:', sumY)

sumXY=0
for x in mydict:
    sumXY=sumXY+ float(x)*float(mydict[x])
print('sumXY is:', sumXY)

sumX2=0
for x in mydict:
    sumX2=sumX2+ float(x)**2
print('sumX2 is:', sumX2)

sumY2=0
for y in mydict:
    sumY2=sumY2+float(mydict[y])**2

slope=((len(mydict)*sumXY)-(sumX*sumY))/((len(mydict)*sumX2)-(sumX**2))
print('The slope is:', slope)

intercept=(sumY-(slope*sumX))/len(mydict)
print('The intercept is:', intercept)

import math
corr=((len(mydict)*sumXY)-(sumX*sumY))/math.sqrt((len(mydict)*sumX2-(sumX**2))*(len(mydict)*sumY2-(sumY**2)))
print('The coorelation is:', corr)

    

    

    
    
