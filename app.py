from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Valley Mutant Twilio Game is Running!"

@app.route("/twilio-webhook", methods=['POST'])
def twilio_webhook():
    response = VoiceResponse()

    response.say("Welcome to Valley Mutant. The payphone rings. You have three choices.")
    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True)
    gather.say("Press 1 to answer it.")
    gather.say("Press 2 to ignore it and walk downtown.")
    gather.say("Press 3 to head toward the abandoned mall.")

    return str(response)

@app.route("/game-choice", methods=['POST'])
def game_choice():
    digits = request.form.get("Digits")
    response = VoiceResponse()

    if digits == "1":
        response.say("You answer the payphone. A voice whispers, You are late. The red door is moving.")
        gather = response.gather(numDigits=1, action="/payphone-choice", method="POST", barge_in=True)
        gather.say("Press 1 to ask where the door is.")
        gather.say("Press 2 to hang up.")

    elif digits == "2":
        response.say("You walk downtown. A stray cat follows you. It meows like it knows you.")
        gather = response.gather(numDigits=1, action="/cat-choice", method="POST", barge_in=True)
        gather.say("Press 1 to pet the cat.")
        gather.say("Press 2 to ignore it and keep walking.")

    elif digits == "3":
        response.say("You head toward the abandoned mall. The front doors are unlocked, even though the mall has been closed for years.")
        gather = response.gather(numDigits=1, action="/mall-choice", method="POST", barge_in=True)
        gather.say("Press 1 to enter through the front.")
        gather.say("Press 2 to sneak into the back.")

    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/payphone-choice", methods=['POST'])
def payphone_choice():
    digits = request.form.get("Digits")
    response = VoiceResponse()

    if digits == "1":
        response.say("The voice chuckles. The red door does not wait. Find the mural in Oak Street Alley. Look away. Then look again.")
        response.say("The call ends. You feel like something is watching you.")
    elif digits == "2":
        response.say("You hang up. The payphone rings again. This time, it feels personal.")

    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True)
    gather.say("Press 1 to return to downtown.")
    gather.say("Press 2 to walk toward the mall.")

    return str(response)

@app.route("/cat-choice", methods=['POST'])
def cat_choice():
    digits = request.form.get("Digits")
    response = VoiceResponse()

    if digits == "1":
        response.say("You pet the cat. It purrs, then spits out a small key. It has a logo for Metrocenter Mall.")
        response.say("This might be useful later.")
    elif digits == "2":
        response.say("You ignore the cat. It follows you for a while, then disappears.")

    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True)
    gather.say("Press 1 to check out the alley murals.")
    gather.say("Press 2 to continue toward the mall.")

    return str(response)

@app.route("/mall-choice", methods=['POST'])
def mall_choice():
    digits = request.form.get("Digits")
    response = VoiceResponse()

    if digits == "1":
        response.say("You walk through the front doors. A security announcement plays. Attention shoppers, todayâ€™s special is... you. Run.")
    elif digits == "2":
        response.say("You sneak into the back entrance. A janitor watches you. He doesnâ€™t blink.")

    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True)
    gather.say("Press 1 to move deeper into the mall.")
    gather.say("Press 2 to leave quickly.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)