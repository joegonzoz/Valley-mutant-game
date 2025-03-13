# Fully expanded app.py for Valley Mutant with deep branching story, more NPCs, and dice rolls

from flask import Flask, request
import random
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/twilio-webhook", methods=['POST'])
def twilio_webhook():
    response = VoiceResponse()

    response.say("Welcome to Valley Mutant. The city hums with something unseen. You have choices to make.")
    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to answer the payphone.")
    gather.say("Press 2 to follow a stray cat downtown.")
    gather.say("Press 3 to enter the abandoned mall.")
    gather.say("Press 4 to take the last train of the night.")
    gather.say("Press 5 to visit the firehouse-turned-Chick-fil-A.")

    return str(response)

@app.route("/game-choice", methods=['POST'])
def game_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("The payphone clicks. A distorted voice whispers, 'You are late. The red door is moving.'")
        gather = response.gather(numDigits=1, action="/payphone-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to ask where the door is.")
        gather.say("Press 2 to hang up.")
        gather.say("Press 3 to say nothing and listen.")
        gather.say("Press 4 to trace the call.")
    elif digits == "2":
        response.say("A stray cat watches you, waiting. It moves with intent.")
        gather = response.gather(numDigits=1, action="/cat-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to pet the cat.")
        gather.say("Press 2 to ignore it and keep walking.")
        gather.say("Press 3 to follow it.")
        gather.say("Press 4 to see where it leads.")
    elif digits == "3":
        response.say("The abandoned mall doors are slightly open, but no one should be inside.")
        gather = response.gather(numDigits=1, action="/mall-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to enter through the front.")
        gather.say("Press 2 to sneak into the back.")
        gather.say("Press 3 to check for another entrance.")
        gather.say("Press 4 to look for security footage.")
    elif digits == "4":
        response.say("The last train of the night pulls up, but the conductor isn’t human.")
        gather = response.gather(numDigits=1, action="/train-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to board the train.")
        gather.say("Press 2 to step back and watch.")
        gather.say("Press 3 to ask the conductor where it goes.")
        gather.say("Press 4 to check the schedule board.")
    elif digits == "5":
        response.say("You step inside the old firehouse. It smells of fryer grease and something older.")
        gather = response.gather(numDigits=1, action="/firehouse-choice", method="POST", barge_in=True, timeout=5)
        gather.say("Press 1 to order food.")
        gather.say("Press 2 to ask about the building’s history.")
        gather.say("Press 3 to look for signs of the past.")
        gather.say("Press 4 to check the locked door in the back.")
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
        response.redirect("/roll-dice")
    elif digits == "2":
        response.say("You hang up. The payphone rings again. This time, it sounds like it’s inside your head.")
    elif digits == "3":
        response.say("Silence stretches. Then, a different voice answers. 'You're not supposed to be here.'")
    elif digits == "4":
        response.say("Tracing the call... The signal leads underground.")
        response.redirect("/deep-mystery")
    else:
        response.say("Invalid choice. Returning to main menu.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/roll-dice", methods=['POST'])
def roll_dice():
    response = VoiceResponse()
    roll = random.randint(1, 6)
    response.say(f"You rolled a {roll}.")

    if roll > 3:
        response.say("The door in your mind unlocks. Something waits on the other side.")
        response.redirect("/deep-mystery")
    else:
        response.say("Something shifts in the world. You feel watched.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/deep-mystery", methods=['POST'])
def deep_mystery():
    response = VoiceResponse()
    response.say("You step off the train, but the station is too old. The sign flickers: 'Metrocenter, 1994'.")
    response.say("A stranger in a long coat hands you a cassette tape. He whispers, 'You’ll need this.'")
    response.redirect("/twilio-webhook")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
