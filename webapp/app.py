from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder="../static",
)


@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

