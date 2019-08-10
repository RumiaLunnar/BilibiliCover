from flask import Flask
from flask import render_template,request
import json
import requests
import urllib3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name=index)


@app.route('/get_cover', methods=['POST', 'GET'])
def get_cover():
    aid = request.values.get('aid')
    url = 'https://api.bilibili.com/x/web-interface/view?aid=' + aid
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Referer':'https://www.bilbili.com'
        }
    urllib3.disable_warnings()
    response = requests.get(url,headers=headers,verify=False).json()
    code = response['code']
    if code == 0:
        data = response['data']
        pic = data['pic']
        return pic
    else:
        return ('error message:',response['message'])


if __name__ == '__main__':
    app.debug = True
    app.run()