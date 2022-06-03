from flask import Flask, redirect, render_template, request
from backend import  predictor
import joblib

# Anwendung erstellen
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/entry')

@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Willkommen!')

@app.route('/predict', methods=['post'])
def predict():
    zip_ = request.form['zip']
    area = request.form['area']
    rooms = request.form['rooms']
    title = 'Hier kommt das Ergebnis...'
    result = str(predictor(zip_, area, rooms))
    return render_template('result.html', the_title=title, the_the_rooms=rooms, the_area=area,the_zip=zip_,the_prediction=result)


if __name__ == '__main__':
    app.run(debug=True)

