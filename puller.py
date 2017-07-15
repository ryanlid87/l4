import os, csv, struct
from datetime import date, timedelta

def check1(f,number):
        past = retry = fail = 0
        fil = open(f,"r+")
        d = fil.readlines()
        fil.seek(0)
        for i in d:
                if i[14] == "O":
                        past += 1
                elif i[14] == "N":
                        if recheck("//gpt/Data/GPT/L05_P12/L02/"+f[27:48],i[0:8]) == 1:
                                fail += 1
                        elif recheck("//gpt/Data/GPT/L05_P12/L02/"+f[27:48],i[0:8]) == 0:
                                fail += 0
                elif i[14] == "R":
                        retry +=1

        return past,retry,fail

def recheck(f,number):
        fil = open(f,"r+")
        d=fil.readlines()
        fil.seek(0)
        for i in d:
                if i.startswith(number):
                        if i[14] == "O":
                                return 0
                        elif i[14] == "N":
                                return 1
                        elif i[14] == "R":
                                return 0

def check2(f,number):
        past = retry = fail = 0
        fil = open(f,"r+")
        d = fil.readlines()
        fil.seek(0)
        for i in d:
                if i[14] == "O":
                        past += 1
                elif i[14] == "N":
                        if recheck("//gpt/Data/GPT/L05_P12/L01/"+f[27:48],i[0:8]) == 1:
                                fail += 1
                        elif recheck("//gpt/Data/GPT/L05_P12/L01/"+f[27:48],i[0:8]) == 0:
                                fail += 0
                elif i[14] == "R":
                        retry +=1

        return past,retry,fail


def test1(number):
        for x in os.listdir("//gpt/Data/GPT/L05_P12/L01/"):
                if x==number:
                        for file in os.listdir("//gpt/Data/GPT/L05_P12/L01/"+x):
                                if file.endswith("Index.Dat") and not file.startswith("All"):
                                        loc="//gpt/Data/GPT/L05_P12/L01/"+x+'/'+file
                                        return check1(loc,number)        

def test2(number):
        for x in os.listdir("//gpt/Data/GPT/L05_P12/L02/"):
                if x==number:
                        for file in os.listdir("//gpt/Data/GPT/L05_P12/L02/"+x):
                                if file.endswith("Index.Dat") and not file.startswith("All"):
                                        loc="//gpt/Data/GPT/L05_P12/L02/"+x+'/'+file
                                        return check2(loc,number)

def daterange(y1,m1,da1,y2,m2,da2):
        d1 = date(y1,m1,da1)  # start date
        d2 = date(y2,m2,da2)  # end date

        delta = d2 - d1         # timedelta     
        days = []
        for i in range(delta.days + 1):
            days.append(str(d1 + timedelta(days=i))[0:4] + str(d1 + timedelta(days=i))[5:7]+ str(d1 + timedelta(days=i))[8:10])
        return days
        
#show defects per day
def main():
        tot1 = ret1 = fai1 =tot2=ret2=fai2= 0
        start = raw_input("Enter start date 07/01/2017: ")
        end = raw_input("Enter end date 07/01/2017: ")
        y1 = int(start[6:10])
        m1 = int(start[0:2])
        da1 = int(start[3:5])
        y2 = int(end[6:10])
        m2 = int(end[0:2])
        da2 = int(end[3:5])
        
        days = daterange(y1,m1,da1,y2,m2,da2)
        for number in days:
                print number + " checked..."
                tester1 = test1(number)
                
                if tester1 == None:
                        tester1 = 0,0,0

                tester2 = test2(number) 
                if tester2 == None:
                        tester2 = 0,0,0
                tot1 += tester1[0]
                ret1 += tester1[1]
                fai1 += tester1[2]
                tot2 += tester2[0]
                ret2 += tester2[1]
                fai2 += tester2[2]
                
        print "Total parts ran on test1: " + str(tot1)
        print "Total parts retested on test1: " + str(ret1)
        print "Total parts failed on test1: " + str(fai1)
        
        print "Total parts ran on test2: " + str(tot2)
        print "Total parts retested on test2: " + str(ret2)
        print "Total parts failed on test2: " + str(fai2)

         
