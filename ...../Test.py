import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
from flask import Flask, render_template, request
from flask.json import jsonify
from ohno import god

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')

df = pd.read_excel('files/youtube_rank.xlsx')
df.head()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=["GET"])
def basic():

    if request.method =="GET":
        return render_template('index.html')

@app.route('/box', methods=["GET"])
def box():
    x = god()
    # print(x)
    return jsonify(x)



if __name__=="__main__":
    app.run(debug=True)
