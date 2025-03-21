from flask import Flask
import json
from datetime import datetime

from database import  get_data_from_db
from predictor import predict_day, predict_monthly
from utils import day_on_month, next_day, past_day


app = Flask(__name__)


@app.route('/predict-tomorrow')
def predict_tomorrow():
    date = int(datetime.today().strftime('%Y%m%d'))


    df = get_data_from_db(past_day(date))
    daily_predict = json.dumps(predict_day(df))

    return daily_predict

@app.route('/predict-month')
def predict_next_month():
    date = datetime.today().strftime('%Y%m%d')

    df = get_data_from_db(next_day(date))
    monthly_predict = json.dumps(predict_monthly(df,day_on_month(date)))
    return monthly_predict

if __name__ == '__main__':
    app.run()
