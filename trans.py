from flask import Flask, send_file

app = Flask(__name__)

@app.route('/lose')
def download_file():
    return send_file('list/lose_score.pickle')

@app.route('/win')
def download():
    return send_file('list/win_score.pickle')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765)