from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)  # Menggunakan __name__

@app.route('/')
def home():
    return render_template('index.html')  # Menggunakan file index.html di folder templates

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return redirect(url_for('home'))  # Arahkan kembali ke form jika tidak ada data

if __name__ == '__main__':
    app.run(debug=True)
