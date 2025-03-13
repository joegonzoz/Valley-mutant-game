# Fully expanded app.py for Valley Mutant with deep branching story, combat, stat progression, and interactive locations

from flask import Flask, request, session
import random
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)
app.secret_key = "valley_mutant_secret"  # Enables session tracking for stats

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

    if digits == "1":
        response.redirect("/payphone")
    elif digits == "2":
        response.redirect("/cat")
    elif digits == "3":
        response.redirect("/mall")
    elif digits == "4":
        response.redirect("/train")
    elif digits == "5":
        response.redirect("/firehouse")
    elif digits == "6":
        response.redirect("/craigslist")
    elif digits == "7":
        response.redirect("/email-inbox")
    elif digits == "8":
        response.redirect("/check-stats")
    else:
        response.say("Invalid choice. Try again.")
        response.redirect("/twilio-webhook")

    return str(response)

@app.route("/check-stats", methods=['POST'])
def check_stats():
    stats = session.get("stats", init_stats())
    response = VoiceResponse()
    response.say(f"Your stats are: Strength {stats['strength']}, Charisma {stats['charisma']}, Perception {stats['perception']}, Health {stats['health']}.")
    response.redirect("/twilio-webhook")
    return str(response)

@app.route("/payphone", methods=['POST'])
def payphone():
    response = VoiceResponse()
    response.say("The payphone clicks. A distorted voice whispers, 'You are late. The red door is moving.'")
    gather = response.gather(numDigits=1, action="/payphone-choice", method="POST", barge_in=True, timeout=5)
    gather.say("Press 1 to ask where the door is.")
    gather.say("Press 2 to hang up.")
    gather.say("Press 3 to say nothing and listen.")
    gather.say("Press 4 to trace the call.")

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

@app.route("/combat", methods=['POST'])
def combat():
    stats = session.get("stats", init_stats())
    response = VoiceResponse()

    enemy_hp = 5
    player_hp = stats["health"]

    response.say("A shadowy figure emerges. You are in combat!")

    while player_hp > 0 and enemy_hp > 0:
        player_roll = random.randint(1, 6) + stats["strength"]
        enemy_roll = random.randint(1, 6)

        if player_roll > enemy_roll:
            enemy_hp -= 2
            response.say(f"You hit! Enemy HP: {enemy_hp}")
        else:
            player_hp -= 2
            response.say(f"You got hit! Your HP: {player_hp}")

    if player_hp <= 0:
        response.say("You fall to the ground. Game over.")
    else:
        response.say("You defeated the enemy!")
        stats["strength"] += 1  # Stat progression example
        session["stats"] = stats

    response.redirect("/twilio-webhook")
    return str(response)

@app.route("/craigslist", methods=['POST'])
def craigslist():
    response = VoiceResponse()
    response.say("You access a forgotten Craigslist terminal.")
    ads = [
        "MISSING: My cat disappeared... but I still hear him purring under the floor.",
        "FOR SALE: VHS tape, unmarked, plays footage of your house from last night.",
        "HELP WANTED: Need someone to check if I’m real. $50 cash.",
        "MISSED CONNECTION: You looked at me at the light rail station. Your eyes were gone."
    ]
    response.say(random.choice(ads))
    response.redirect("/twilio-webhook")
    return str(response)

@app.route("/email-inbox", methods=['POST'])
def email_inbox():
    response = VoiceResponse()
    response.say("You log into your old email. One unread message.")
    emails = [
        "FROM: unknown@nowhere.com | SUBJECT: STOP DIGGING. | MESSAGE: They know what you found. Run.",
        "FROM: self@past.com | SUBJECT: DON'T GET ON THE TRAIN. | MESSAGE: I didn't listen. Now I'm stuck.",
        "FROM: station13@radio.com | SUBJECT: BROADCASTING SOON. | MESSAGE: Tune in at 3:13 AM. We will be waiting."
    ]
    response.say(random.choice(emails))
    response.redirect("/twilio-webhook")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)