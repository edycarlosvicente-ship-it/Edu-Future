from flask import Flask, render_template

app = Flask(__name__)

#adicionar rota para home page

@app.route("/")
def index():
  return render_template("index.html")

#rodar a app
if __name__ == "__main__":
  app.run(host="0.0.0.0", host=5000)