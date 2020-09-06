import re
import os.path


def trans(ss):
    r=ss/30
    return r

def open_file1(file):
    inputFile = file+ '-H.txt'
    
    p = re.compile('[ ㄱ-ㅣ가-힣A-Za-z0-9]')
    f = open(inputFile, mode='r', encoding='euc-kr')
    s = f.read()
    f.close()
    s = p.findall(s)
    s = ''.join(s)
    f = open(inputFile, mode='w', encoding='euc-kr')
    f.write(s)
    f.close()

    myFile = open(inputFile,'r')
        
    lines = myFile.readlines()    
    text=[]
    for line in lines :
        text = line.split() 

    count=len(text)

    for i in range(count) :
        if 'Sleep' in text[i] :
            text[i]=text[i].replace('Sleep',"")
    count=len(text)
    for i in range(count) :
        if 'stage' in text[i] :
            text[i]=text[i].replace('stage',"")

    count=len(text)
    for i in range(count) :
        if '' in text[i] :
            text[i]=text[i].replace(''," ")              
    text = ' '.join(text).split()

    y=text[6][5:9]  # 년도
    m=text[10][2:4] # 월
    d=text[6][0:2]  # 일

    del text[:10]
    #date=int(text[0][6:12])
    del text[:13]

    count=len(text)
    if (text[count-1] != "1")|(text[count-1] != "2")|(text[count-1] != "3")|(text[count-1] != "4")|(text[count-1] != "W")|(text[count-1] != "R") :
        text.append("N")


    count=len(text)
    start=[]
    sc=[]
    end=[]
    stage=[]

    for i in range(0,count,3):
        start.append(text[i])
    for i in range(1,count,3):
        end.append(text[i])
    for i in range(2,count,3):
        stage.append(text[i])

    count=len(end)
    for i in range(count):
        sc.append(int(end[i]))

    for i in range(count) :
        sc[i]=int(trans(sc[i]))

    return stage,sc  


def open_file2(file):

    myFile = open(file+'-P.txt','r')
    lines = myFile.readlines()
    n=len(lines)

    text=[]
    date=[] #날짜
    hour=[] #시간
    mi=[]   #분
    sec=[]  #초
    eeg=[]
    eog=[]
    date2=[] 
    hour2=[] 
    mi2=[]   
    sec2=[]  
    eeg2=[]
    eog2=[]

    for line in lines :
        text =line.split()
        date.append(text[0]) 
        hour.append(text[1])
        mi.append(text[2])
        sec.append(text[3])
        eeg.append(text[4])
        eog.append(text[5])
        
    myFile.close()
    n=len(date)
    for i in range(1,n):
        date2.append(date[i])
        hour2.append(hour[i])
        mi2.append(mi[i])
        sec2.append(sec[i])
        eeg2.append(eeg[i])
        eog2.append(eog[i])
        
    return date2,hour2,mi2,sec2,eeg2,eog2


def select(file):

    stage,epoch=open_file1(file)
    date,hour,mi,sec,eeg,eog =open_file2(file)
    count=len(stage)
    start=0
    end=3000
    data=[]
    count_w=1
    count_o=1
    count_t=1
    count_tr=1
    count_f=1
    count_r=1
    a=1
    
    
    for i in range(0,count):#총 횟수
        n=epoch[i]
        for j in range(0,n):#한 스테이지당 횟수(30초단위)
            for k in range(start,end):
                 data.append(date[k]+"    "+hour[k]+"    "+mi[k]+"    "+sec[k]+"    "+eeg[k]+"    "+eog[k])   
            
            if stage[i] == 'W' :
                    if not os.path.exists('W'):
                        os.makedirs('W')
                    if not os.path.exists('W/W_data'):
                        os.makedirs('W/W_data')
                    copy=open('W/W_data/'+file+'_%d.txt'%count_w,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=3000
                    end+=3000
                    count_w+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '1' :
                    if not os.path.exists('1'):
                        os.makedirs('1')
                    if not os.path.exists('1/1_data'):
                        os.makedirs('1/1_data')
                    copy=open('1/1_data/'+file+'_%d.txt'%count_o,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=3000
                    end+=3000
                    count_o+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '2' :
                    if not os.path.exists('2'):
                        os.makedirs('2')
                    if not os.path.exists('2/2_data'):
                        os.makedirs('2/2_data')
                    copy=open('2/2_data/'+file+'_%d.txt'%count_t,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=3000
                    end+=3000
                    count_t+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '3' :
                    if not os.path.exists('3'):
                        os.makedirs('3')
                    if not os.path.exists('3/3_data'):
                        os.makedirs('3/3_data')
                    copy=open('3/3_data/'+file+'_%d.txt'%count_tr,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=3000
                    end+=3000
                    count_tr+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '4' :
                    if not os.path.exists('4'):
                        os.makedirs('4')
                    if not os.path.exists('4/4_data'):
                        os.makedirs('4/4_data')
                    copy=open('4/4_data/'+file+'_%d.txt'%count_f,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=3000
                    end+=3000
                    count_f+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == 'N' :
                        start+=3000
                        end+=3000
                        data=[]
        
    
