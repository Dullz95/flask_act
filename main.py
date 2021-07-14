from flask import Flask, render_template

app=Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('index.html',name=name)

@app.route('/times/<int:number>')
def looping(number):
    return render_template('loopy.html',number=number)

if __name__ == '__main__':
    app.debug=True
    app.run()