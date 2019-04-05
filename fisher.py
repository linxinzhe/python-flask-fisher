from flask import Flask

app = Flask(__name__)

__author__='linxinzhe'

@app.route('/hello/')  # 唯一url原则，带/可以兼容不带/情况
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
