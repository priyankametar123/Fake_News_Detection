from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("logistic_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['news']
        prediction = model.predict([text])[0]
        label = "Real News" if prediction == 1 else "Fake News"
        return render_template('index.html', prediction=label)

if __name__ == '__main__':
    app.run(debug=True)
