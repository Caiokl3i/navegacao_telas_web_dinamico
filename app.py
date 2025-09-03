from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return redirect(url_for('grupos', grupo=0))

@app.route("/grupo<int:grupo>")
def grupos(grupo):  
    return render_template(f"grupo{grupo}/index.html")

@app.route("/grupo<int:grupo>/tela<int:tela>")
def telas(grupo, tela):
    return render_template(f"grupo{grupo}/tela{tela}.html")

if __name__ == "__main__":
    app.run(debug=True)