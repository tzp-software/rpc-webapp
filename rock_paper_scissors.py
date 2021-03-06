from flask import Flask, redirect, request, url_for, render_template
from rps_app import get_rps_choice, get_rps_winner

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #return str(request.form) + str(request.get_data())#str(dir(request))
        choice = request.form['choice']
        compChoice = get_rps_choice()
        winner, quote = get_rps_winner(choice,compChoice,quote=True)
        if winner == 1:
            return render_template('results-a.html',choice=choice,compChoice=compChoice,quote=quote)
        elif winner == 2:
            return render_template('results-b.html',choice=choice,compChoice=compChoice,quote=quote)
        else:
            return render_template('results-c.html',choice=choice,compChoice=compChoice)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
