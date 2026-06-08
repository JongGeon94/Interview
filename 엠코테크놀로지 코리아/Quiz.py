import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_interactive_quiz():
    # 5번부터 24번까지 총 20개의 모든 문항 데이터 정의
    questions = [
        {
            "num": 1,
            "type": "text",
            "q": "어느 지도에서 1cm는 실제 거리로는 4KM가 된다.\n지도상에서 5cm는 실제 거리로는 얼마인가?\n(입력 예시: 20KM)",
            "check": lambda ans: ans.strip().upper() == "20KM",
            "info": "1cm = 4KM 이므로, 5cm는 4KM x 5 = 20KM가 됩니다."
        },
        {
            "num": 2,
            "type": "text",
            "q": "조립(어셈블리)를 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() == "assembly",
            "info": "정답은 'assembly'입니다."
        },
        {
            "num": 3,
            "type": "choice",
            "q": "15 ( ) (9-6) + 4x3 = 17 에서 괄호 안에 들어갈 적절한 기호는?",
            "options": ["① +", "② -", "③ ÷", "④ x"],
            "correct_idx": 3,
            "info": "15 ÷ (3) + 12 = 5 + 12 = 17이 되므로 나눗셈(③) 기호가 알맞습니다."
        },
        {
            "num": 4,
            "type": "choice",
            "q": "짝지어진 두 단어의 관계가 다른 것을 고르시오.",
            "options": ["① Strong – Weak", "② Huge – Tiny", "③ Blank – Fix", "④ Slow – Fast"],
            "correct_idx": 3,
            "info": "다른 쌍들은 모두 반의어 관계이지만, Blank(비어있는)와 Fix(고치다)는 반의어가 아닙니다."
        },
        {
            "num": 5,
            "type": "text",
            "q": "정리하다(어레인지)를 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() == "arrange",
            "info": "정답은 'arrange'입니다."
        },
        {
            "num": 6,
            "type": "text",
            "q": "[계산 문제] 5 x 6 - 12 ÷ 3 을 계산하시오.",
            "check": lambda ans: ans.strip() == "26",
            "info": "곱셈과 나눗셈을 먼저 계산하면 30 - 4 = 26이 됩니다."
        },
        {
            "num": 7,
            "type": "text",
            "q": "73.862 + 33.529 - 325.793 을 계산하시오.\n(음수인 경우 마이너스 기호를 붙여 소수 3자리까지 정확히 입력)",
            "check": lambda ans: ans.strip() == "-218.402",
            "info": "73.862 + 33.529 = 107.391이며, 107.391 - 325.793 = -218.402 입니다."
        },
        {
            "num": 8,
            "type": "text",
            "q": "전기(일렉트릭)을 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() in ["electric", "electricity"],
            "info": "정답은 'electric' 또는 'electricity'입니다."
        },
        {
            "num": 9,
            "type": "text",
            "q": "4 x 27 - 3 x 2 ÷ 3 을 계산하시오.",
            "check": lambda ans: ans.strip() == "106",
            "info": "4 x 27 = 108 이고 3 x 2 ÷ 3 = 2 이므로, 108 - 2 = 106 입니다."
        },
        {
            "num": 10,
            "type": "text",
            "q": "품질(퀄리티)를 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() == "quality",
            "info": "정답은 'quality'입니다."
        },
        {
            "num": 11,
            "type": "choice",
            "q": "대화의 빈칸에 들어갈 말로 알맞은 것을 고르시오.\n\nA : I went fishing in the East Sea.\nB : Really? ____________?\nA : It was so much fun!",
            "options": ["① How was it", "② Where was it", "③ When did you go", "④ Who went with you"],
            "correct_idx": 1,
            "info": "'정말 재미있었어!'라는 대답으로 보아 상태나 소감을 묻는 ①번이 가장 자연스럽습니다."
        },
        {
            "num": 12,
            "type": "choice",
            "q": "수빈이와 어머니의 나이차는 32이다. 그리고 어머니의 나이는 수빈이의 나이의 3배라면 현재 수빈이의 나이는?",
            "options": ["① 13", "② 18", "③ 14", "④ 16"],
            "correct_idx": 4,
            "info": "어머니 나이(3x) - 수빈이 나(x) = 32 -> 2x = 32이므로 수빈이는 16세(④번)입니다."
        },
        {
            "num": 13,
            "type": "text",
            "q": "오류(에러)를 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() == "error",
            "info": "정답은 'error'입니다."
        },
        {
            "num": 14,
            "type": "choice",
            "q": "다음 중 제시된 단어와 같거나 비슷한 뜻을 가진 것을 고르시오.\n\n[ region ]",
            "options": ["① area", "② surface", "③ situation", "④ union"],
            "correct_idx": 1,
            "info": "region은 '지역, 구역'을 뜻하므로 ①번 area가 유의어로 알맞습니다."
        },
        {
            "num": 15,
            "type": "text",
            "q": "12 - 4 x 8 + 32 ÷ 4 를 계산하시오.",
            "check": lambda ans: ans.strip() == "-12",
            "info": "곱셈과 나눗셈을 먼저 하면 12 - 32 + 8이 되므로 계산 결과는 -12입니다."
        },
        {
            "num": 16,
            "type": "text",
            "q": "생산(프로덕션)을 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() == "production",
            "info": "정답은 'production'입니다."
        },
        {
            "num": 17,
            "type": "text",
            "q": "영수는 100M를 뛰는데 17초가 걸린다. 희원이는 50M를 뛰는데 11초가 걸린다.\n둘이 각각 150M를 나누어 뛰었을 때(총 300M), 걸리는 총 시간은 몇 초인가?\n(숫자만 입력하세요. 예: 58.5)",
            "check": lambda ans: ans.strip() == "58.5",
            "info": "영수(150M) = 25.5초, 희원(150M) = 33초이므로 둘을 더하면 58.5초가 됩니다."
        },
        {
            "num": 18,
            "type": "text",
            "q": "[ {20 - (4x3) x 4} ÷ 2 ] + 3 을 계산하시오.",
            "check": lambda ans: ans.strip() == "-11",
            "info": "괄호 안쪽부터 풀면 [ {20 - 48} ÷ 2 ] + 3 = [ -28 ÷ 2 ] + 3 = -14 + 3 = -11 입니다."
        },
        {
            "num": 19,
            "type": "text",
            "q": "기술(테크놀로지)를 영어로 쓰시오. (소문자로 입력)",
            "check": lambda ans: ans.strip().lower() == "technology",
            "info": "정답은 'technology'입니다."
        },
        {
            "num": 20,
            "type": "choice",
            "q": "[분수식 계산] (8 ÷ 2) - 2 를 계산하고 알맞은 보기를 고르시오.",
            "options": ["① 3", "② 1", "③ 1/2", "④ 2"],
            "correct_idx": 4,
            "info": "4 - 2 = 2이므로 정답 보기 번호는 ④번입니다."
        }
    ]

    clear_screen()
    print("==================================================")
    print(" 🎯 고등학교 기초 수학 및 어휘 평가 종합 시뮬레이터")
    print("==================================================")
    print(f" 원본 시험지 5번~24번 전체 문항(총 {len(questions)}문제)이 세팅되었습니다.")
    print(" 준비가 완료되었다면 [Enter]를 누르세요.")
    input()

    score = 0
    total_questions = len(questions)

    for idx, item in enumerate(questions, 1):
        clear_screen()
        print(f"[{idx}/{total_questions}단계] 문제 {item['num']}번 (배점: 5점)")
        print("-" * 50)
        print(item['q'])
        print("-" * 50)

        if item['type'] == "choice":
            for opt in item['options']:
                print(opt)
            print("-" * 50)
            user_input = input("정답 번호 숫자를 입력하세요 (1~4): ")
            is_correct = user_input.strip() == str(item['correct_idx'])
        else:
            user_input = input("정답을 입력하세요: ")
            is_correct = item['check'](user_input)

        print("\n" + "=" * 50)
        if is_correct:
            print("⭕ 정답입니다! (+5점)")
            score += 5
        else:
            print("❌ 틀렸습니다.")
        print(f"💡 해설: {item['info']}")
        print("=" * 50)
        
        print("\n다음 문제로 넘어가려면 [Enter]를 누르세요...")
        input()

    clear_screen()
    print("==================================================")
    print(" 🎉 모든 시험 문항이 종료되었습니다!")
    print("==================================================")
    print(f" ㆍ 최종 획득 점수: {score}점 / {total_questions * 5}점 만점")
    print(f" ㆍ 맞힌 문항 수  : {score // 5}개 / {total_questions}개")
    print("==================================================")
    print(" 고생하셨습니다. 창을 닫으려면 [Enter]를 누르세요.")
    input()

if __name__ == "__main__":
    run_interactive_quiz()