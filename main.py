from flask import Flask, request, render_template, Response
from lib.Auth import Auth
import qrcode, io


app = Flask(__name__, static_folder="assets")
inst = Auth()


@app.route("/", methods=["GET", "POST"])
def root() -> str:
    return render_template("serve.html", route=request.path)


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up() -> str:
    params = dict(route=request.path, message="", success=False, auth_uri="")

    if request.method == "POST":
        username, password = request.form.values()
        result = inst.create_entry(username, password)

        if result['code']:
            params["message"] = result['message']

        if not result["code"]:
            params["success"] = True

        if params["success"]:
            params["auth_uri"],params["secret_key"] = result['content']

    return render_template("serve.html", **params)


@app.route("/sign-in", methods=["GET", "POST"])
def sign_in() -> str:
    params = dict(route=request.path, message="", success=False, client_id="", require_otp=False)

    if request.method == "POST":

        if "otp" in request.form.keys():
            client_id, otp = request.form.values()
            result = inst.authorization(client_id, int(otp))
            params["success"] = True if not result['code'] else False

        else:
            username, password = request.form.values()
            result = inst.authentication(username, password)

            if not result['code']:
                params["require_otp"] = True
                params["client_id"] = result['content']

        params['message'] = result['message'] if result['code'] else ""

    return render_template("serve.html", **params)


@app.route("/qrcode.png", methods=["POST"])
def qr_image() -> str:
    f = io.BytesIO()
    img = qrcode.make(request.get_json(force=True)['content'])
    img.save(f)
    f.seek(0)
    return Response(f.read(), mimetype="image/png")


app.run("127.0.0.1", 5000, debug=True)
