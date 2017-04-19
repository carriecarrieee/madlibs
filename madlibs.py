"""A madlib game that compliments its users."""

from random import choice, sample, randint

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")
    number = randint(1, 10)
    compliments = sample(AWESOMENESS, number)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Returns game if user said yes or goodbye page if no"""

    answer = request.args.get('answer')
    if answer == 'yes':
        return render_template('game.html')
    else:
        return render_template('goodbye.html')


@app.route('/madlibs', methods=['POST'])
def show_madlibs():
    """Returns madlib template that fills in inputs from user"""

    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    vehicle = request.form.get('vehicle')
    animals = request.form.getlist('animals')
    pages = ['madlibs.html', 'madlibs2.html']
    page = choice(pages)

    return render_template(page,
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            vehicle=vehicle,
                            animals=animals)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
