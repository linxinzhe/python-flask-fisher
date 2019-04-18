from flask import make_response

from app import create_app

app = create_app()

__author__ = 'linxinzhe'


@app.route('/hello/')  # 唯一url原则，带/可以兼容不带/情况
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response


# app.add_url_rule('/hello/', view_func=hello)  # 另一个注册路由方式

if __name__ == '__main__':  # 生产环境是放在nginx+uwsgi里的，使用这行保证不会启动自带的服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
