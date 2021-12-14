# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:17:49 2021

@author: 葉詠馨
"""

n=0
a1=[]
with open('IMDB-Movie-Data.csv','r',encoding='utf-8') as data:
#開啟檔案
    while n<1001:
        #把檔案每筆資料讀取並存進一個list內
        x=data.readline()
        n+=1
        x=x.split(',')
        a1.append(x)
    a1.remove(a1[0])
    #移除掉第一列的說明列
#第一小題
r1=[]
r2=[]
for i in a1:
    if i[5]=='2016':
        r1.append(i[7])
        r1.sort()
        for j in r1:
            if j==i[7]:
                r2.append(i[1])
print('(1)Top-3 movies with the highest ratings in 2016: ',r2[0],r2[1],r2[2],sep=',')

#第二小題
r3=[]
r4=[]
r5=[]
r6=[]
r7=[]
s1=()
for i in a1:
   x=i[4].split('|')   
   r3.append(x)
for j in r3:
       for k in j:
           r4.append(k)
           s1=set(r4)
for l in s1:
    n=r4.count(l)
    if k==l:
        sum1=0
        z=float(i[9])
        sum1+=z
        r5.append(sum1)
for m in r5:
    avg=m/n
    r6.append(avg)
    if avg==max(r6):
        r7.append(l)
print('(2)The actor generating the highest average revenue:',r7)
               
#第三小題
avg=[]
sum=0
for i in a1:
    if 'Emma Watson' in i[4] :
        avg.append(i)
        for i in avg:
            x=float(i[7])
            sum+=x
        n=len(avg)
print('(3)The average rating of Emma Watson’s movies:',sum/n)

#第四小題
r7=[]
r8=[]
s2=()
for i in a1:
    x=i[3].split('|')
    r7.append(x)
for j in r7:
    for k in j:
        r8.append(k)
        s2=set(r8)#不重複的導演名單
r9=[]
r10=[]
r13=[]
for i in a1:
    for l in s2:
        if l in i[3]:
            r9.append(i[4])
            x=len(r9)
            r10.append(x)
            y=sorted(r10,reverse=True)
for k in r10:
        if k==y[0]:        
            r13.append(l)
        elif k==y[1]:
           r13.append(l)
        elif k==y[2]:
            r13.append(l)
print('(4)Top-3 directors who collaborate with the most actors:',r13)        
#第五小題
r11=[]
r12=[]
s2=()
for i in a1:
    x=i[4].split('|')
    r11.append(x)
for j in r11:
    for k in j:
        r12.append(k)
        s2=set(r12)#不重複的演員名單
r13=[]
r14=[]
for i in a1:
    for l in s2:
        if l in i[4]:
            r13.append(i[3])
            x=len(r13)
            r14.append(x)
            y=sorted(r14,reverse=True)
print('(5)Top-3 directors who collaborate with the most actors:')
for k in r14:
        if k==y[0]:        
            print(l)
        elif k==y[1]:
            print(l)

    

    
        
    

   
    
        
        
        
