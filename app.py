from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

def features(url):
    return [len(url)]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        prediction = model.predict([features(url)])

        if prediction[0] == 1:
            result = "⚠️ PHISHING WEBSITE DETECTED"
        else:
            result = "✅ SAFE LEGITIMATE WEBSITE"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
