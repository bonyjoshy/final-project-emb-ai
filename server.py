"""This module recives the text from the HTML interface and runs 
Emotion Detection over it using emotion_detector_server() function"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_detector_server():
    """This function calls the emotion_detector() function and returns a formated string"""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    label_dominant_emotion = response.pop("dominant_emotion")
    key, value = response.popitem()
    last_emotion = {key: value}

    if label_dominant_emotion is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is \
    {str(response).replace('{', '').replace('}', '')} and \
    {str(last_emotion).replace('{', '').replace('}', '')}. \
    The dominant emotion is {label_dominant_emotion}."

@app.route("/")
def render_index_page():
    """This function render the main application page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
