import time

class QuizGame:
    def __init__(self, questions_answers):
        self.questions_answers = questions_answers

    def play(self):
        correct_count = 0
        total_questions = len(self.questions_answers)# lenは長さ

        for question, correct_answer in self.questions_answers.items():# 問題をループさせている
            print("\n問題：", question)
            user_answer = input("答えを入力してください: ")
            start_time = time.time()
            end_time = time.time()
            if user_answer.lower() == correct_answer.lower():# 小文字にして、大文字小文字による答えの差異をなくす
                correct_count += 1
                print(f"正解！所要時間: {end_time - start_time:.2f}秒")
            else:
                print(f"不正解。正しい答えは「{correct_answer}」です。")

        print(f"\nゲーム終了！{total_questions}問中、{correct_count}問正解でした。")
