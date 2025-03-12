
# Expanded app.py for .pyramid with more branches and interactions

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
        response.say("You answer the payphone. A voice whispers, 'You are late. The red door is moving.'")
        gather = response.gather(numDigits=1, action="/payphone-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to ask where the door is.")
        gather.say("Press 2 to hang up.")
        gather.say("Press 3 to ask who is speaking.")
    elif digits == "2":
        response.say("You walk downtown. A stray cat follows you. It meows like it knows you.")
        gather = response.gather(numDigits=1, action="/cat-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to pet the cat.")
        gather.say("Press 2 to ignore it and keep walking.")
        gather.say("Press 3 to follow it.")
    elif digits == "3":
        response.say("You head toward the abandoned mall. The front doors are unlocked, even though the mall has been closed for years.")
        gather = response.gather(numDigits=1, action="/mall-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to enter through the front.")
        gather.say("Press 2 to sneak into the back.")
        gather.say("Press 3 to look for another entrance.")
    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/payphone-choice", methods=['POST'])
def payphone_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("The voice chuckles. 'The red door does not wait. Find the mural in Oak Street Alley. Look away. Then look again.'")
        response.say("The call ends. You feel like something is watching you.")
    elif digits == "2":
        response.say("You hang up. The payphone rings again. This time, it feels personal.")
    elif digits == "3":
        response.say("The voice pauses. Then, with certainty, it says: 'You already know me.'")
        response.say("The call disconnects, but the feeling lingers.")
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
        response.say("This might be useful later.")
    elif digits == "2":
        response.say("You ignore the cat. It follows you for a while, then disappears.")
    elif digits == "3":
        response.say("You follow the cat. It walks with purpose, leading you into a dark alley.")
        response.say("A single payphone sits in the alley, ringing. But it has no cord.")
    else:
        response.say("Invalid choice. Returning to main menu.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/mall-choice", methods=['POST'])
def mall_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("You walk through the front doors. A security announcement plays. 'Attention shoppers, todayâ€™s special is... you. Run.'")
    elif digits == "2":
        response.say("You sneak into the back entrance. A janitor watches you. He doesnâ€™t blink.")
    elif digits == "3":
        response.say("You search for another way in. There is a service entrance, slightly open.")
        response.say("Inside, faint music plays from unseen speakers. The escalators hum, moving nowhere.")
    else:
        response.say("Invalid choice. Returning to main menu.")
        response.redirect("/twilio-webhook")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
