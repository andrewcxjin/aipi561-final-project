from flask import Flask
from app.routes import routes
import os

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)