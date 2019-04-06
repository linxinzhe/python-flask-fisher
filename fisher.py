from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

__author__ = 'linxinzhe'


@app.route('/hello/')  # 唯一url原则，带/可以兼容不带/情况
def hello():
    return 'Hello World!'


# app.add_url_rule('/hello/', view_func=hello)  # 另一个注册路由方式

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
