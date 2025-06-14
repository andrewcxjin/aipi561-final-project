import click
from pipeline.orchestrator import run_trend_pipeline
from llm.local_model import generate_content

@click.group()
def cli():
    pass

@cli.command()
def trends():
    report = run_trend_pipeline()
    click.echo(report)

@cli.command()
@click.argument("prompt")
def generate(prompt):
    output = generate_content(prompt)
    click.echo(output)

if __name__ == "__main__":
    cli()