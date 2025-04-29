from flask import Flask, request

app = Flask(__name__)

@app.route('/calc')
def search():
    a = request.args.get('a')
    b = request.args.get('b')
    op = request.args.get('op')
    if a.isdigit() and b.isdigit():
        if op == "add":
            sum = int(a) + int(b)
            return f'Результаты вычисления: {sum}'
        elif op == "mult":
            sum = int(a) * int(b)
            return f'Результаты вычисления: {sum}'
        elif op == "diff":
            sum = int(a) / int(b)
            return f'Результаты вычисления: {sum}'
        elif op == "sub":
            sum = int(a) - int(b)
            return f'Результаты вычисления: {sum}'
        else:
            return 'Оператора не существует'
    else:
        return 'Неверные аргументы'

if __name__ == '__main__':
    app.run(debug=True)