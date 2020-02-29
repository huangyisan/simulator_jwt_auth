import jwt
from sanic import Sanic
from sanic.response import json

import time
from sanic_cors import CORS

'''
/auth: 认证接口, success:{'code':200, 'info':'authSuccess'}, failed:{'code':401, 'info':'authFaildd'}
/check: token校验接口, success:{'code':200, 'info':'checkSuccess'}, failed:{'code':401, 'info':'checkFailed'}
/homeinfo: 主页信息, {'currentPage': 'homeinfo'}
'''

app = Sanic(__name__)
CORS(app, automatic_options=True)

# 只给login页面使用
@app.route("/tokencheck", methods=['GET', 'OPTIONS'])
def tokencheck(request):

    jwt_headers = {
        "alg": "HS256",
        "typ": "JWT"
    }

    token = request.headers.get('authorization')
    if token:
        token = token.split(' ')[-1]
        try:
            payload = jwt.decode(token, 'today', audience='yisan.com', headers=jwt_headers, algorithms=['HS256'])

            if payload:
                return json({'code': 200, 'info': 'checkSuccess'})
            return json({'code': 401, 'info': 'checkFailed'})
        except Exception as e:
            print(e)
            return json({'code': 401, 'info': 'checkFailed'})


def check(func):
    print('执行check')
    def wrapper(request):
        print('执行wrapper')
        jwt_headers = {
            "alg": "HS256",
            "typ": "JWT"
        }

        token = request.headers.get('authorization')
        if token:
            token = token.split(' ')[-1]
            try:
                payload = jwt.decode(token, 'today', audience='yisan.com', headers=jwt_headers, algorithms=['HS256'])
                if payload:
                    return func(request)
                return json({'code': 401, 'info': 'checkFailed'})
            except Exception as e:
                print(e)
                return json({'code': 401, 'info': 'checkFailed'})

            # 具体要请求的接口数据

        return json({'code': 405, 'info': '函数没有返回值'})
    return wrapper


@app.route("/auth", methods=['POST', 'OPTIONS'])
def auth(request):
    body = request.body
    body = eval(body.decode())

    username = body.get('username')
    password = body.get('password')

    jwt_headers = {
        "alg": "HS256",
        "typ": "JWT"
    }

    payload = {
        'iss': 'huangyisan',
        'sub': 'yisan',
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        'aud': 'yisan.com',
        'username': username
    }

    token = jwt.encode(payload, 'today', headers=jwt_headers, algorithm='HS256').decode()


    if username == 'admin' and password == 'admin':
        return json({'code': 200, 'info': 'authSuccess','access_token': token, 'account_id': username})
    else:
        return json({'code': 401, 'info': 'authFaildd'})


@app.route("/homeinfo", methods=['GET'])
@check
def homeinfo(request):
    print(111111111)
    return json({'currentPage': 'homeinfo'})

app.run(host="127.0.0.1", port=8000, debug=True)
