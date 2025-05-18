from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/access")
def access():
    role = request.args.get("role")
    ip = request.remote_addr
    if role == "admin" and ip.startswith("192.168."):
        return jsonify({"access": "granted"})
    return jsonify({"access": "denied"})
if __name__ == "__main__":
    app.run(port=5000)
