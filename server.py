from flask import Flask, request, render_template
app = Flask(__name__)



#render 
@app.route("/")
def hello():
    return render_template('form.html')


@app.route("/echo", methods=["POST"])
def echo():
    story_title = request.form["story_title"]
    user_story = request.form["user_story"]
    acceptance_criteria = request.form["acceptance_criteria"]
    business_value = request.form["business_value"]
    estimation = request.form["estimation"]
    status = request.form["status"]
    data_from_user = [story_title, user_story, acceptance_criteria, estimation, status]
    with open("database.csv", "a") as database:
        for i in data_from_user:
            if i == data_from_user[len(data_from_user) - 1]:
                database.write(i + "\n")
            else:
                database.write(i + ", ")
    return render_template('form.html', story_title=request.form['story_title'])


if __name__ == "__main__":
    app.run()
