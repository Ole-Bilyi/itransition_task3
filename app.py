from flask import Flask, request, Response
from math import lcm
import re

app = Flask(__name__)

@app.route("/oleksandrbilyi207_gmail_com", methods=["GET"])
def lcm_endpoint():
    x, y = request.args.get("x", ""), request.args.get("y", "")

    if not re.fullmatch(r"[0-9]+", x) or not re.fullmatch(r"[0-9]+", y):
        return Response("NaN", mimetype="text/plain")

    result = str(lcm(int(x), int(y)))

    return Response(result, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
