
# Fixed app.py for .pyramid with optimized TwiML response size

from flask import Flask, request, session
import twilio.twiml
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)
app.secret_key = "valley_mutant_secret"  # For session handling

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Handles incoming calls and presents story choices with optimized response size."""
    response = VoiceResponse()

    # Vaporwave intro (shortened)
    response.play("https://your-audio-host.com/vaporwave_intro.mp3")
    response.say("Welcome to Valley Mutant. You shouldnâ€™t be here.")

    # Redirect to first choice to keep TwiML response small
    response.redirect("/choice1")

    return str(response)

@app.route("/choice1", methods=['GET', 'POST'])
def choice1():
    """Handles the first choice in a separate request."""
    response = VoiceResponse()

    gather = Gather(input="dtmf", num_digits=1, action="/choice1_result")
    gather.say("A flickering payphone. Press 1 to listen to the static. Press 2 to hang up.")
    response.append(gather)

    return str(response)

@app.route("/choice1_result", methods=['GET', 'POST'])
def choice1_result():
    """Processes the first choice and redirects to avoid large TwiML responses."""
    response = VoiceResponse()
    digits = request.values.get("Digits")

    if digits == "1":
        response.play("https://your-audio-host.com/static_noise.mp3")
        response.say("You hear voices in the static. They know your name.")
        response.redirect("/dice_roll")
    elif digits == "2":
        response.say("You hang up. But the phone rings again. Louder.")
        response.redirect("/game_over")

    return str(response)

@app.route("/dice_roll", methods=['GET', 'POST'])
def dice_roll():
    """Handles a dice roll event with a separate response to keep it small."""
    response = VoiceResponse()
    response.play("https://your-audio-host.com/dice_roll.mp3")
    response.say("Rolling the dice. Your fate is being decided.")

    # Random success or failure outcome
    import random
    roll = random.randint(1, 6)
    if roll > 3:
        response.say(f"You rolled a {roll}. You move deeper into the mystery.")
        response.redirect("/deep_mystery")
    else:
        response.say(f"You rolled a {roll}. Something is wrong. Very wrong.")
        response.redirect("/game_over")

    return str(response)

@app.route("/deep_mystery", methods=['GET', 'POST'])
def deep_mystery():
    """Continues the story with optimized response size."""
    response = VoiceResponse()
    response.say("You step off the train, but the station looks... old. Too old.")
    response.play("https://your-audio-host.com/creepy_ambience.mp3")
    response.say("A stranger in a long coat hands you a cassette tape. He whispers, 'Youâ€™ll need this.'")
    response.redirect("/game_over")

    return str(response)

@app.route("/game_over", methods=['GET', 'POST'])
def game_over():
    """Handles the game over sequence separately."""
    response = VoiceResponse()
    response.play("https://your-audio-host.com/game_over_sound.mp3")
    response.say("The city closes around you. Your story ends here. Game over.")
    response.hangup()

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)