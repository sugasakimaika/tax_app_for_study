from flask import Flask, jsonify, request

app = Flask(__name__)

# ここに問題と答えを定義
questions_answers = {
    # ... 問題と答えのデータ ...
}

@app.route('/get_question', methods=['GET'])
def get_question():
    # 問題を送るロジック
    pass

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    # ユーザーの回答を検証するロジック
    pass

if __name__ == '__main__':
    app.run(debug=True)
