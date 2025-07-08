from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
num = random.randint(1, 6)

@app.route('/')
def home():
    return render_template('gng.html')

@app.route('/guess', methods=['POST'])
def guess():
    global num
    user_guess = int(request.json['guess'])
    if user_guess > num:
        return jsonify(feedback="Your guess is greater than the number! Try again..")
    elif user_guess < num:
        return jsonify(feedback="Your guess is less than the number! Try again..")
    elif user_guess == num:
        feedback = f"Correct! The number was {num}."
        num = random.randint(1, 6)  # Reset for the next game
        return jsonify(feedback=feedback)
if __name__ == '__main__':
    app.run(debug=True)
