import time

# 消費税法の穴埋め問題、答え、および関連する条文
questions_answers = {
    "消費税法において、課税事業者は年間の______を超える売上がある場合に、消費税の納税義務が生じます。": ("特定の金額", "第六条"),
    "消費税の課税対象となるのは、物品の販売やサービスの提供など、事業者による______です。": ("取引", "第三条"),
    "輸入される物品に対しても、消費税が課され、これを______消費税と呼びます。": ("輸入", "第十条"),
    "消費税の納税義務者は、定期的に______を提出し、消費税を納付しなければなりません。": ("申告書", "第二十一条"),
    "消費税の計算では、課税売上高から課税仕入高を差し引いた金額に対して、一定の______を乗じて消費税額を算出します。": ("税率", "第二十八条"),
    "消費税では、小規模事業者に対して特定の条件のもとで______が適用されることがあります。": ("免税措置", "第二十九条")
}

def play_game(questions_answers):
    correct_count = 0
    total_questions = len(questions_answers)

    for question, (correct_answer, article) in questions_answers.items():
        print("\n問題：", question)
        print("関連する条文：", article)
        start_time = time.time()
        user_answer = input("答えを入力してください: ")
        end_time = time.time()
        if user_answer.lower() == correct_answer.lower():
            correct_count += 1
            print(f"正解！所要時間: {end_time - start_time:.2f}秒")
        else:
            print(f"不正解。正しい答えは「{correct_answer}」で、関連する条文は「{article}」です。")

    print(f"\nゲーム終了！{total_questions}問中、{correct_count}問正解でした。")

# ゲームを開始する
play_game(questions_answers)
