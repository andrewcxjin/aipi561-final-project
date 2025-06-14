from pipeline.orchestrator import run_trend_pipeline

def test_pipeline_returns_report():
    result = run_trend_pipeline()
    assert "Trend" in result