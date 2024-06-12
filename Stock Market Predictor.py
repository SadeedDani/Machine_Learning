from flask import Flask, render_template,request
import utils

app=Flask(__name__)

@app.route("/")

def home():
    print("Hello")
    return render_template("index.html")
@app.route('/predict',methods=["GET","POST"])



def predict():
    print("something")
    if request.method == "POST":
        print("Predict route triggered")
        Open = request.form.get('Open')
        High = request.form.get('High')
        Low = request.form.get('Low')
        Volume = request.form.get('Volume')
        print(f"Received data: Open={Open}, High={High}, Low={Low}, Volume={Volume}")

        prediction = utils.preprocess(Open, High, Low, Volume)
        print(f"prediction: {prediction}")

        return render_template("prediction.html", prediction=prediction)




if __name__ == "__main__":
    app.run(debug=True)