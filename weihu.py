from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/page', methods=['GET'])
@cross_origin()
def page():
    return '服务器维护中，预计2023.9.4 凌晨0：30恢复使用，感谢大家支持！'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765)