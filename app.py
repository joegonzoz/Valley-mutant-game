from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Valley Mutant Twilio Game is Running!"

@app.route("/twilio-webhook", methods=['POST'])
def twilio_webhook():
    response = VoiceResponse()
    
    # Game Introduction
    response.say("Welcome to Valley Mutant. Choose your adventure. Press 1 to explore downtown. Press 2 to investigate the abandoned mall.")
    response.gather(numDigits=1, action="/game-choice", method="POST")

    return str(response)

@app.route("/game-choice", methods=['POST'])
def game_choice():
    digits = request.form.get("Digits")
    response = VoiceResponse()
    
    roll = random.randint(1, 20)
    
    if digits == "1":
        response.say(f"You explore downtown. You roll a {roll}.")
        if roll >= 15:
            response.say("You find an ancient artifact glowing under a streetlight.")
        elif roll >= 10:
            response.say("You hear whispers from a nearby alley but see nothing.")
        else:
            response.say("A stray cat hisses at you. Something feels off.")
    elif digits == "2":
        response.say(f"You enter the abandoned mall. You roll a {roll}.")
        if roll >= 15:
            response.say("A hidden basement door creaks open before you.")
        elif roll >= 10:
            response.say("An old radio flickers on. It plays a distorted message.")
        else:
            response.say("A mannequin shifts in the dark. You are not alone.")
    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/twilio-webhook")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
    