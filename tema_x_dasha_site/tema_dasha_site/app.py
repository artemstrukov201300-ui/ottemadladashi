from flask import Flask, render_template, send_file, request, abort
from io import BytesIO
import qrcode
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/qr.png")
def qr_png():
    # After deployment, this automatically points to the public site address.
    # You can override it with the PUBLIC_URL environment variable.
    target = os.environ.get("PUBLIC_URL") or request.host_url.rstrip("/")
    img = qrcode.make(target)
    output = BytesIO()
    img.save(output, format="PNG")
    output.seek(0)
    return send_file(output, mimetype="image/png", download_name="tema-loves-dasha-qr.png")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
