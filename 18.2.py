from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
	return 'hello,word'#不知道什么原因，好像不能运行

