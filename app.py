
# Fully expanded app.py for .pyramid with deep branching story

from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/twilio-webhook", methods=['POST'])
def twilio_webhook():
    response = VoiceResponse()

    response.say("Welcome to Valley Mutant. The payphone rings. You have three choices.")
    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to answer it.")
    gather.say("Press 2 to ignore it and walk downtown.")
    gather.say("Press 3 to head toward the abandoned mall.")

    return str(response)

@app.route("/game-choice", methods=['POST'])
def game_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("You answer the payphone. A distorted voice whispers, 'You're late. The red door is moving.'")
        gather = response.gather(numDigits=1, action="/payphone-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to ask where the door is.")
        gather.say("Press 2 to hang up.")
        gather.say("Press 3 to ask who is speaking.")
    elif digits == "2":
        response.say("You walk downtown. The streetlights flicker. A stray cat watches you.")
        gather = response.gather(numDigits=1, action="/cat-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to pet the cat.")
        gather.say("Press 2 to ignore it and keep walking.")
        gather.say("Press 3 to follow it.")
    elif digits == "3":
        response.say("You approach the abandoned mall. It looks... open. But it shouldnâ€™t be.")
        gather = response.gather(numDigits=1, action="/mall-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to enter through the front.")
        gather.say("Press 2 to sneak into the back.")
        gather.say("Press 3 to search for another way in.")
    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/payphone-choice", methods=['POST'])
def payphone_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("The voice chuckles. 'Find the mural in Oak Street Alley. Look away. Then look again.'")
        response.say("The call ends. A red flyer is stuck to the payphone.")
    elif digits == "2":
        response.say("You hang up. The payphone rings again. This time, the ring sounds... off.")
    elif digits == "3":
        response.say("The voice pauses. 'You already know me. Don't you remember?'")
        response.say("The call disconnects. The street feels quieter than before.")
    else:
        response.say("Invalid choice. Returning to main menu.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/cat-choice", methods=['POST'])
def cat_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("You pet the cat. It purrs, then spits out a small key. It has a logo for Metrocenter Mall.")
        response.say("You donâ€™t know why, but you pocket it.")
    elif digits == "2":
        response.say("You ignore the cat. It watches you as you walk. When you glance back, itâ€™s gone.")
    elif digits == "3":
        response.say("You follow the cat into an alley. It stops in front of a payphone with no cord.")
        response.say("The payphone starts ringing.")
    else:
        response.say("Invalid choice. Returning to main menu.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/mall-choice", methods=['POST'])
def mall_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("You walk through the front doors. The speakers hum. A voice announces, 'Attention shoppers: Prepare for inventory check.'")
    elif digits == "2":
        response.say("You sneak in through the back entrance. A janitor stands there, motionless, watching.")
    elif digits == "3":
        response.say("You search for another way in. A service door is open just a crack.")
        response.say("Inside, faint music plays from unseen speakers. The escalators move, but there's no power.")
    else:
        response.say("Invalid choice. Returning to main menu.")
        response.redirect("/twilio-webhook")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
