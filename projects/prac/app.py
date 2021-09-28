from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/mypage')
def mypage():
   return 'my page 입니다!'

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') #클라이언트가 준, title_give로 가지고 온 값 찍어봐봐.
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

   #아홉줄만으로도 서버를 만듦