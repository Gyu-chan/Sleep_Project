from tool import*

while True :
     menu()
     ch=int(input("\n입력 >> "))
     draw_menu()
     if ch == 1:
          input_data=input("파일명 : ")
          input_op= int(input("옵션 선택 : "))

          turn=['1/1_data/','2/2_data/','3/3_data/','4/4_data/','W/W_data/','R/R_data/']

          if input_op == 1:
               for i in range(0,len(turn)-1):
                    a=draw_data(input_data,turn[i])
                    print(turn[i][0]+" 스테이지의 EEG 이미지 %d개 생성완료"%a)
                    sum+=a
               print(input_data+"의 이미지 총 %d개 생성하였습니다."%sum)
          continue
     if ch == 2:
          break
               
