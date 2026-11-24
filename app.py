from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    submitted_name = ""
    submitted_nim = ""
    submitted_fakultas = ""
    submitted_prodi = ""
    biodata = None

    if request.method == "POST":
        submitted_name = request.form.get("username", "").strip()
        submitted_nim = request.form.get("nim", "").strip()
        submitted_fakultas = request.form.get("fakultas", "").strip()
        submitted_prodi = request.form.get("prodi", "").strip()

        biodata = {
            "username": submitted_name,
            "nim": submitted_nim,
            "fakultas": submitted_fakultas,
            "prodi": submitted_prodi,
        }

    return render_template(
        "index.html",
        biodata=biodata,
        submitted_name=submitted_name,
        submitted_nim=submitted_nim,
        submitted_fakultas=submitted_fakultas,
        submitted_prodi=submitted_prodi,
    )


if __name__ == "__main__":
    app.run(debug=True)