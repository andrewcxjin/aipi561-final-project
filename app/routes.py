from flask import Blueprint, request, render_template
from pipeline.orchestrator import run_trend_pipeline
from llm.local_model import generate_content

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/run-pipeline", methods=["POST"])
def run_pipeline():
    report = run_trend_pipeline()
    return {"report": report}

@routes.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt")
    result = generate_content(prompt)
    return {"output": result}