from tool import*

while True :
     draw_menu()
     ch=int(input("\n입력 >> "))
     sum=0
     
     if ch == 1:      
          input_data=input("파일명 : ")
          turn=['1/1_data/','2/2_data/','3/3_data/','4/4_data/','W/W_data/','R/R_data/']     
          for i in range(0,len(turn)):
               a=draw_data_time(input_data,turn[i])
               print(turn[i][0]+" 스테이지의 EEG 이미지 %d개 생성완료"%a)
               sum+=a
          print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue
     
     if ch == 2:      
          input_data=input("파일명 : ")
          turn=['1/1_data/','2/2_data/','3/3_data/','4/4_data/','W/W_data/','R/R_data/']     
          for i in range(0,len(turn)):
               a=draw_data_eog(input_data,turn[i])
               print(turn[i][0]+" 스테이지의 EOG 이미지 %d개 생성완료"%a)
               sum+=a
          print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue 
               
     if ch == 3:       
          input_data=input("파일명 : ")  
          turn=['1/1_data/','2/2_data/','3/3_data/','4/4_data/','W/W_data/','R/R_data/']

          for i in range(0,len(turn)):
               b=draw_data_fft(input_data,turn[i])
               print(turn[i][0]+" 스테이지의 EEG FFT 이미지 %d개 생성완료"%b)
               sum+=b
          print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue
     
     if ch == 4:       
          input_data=input("파일명 : ")  
          turn=['1/1_data/','2/2_data/','3/3_data/','4/4_data/','W/W_data/','R/R_data/']

          for i in range(0,len(turn)):
               c=draw_data_eog_fft(input_data,turn[i])
               print(turn[i][0]+" 스테이지의 EOG FFT 이미지 %d개 생성완료"%c)
               sum+=c
          print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue
     
     if ch == 5:
          input_data=input("파일명 : ")  
          turn=['1/1_data_emg/','2/2_data_emg/','3/3_data_emg/','4/4_data_emg/','W/W_data_emg/','R/R_data_emg/']

          for i in range(0,len(turn)):
               d=draw_data_emg(input_data,turn[i])
               print(turn[i][0]+" 스테이지의 EMG 이미지 %d개 생성완료"%d)
               sum+=d
          print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue
     if ch == 6:
          input_data=input("파일명 : ")  
          turn=['1/1_data_emg/','2/2_data_emg/','3/3_data_emg/','4/4_data_emg/','W/W_data_emg/','R/R_data_emg/']

          for i in range(0,len(turn)):
               d=draw_data_emg_fft(input_data,turn[i])
               print(turn[i][0]+" 스테이지의 EMG 이미지 %d개 생성완료"%d)
               sum+=d
          print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue
     if ch == 7:
          break

          
               
          
