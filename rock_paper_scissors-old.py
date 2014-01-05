from flask import Flask, redirect, request, url_for, render_template
from rps_app import get_rps_choice, get_rps_winner

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #return str(request.form) + str(request.get_data())#str(dir(request))
        choice = request.form['choice']
        compChoice = get_rps_choice()
        winner = get_rps_winner(choice,compChoice)
        if winner == 1:
            return '''you chose {}   computer chose {}
            You Won!!
            <input type="submit" method="get" value="play again" action="index"/>'''.format(choice,compChoice)
        else:
            return '''you chose {} computer chose {}
            You lost!!
            <input type="submit" method="get" value="play again" action="index"/>'''.format(choice,compChoice)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
