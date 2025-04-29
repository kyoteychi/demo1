from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Генерируем список уникальных телефонных номеров
phone_numbers = [f"891382{str(i).zfill(5)}" for i in range(1000)]

@app.route('/')
def index():
    return render_template('index.html', phone_numbers=phone_numbers)

@app.route('/number/<number>')
def phone_number_detail(number):
    return render_template('detail.html', phone_number=number)

@app.route('/search', methods=['POST'])
def search():
    entered_number = request.form['phone_number']
    if entered_number in phone_numbers:
        return redirect(url_for('phone_number_detail', number=entered_number))
    else:
        return redirect(url_for('phone_number_detail', number=entered_number))

if __name__ == '__main__':
    app.run(debug=True)