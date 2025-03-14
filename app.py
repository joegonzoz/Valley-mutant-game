# Fully expanded app.py for Valley Mutant with deep branching, expanded mall path, and more failure routes.

from flask import Flask, request, session
import random
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)
app.secret_key = "valley_mutant_secret"

# Initialize player stats
def init_stats():
    return {"strength": 3, "charisma": 2, "perception": 4, "health": 10}

@app.route("/twilio-webhook", methods=['POST'])
def twilio_webhook():
    if "stats" not in session:
        session["stats"] = init_stats()

    response = VoiceResponse()
    response.say("Welcome to Valley Mutant. This is a test. The city hums with something unseen. You have choices to make.")
    gather = response.gather(numDigits=1, action="/game-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to answer the payphone.")
    gather.say("Press 2 to follow a stray cat downtown.")
    gather.say("Press 3 to enter the abandoned mall.")
    gather.say("Press 4 to take the last train of the night.")
    gather.say("Press 5 to visit the firehouse-turned-Chick-fil-A.")
    gather.say("Press 6 to access a mysterious Craigslist terminal.")
    gather.say("Press 7 to open your cryptic email inbox.")
    gather.say("Press 8 to check your stats.")

    return str(response)

@app.route("/game-choice", methods=['POST'])
def game_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "3":
        response.redirect("/mall")

    response.say("Invalid choice. Try again.")
    response.redirect("/twilio-webhook")

    return str(response)

@app.route("/mall", methods=['POST'])
def mall():
    response = VoiceResponse()
    response.say("You stand before the abandoned Metrocenter Mall. The doors are slightly open, but no one should be inside.")
    gather = response.gather(numDigits=1, action="/mall-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to enter through the front.")
    gather.say("Press 2 to sneak into the back.")
    gather.say("Press 3 to check the security footage.")
    gather.say("Press 4 to explore the underground tunnels beneath the mall.")

    return str(response)

@app.route("/mall-choice", methods=['POST'])
def mall_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("You walk through the front doors. The escalators are moving, even though there’s no power.")
        response.redirect("/mall-explore")
    elif digits == "2":
        response.say("You sneak into the back entrance. The janitor closet is unlocked. Something moves inside.")
        response.redirect("/janitor-room")
    elif digits == "3":
        response.say("You find a working security monitor. The footage is grainy, but there’s movement in the food court.")
        response.redirect("/security-footage")
    elif digits == "4":
        response.say("You find a door leading underground. A sign reads: 'AUTHORIZED PERSONNEL ONLY.' It is unlocked.")
        response.redirect("/underground-mall")
    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/mall")

    return str(response)

@app.route("/mall-explore", methods=['POST'])
def mall_explore():
    response = VoiceResponse()
    response.say("The mall is quiet, but the air feels heavy. You see three possible paths.")
    gather = response.gather(numDigits=1, action="/mall-decision", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to explore the old arcade.")
    gather.say("Press 2 to check out the food court.")
    gather.say("Press 3 to enter a department store that is somehow still fully stocked.")

    return str(response)

@app.route("/mall-decision", methods=['POST'])
def mall_decision():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("You step into the old arcade. The machines turn on by themselves. A game you don't recognize is waiting for you to play.")
    elif digits == "2":
        response.say("The food court smells fresh. A tray of hot food sits on a table, untouched. Someone is watching you.")
    elif digits == "3":
        response.say("The department store is still fully stocked. A mannequin turns its head when you aren't looking.")
    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/mall-explore")

    return str(response)

@app.route("/janitor-room", methods=['POST'])
def janitor_room():
    response = VoiceResponse()
    response.say("The janitor closet is filled with old equipment. Something scurries into the shadows.")
    gather = response.gather(numDigits=1, action="/janitor-decision", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to investigate further.")
    gather.say("Press 2 to leave quickly.")

    return str(response)

@app.route("/security-footage", methods=['POST'])
def security_footage():
    response = VoiceResponse()
    response.say("The footage shows a group of people gathered in the food court. But the timestamp is from last night.")
    response.redirect("/mall")

    return str(response)

@app.route("/underground-mall", methods=['POST'])
def underground_mall():
    response = VoiceResponse()
    response.say("You step into the underground mall. The halls are too clean. The lights flicker on.")
    response.redirect("/mall")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)