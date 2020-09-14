import re
import os
import os.path
import matplotlib.pyplot as plt
import numpy as np
import glob

def trans(ss):
    r=ss/30
    return r

def open_file1(file):
    inputFile =('EDF_Data/'+ file+ '-H.txt')
    
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
    a=len(stage)
    del stage[a-1]
    a=len(sc)
    del sc[a-1]
    
    return stage,sc  


def open_file2(file):

    myFile = open('EDF_Data/'+file+'-P.txt','r')
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

    eeg_max=-10.0
    eeg_min=10.0
    eog_max=-10.0
    eog_min=10.0
    

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
        
        if float(eeg[i])>eeg_max :
            eeg_max=float(eeg[i])
        if float(eeg[i])<eeg_min :
            eeg_min=float(eeg[i])
        if float(eog[i])>eog_max :
            eog_max=float(eog[i])
        if float(eog[i])<eog_min :
            eog_min=float(eog[i])
        
    eeg_max = int(eeg_max)
    eeg_min = int(eeg_min)
    eog_max = int(eog_max)
    eog_min = int(eog_min)

    
    return date2,hour2,mi2,sec2,eeg2,eog2,eeg_max,eeg_min,eog_max,eog_min

def open_file3(file) :
    myFile = open('EDF_Data/'+file+'-M.txt','r')
    lines = myFile.readlines()
    n=len(lines)

    text=[]
    date=[] #날짜
    hour=[] #시간
    mi=[]   #분
    sec=[]  #초
    emg=[]
 
    emg2=[]
    emg_max=-10.0
    emg_min=10.0
    

    for line in lines :
        text =line.split()
        date.append(text[0]) 
        hour.append(text[1])
        mi.append(text[2])
        sec.append(text[3])
        emg.append(text[4])
        
        
    myFile.close()
    n=len(date)
    
    for i in range(1,n):
        emg2.append(emg[i])
        if float(emg[i])>emg_max :
            emg_max=float(emg[i])
        if float(emg[i])<emg_min :
            emg_min=float(emg[i])
            
    emg_max = int(emg_max)
    emg_min = int(emg_min)
    return emg2,emg_max,emg_min
    

def select(file):

    stage,epoch=open_file1(file)
    date,hour,mi,sec,eeg,eog,eeg_max,eeg_min,eog_max,eog_min=open_file2(file)
    emg,emg_max,emg_min=open_file3(file)
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
    eeg_max = str(eeg_max)
    eeg_min = str(eeg_min)
    eog_max = str(eog_max)
    eog_min = str(eog_min)
    emg_max = str(emg_max)
    emg_min = str(emg_min)
    
    if not os.path.exists('File_Data'):
            os.makedirs('File_Data')
            
    f=open('File_Data/'+file+'_data.txt','w')
    f.write(eeg_max+'\n')
    f.write(eeg_min+'\n')
    f.write(eog_max+'\n')
    f.write(eog_min+'\n')
    f.write(emg_max+'\n')
    f.write(emg_min)

    f.close()
    
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
            if stage[i] == 'R' :
                    if not os.path.exists('R'):
                        os.makedirs('R')
                    if not os.path.exists('R/R_data'):
                        os.makedirs('R/R_data')
                    copy=open('R/R_data/'+file+'_%d.txt'%count_r,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=3000
                    end+=3000
                    count_r+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == 'N' :
                        start+=3000
                        end+=3000
                        data=[]
                        
    start=0
    end=30
    data=[]
    count_w=1
    count_o=1
    count_t=1
    count_tr=1
    count_f=1
    count_r=1
    a=1
    
    for i in range(0,count):
        n=epoch[i]
        for j in range(0,n):#한 스테이지당 횟수(30초단위)
            for k in range(start,end):
                 data.append(emg[k])   
            
            if stage[i] == 'W' :
                    if not os.path.exists('W'):
                        os.makedirs('W')
                    if not os.path.exists('W/W_data'):
                        os.makedirs('W/W_data')
                    copy=open('W/W_data/'+file+'_emg_%d.txt'%count_w,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=30
                    end+=30
                    count_w+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '1' :
                    if not os.path.exists('1'):
                        os.makedirs('1')
                    if not os.path.exists('1/1_data'):
                        os.makedirs('1/1_data')
                    copy=open('1/1_data/'+file+'_emg_%d.txt'%count_o,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=30
                    end+=30
                    count_o+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '2' :
                    if not os.path.exists('2'):
                        os.makedirs('2')
                    if not os.path.exists('2/2_data'):
                        os.makedirs('2/2_data')
                    copy=open('2/2_data/'+file+'_emg_%d.txt'%count_t,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=30
                    end+=30
                    count_t+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '3' :
                    if not os.path.exists('3'):
                        os.makedirs('3')
                    if not os.path.exists('3/3_data'):
                        os.makedirs('3/3_data')
                    copy=open('3/3_data/'+file+'_emg_%d.txt'%count_tr,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=30
                    end+=30
                    count_tr+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == '4' :
                    if not os.path.exists('4'):
                        os.makedirs('4')
                    if not os.path.exists('4/4_data'):
                        os.makedirs('4/4_data')
                    copy=open('4/4_data/'+file+'_emg_%d.txt'%count_f,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=30
                    end+=30
                    count_f+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == 'R' :
                    if not os.path.exists('R'):
                        os.makedirs('R')
                    if not os.path.exists('R/R_data'):
                        os.makedirs('R/R_data')
                    copy=open('R/R_data/'+file+'_emg_%d.txt'%count_r,'w')
                    copy.writelines('\n'.join(data))
                    copy.close()
                    start+=30
                    end+=30
                    count_r+=1 
                    data=[]
                    print("%d개 생성완료 " % a)
                    a+=1
            if stage[i] == 'N' :
                        start+=30
                        end+=30
                        data=[]
    print("작업 완료\n")
    
def open_file4(file):
    myFile = open(file,'r')
    lines = myFile.readlines()
    n=len(lines)

    text=[]
    date=[] 
    hour=[] 
    mi=[]   
    sec=[]
    eeg=[]
    eog=[]
   

    for line in lines :
        text =line.split()
        date.append(text[0]) 
        hour.append(text[1])
        mi.append(text[2])
        sec.append(text[3])
        eeg.append(text[4])
        eog.append(text[5])
        

    return date,hour,mi,sec,eeg,eog

def draw_eeg(file,file_name,thick,c,a):
    date,hour,mi,sec,eeg,eog=open_file4(file)
    x=[]
    y=[]
    z=[]
    fmax = 100      # 주파수 샘플링
    dt = 1/fmax     # dt
    N  = 3000    # 신호 길이
    
    for i in range(0,3000):
        x.append(i)
        y.append(eeg[i])
        z.append(eog[i])
       
    y_a=[float(num) for num in y]
    

    plt.plot(x,y_a,c,linewidth=thick)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
    
    if file[0] == 'W' :
                    if not os.path.exists('W'):
                        os.makedirs('W')
                    if not os.path.exists('W/W_eeg'):
                        os.makedirs('W/W_eeg')
                    plt.savefig('W/W_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '1' :
                    if not os.path.exists('1'):
                        os.makedirs('1')
                    if not os.path.exists('1/1_eeg'):
                        os.makedirs('1/1_eeg')
                    plt.savefig('1/1_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '2' :
                   
                    if not os.path.exists('2/2_eeg'):
                        os.makedirs('2/2_eeg')
                    plt.savefig('2/2_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '3' :
                    
                    if not os.path.exists('3/3_eeg'):
                        os.makedirs('3/3_eeg')
                    plt.savefig('3/3_eeg/'+file_name+'.png',format='png')
                    plt.clf() 
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '4' :
                    
                    if not os.path.exists('4/4_eeg'):
                        os.makedirs('4/4_eeg')
                    plt.savefig('4/4_eeg/'+file_name+'.png',format='png')
                    plt.clf() 
                    print("%d개 생성완료 " % a)
                    
    if file[0] == 'R' :
                   
                    if not os.path.exists('R/R_eeg'):
                        os.makedirs('R/R_eeg')
                    plt.savefig('R/R_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
                    
           

def draw_eog() :
                    
    for i in range(0,30):
        x.append(i)
        w.append(dmg[i])
        
    w_a=[float(num) for num in w]
    z_a=[float(num) for num in z]
 
def drawing():
    plt.subplot(321)
    plt.plot(x,y_a,linewidth=1)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
    
    plt.subplot(322)
    plt.plot(x,z_a,linewidth=1)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)

    plt.subplot(323)
    plt.plot(x,w_a,linewidth=1)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)

    
    xf = np.fft.fft(y_a)*dt
    plt.subplot(324)
    plt.plot(f[0:int(N/2+1)],np.abs(xf[0:int(N/2+1)]))
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.xlabel('frequency(Hz)'); plt.ylabel('abs(xf)'); plt.grid()
    plt.tight_layout() 

    xf = np.fft.fft(z_a)*dt
    plt.subplot(325)
    plt.plot(f[0:int(N/2+1)],np.abs(xf[0:int(N/2+1)]))
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.xlabel('frequency(Hz)'); plt.ylabel('abs(xf)'); plt.grid()
    plt.tight_layout()
 
    xf = np.fft.fft(w_a)*dt
    plt.subplot(326)
    plt.plot(f[0:int(N/2+1)],np.abs(xf[0:int(N/2+1)]))
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.xlabel('frequency(Hz)'); plt.ylabel('abs(xf)'); plt.grid()
    plt.tight_layout()
    plt.show()
    
def draw_data(input_data,dir_name):

     x=[]
     y=[]
     count=0
     for i in glob.glob(dir_name+input_data+'_*'):
          x.append(i)
     a=len(x)    
     for i in range (0,a):
         x[i]=x[i].replace("\\","/")
    
     thick=1
     k='k'   
     path = dir_name
     file_list = os.listdir(path)
     n=len(file_list)
     for i in range(0,n):
          count+=1
          file_name=file_list[i]
          a=len(file_name)
          file_name=(file_name[0:a-4])
          if file_name[:2]==(input_data+'_'):
               y.append(file_name)
               draw_eeg(x[i],file_name,thick,k,count)
               
     return count
    
def menu():
    print("■■■■■■■■■■■■■")
    print("■  1.시           작   ■")
    print("■                      ■")
    print("■  2.프 로 그 램 종료  ■")
    print("■■■■■■■■■■■■■")

def draw_menu():
    print("■■■■■■■■■■■■■")
    print("■  1.시간영역  데이터  ■")
    print("■                      ■")
    print("■  2.주파수영역데이터  ■")
    print("■                      ■")
    print("■  3.프 로 그 램 종료  ■")
    print("■■■■■■■■■■■■■")

