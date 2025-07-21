import re  # re는 "정규 표현식"을 사용할 수 있게 해주는 모듈입니다. 특정한 패턴이 문자열에 있는지 검사할 때 사용합니다.

# 이 함수는 사용자가 입력한 비밀번호가 조건을 만족하는지 확인하고,
# 부족한 조건이 있으면 어떤 조건이 부족한지 알려줍니다.
def check_password(password: str) -> None:
    errors = []  # 조건을 만족하지 못한 항목들을 담을 빈 리스트를 준비합니다.

    # 1. 소문자가 들어 있는지 확인합니다. 예: a, b, c ...
    if not re.search(r'[a-z]', password):  
        errors.append("❌ 소문자가 최소 1개 포함되어야 합니다.")

    # 2. 대문자가 들어 있는지 확인합니다. 예: A, B, C ...
    if not re.search(r'[A-Z]', password):  
        errors.append("❌ 대문자가 최소 1개 포함되어야 합니다.")

    # 3. 숫자가 들어 있는지 확인합니다. 예: 0, 1, 2 ...
    if not re.search(r'\d', password):     
        errors.append("❌ 숫자가 최소 1개 포함되어야 합니다.")

    # 4. 특수문자가 들어 있는지 확인합니다. 예: !, @, #, $, %, 등등
    # 여기서는 영문자(a~z, A~Z)와 숫자(0~9)를 제외한 문자를 특수문자로 봅니다.
    if not re.search(r'[^a-zA-Z0-9]', password):  
        errors.append("❌ 특수문자(기호)가 최소 1개 포함되어야 합니다.")

    # 5. 비밀번호 길이가 8자 이상인지 확인합니다.
    if len(password) < 8:
        # 문자열의 길이를 구할 수 있는 len() 함수를 사용합니다.
        errors.append(f"❌ 비밀번호 길이는 최소 8자 이상이어야 합니다. (현재 {len(password)}자)")

    # 모든 조건을 통과한 경우
    if not errors:
        print("✅ 비밀번호가 모든 조건을 만족합니다.")
    else:
        # 하나라도 조건이 부족하면 그 내용을 출력합니다.
        print("⚠️ 비밀번호가 다음 조건을 만족하지 못했습니다:")
        for err in errors:
            print(err)  # 부족한 조건 하나씩 출력
            

# 사용자로부터 직접 비밀번호를 입력받습니다.
# input() 함수는 사용자로부터 키보드로 입력을 받을 수 있게 해줍니다.
user_password = input("비밀번호를 입력하세요: ")

# 위에서 정의한 함수를 호출해서 입력된 비밀번호를 검사합니다.
check_password(user_password)
