from flask import Flask, url_for, render_template
from forms import InfoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TOP_SECRET'


@app.route('/answer', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    # if form.validate_on_submit():
    #     return render_template()
    return render_template('form.html', title='Введите данные', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
