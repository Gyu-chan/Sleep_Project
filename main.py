from tool import*

def menu():
    print("■■■■■■■■■■■■■")
    print("■  1.시           작   ■")
    print("■                      ■")
    print("■  2.프 로 그 램 종료  ■")
    print("■■■■■■■■■■■■■")
    
while True :
    menu()
    ch=int(input("\n입력 >> "))

    if ch==1:
        file=input("파일이름 : ") ## 추후 넣는 방식 수정 (함수+스크립트형식)

        select(file)

        continue
    
    if ch==2:
        break

