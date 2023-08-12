from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder = "template") # create a object as app

todos = [{"task":"Sample todo", "done": False}]  # we are going to create todo list for add the dictionary as {"todo":"hdahdjh", "done" : True}

@app.route("/")
def index():
    return render_template("index.html",todos = todos )

#  add todos for the list
@app.route("/add", methods = ["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods = ["POST", "GET"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        new_task = request.form["todo"]
        todos[index]["task"] = new_task
        return redirect(url_for("index"))
    else:
        return render_template("edit.html",todo = todo, index = index )

@app.route("/check/<int:index>")
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug  = True)
