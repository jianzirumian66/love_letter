import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def love_letter():
    return render_template('index.html')

if __name__ == '__main__':
    # 读取云端分配的端口，如果没有就默认用 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)