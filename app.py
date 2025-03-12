from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    
    # Correctly format the MP3 play command
    response.play("https://your-audio-host.com/vaporwave_intro.mp3")
    
    # Twilio speaks after playing audio
    response.say("Welcome to Valley Mutant. The payphone rings. You have three choices.")

    # Gather user input (1 digit)
    gather = Gather(input="dtmf", num_digits=1, action="/choice1")
    gather.say("Press 1 to answer it. Press 2 to ignore it.")

    response.append(gather)
    return str(response)  # Ensures Twilio receives valid TwiML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)