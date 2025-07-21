# 사용자로부터 입력을 반복해서 받고,
# 입력한 내용을 그대로 출력하다가
# '!quit'을 입력하면 종료되는 프로그램

def main():
    while True:  # 무한 반복
        user_input = input("입력하세요 (종료하려면 !quit 입력): ")

        if user_input == "!quit":
            print("프로그램을 종료합니다.")
            break  # 반복문을 빠져나가며 종료

        print("입력한 내용:", user_input)

if __name__ == "__main__":
    main()

