from flask import Flask
from flask_cors import *
from flask import request, jsonify
import json

from mysqlConect import select

app = Flask(__name__)

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return '<h1>hello 阿辉</h1>'

@app.route('/search', methods = ["GET","POST"])   # GET 和 POST 都可以
def get_data():
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&age=20

    #可以通过 request 的 args 属性来获取参数
    name = request.args.get("name")
    print(name)
    
    # 经过处理之后得到要传回的数据
    res= select(name)
    ans = {
        'content':res,
        'status':200
        }
    ans = json.dumps(ans)
    
    # 将数据再次打包为 JSON 并传回
    
    return ans




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)