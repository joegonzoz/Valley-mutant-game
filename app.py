from flask import Flask, request, session
import random
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)
app.secret_key = "valley_mutant_secret"

# Initialize player stats and inventory
def init_stats():
    return {
        "strength": 3,
        "charisma": 2,
        "perception": 4,
        "health": 10,
        "inventory": []
    }

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

    if digits == "2":
        response.redirect("/cat")
    elif digits == "3":
        response.redirect("/mall")
    
    response.say("Invalid choice. Try again.")
    response.redirect("/twilio-webhook")

    return str(response)

@app.route("/cat", methods=['POST'])
def cat():
    response = VoiceResponse()
    response.say("A stray cat watches you, waiting. It moves with intent.")
    
    gather = response.gather(numDigits=1, action="/cat-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to pet the cat.")
    gather.say("Press 2 to ignore it and keep walking.")
    gather.say("Press 3 to follow it.")
    gather.say("Press 4 to see where it leads.")

    return str(response)

@app.route("/cat-choice", methods=['POST'])
def cat_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()
    stats = session.get("stats", init_stats())

    if digits == "1":
        response.say("You pet the cat. It purrs, then looks up at you. A moment later, it spits out a small key with a Metrocenter logo on it.")
        stats["inventory"].append("Metrocenter Key")
        session["stats"] = stats
        response.redirect("/mall")
    elif digits == "2":
        response.say("You ignore the cat and walk away. As you leave, you swear you hear it whisper something.")
        response.redirect("/twilio-webhook")
    elif digits == "3":
        response.say("You follow the cat. It moves with purpose, leading you through a twisting alleyway.")
        response.redirect("/cat-follow")
    elif digits == "4":
        response.say("The cat stops in front of a payphone. The receiver is off the hook, but no one is there.")
        response.redirect("/payphone")

    return str(response)

@app.route("/mall", methods=['POST'])
def mall():
    response = VoiceResponse()
    response.say("You arrive at Metrocenter Mall. The air feels thick, like memories are still clinging to the walls.")
    
    gather = response.gather(numDigits=1, action="/mall-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to enter through the front doors.")
    gather.say("Press 2 to sneak in through an employee entrance.")
    gather.say("Press 3 to check if anything is still open.")
    gather.say("Press 4 to use the Metrocenter Key.")

    return str(response)

@app.route("/mall-choice", methods=['POST'])
def mall_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()
    stats = session.get("stats", init_stats())

    if digits == "1":
        response.say("You walk through the front doors. The lights flicker on, but you swear the mall has been closed for years.")
    elif digits == "2":
        response.say("You sneak into the back. You hear the distant sound of a janitor’s cart, but no one is pushing it.")
    elif digits == "3":
        response.say("The old arcade is still running, but the machines play games you've never seen before.")
    elif digits == "4" and "Metrocenter Key" in stats["inventory"]:
        response.say("You insert the Metrocenter Key into an old maintenance door. A hidden escalator whirs to life, leading down.")
        response.redirect("/hidden-mall-level")
    else:
        response.say("You don't have the key. The door doesn’t budge.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/hidden-mall-level", methods=['POST'])
def hidden_mall_level():
    response = VoiceResponse()
    response.say("You step into a part of the mall that shouldn't exist. Mannequins line the walls, watching.")
    
    gather = response.gather(numDigits=1, action="/hidden-mall-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to approach a mannequin.")
    gather.say("Press 2 to check an abandoned store.")
    gather.say("Press 3 to look for an exit.")
    gather.say("Press 4 to listen for any sounds.")

    return str(response)

@app.route("/hidden-mall-choice", methods=['POST'])
def hidden_mall_choice():
    digits = request.form.get("Digits", "").strip()
    response = VoiceResponse()

    if digits == "1":
        response.say("One of the mannequins moves. Its head turns slowly toward you.")
    elif digits == "2":
        response.say("Inside the store, old sale signs hang untouched. A radio crackles to life, playing an old jingle.")
    elif digits == "3":
        response.say("Every hallway leads back to the same spot. The mannequins seem closer now.")
    elif digits == "4":
        response.say("A distant voice whispers your name. It sounds familiar.")

    response.redirect("/twilio-webhook")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)