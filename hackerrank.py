N=int(input('enter the no. of students'))
if N>=2 and N<=10:
    for i in range(N):
        report=[input('enter the name '),int(input('enter ')),int(input('enter')),int(input('enter'))]
else:
    print('Invalid input')
                
a=input('enter student name')
if a in report:
    sum1=0
    for i in report(1,len(report)):
        sum1=sum1+report[i]
average=sum1/2
print(average)

        
        
