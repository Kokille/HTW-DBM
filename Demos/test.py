from flask import Flask

app = Flask("Demo")

@app.route("/hello/<name>")
def begruessung(name):
	return "Hallo " + name + "!"

if __name__ == "_main_":
	app.run(debug=True, port=5000)