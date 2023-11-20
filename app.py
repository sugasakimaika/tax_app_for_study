from flask import Flask, request, render_template

womanmoneycareer = Flask(__name__)

@womanmoneycareer.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            user_input = float(request.form['user_input'])
            result = calculate_tax(user_input)
        except ValueError:
            result = "無効な入力です。数値を入力してください。"

    return render_template('index.html', result=result)

def calculate_tax(amount):
    tax_rate = 0.10  # 消費税率（10％）
    return amount * (1 + tax_rate)

if __name__ == '__main__':
    womanmoneycareer.run(debug=True)

