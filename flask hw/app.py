from flask  import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def madlibs_form():
    """Shows a form for prompts for all the words in the story"""

    prompts = story.prompts
    return render_template("questions.html", prompts = prompts)

@app.route('/story')
def make_story():
    """Returns story from prompts"""

    text = story.generate(request.args)
    return render_template('story.html', text = text)