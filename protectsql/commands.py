import click

@click.group()
def protectsql():
    pass


@protectsql.command()
@click.option("--config-path", default=".", show_default=True, type=click.Path())
def init(config_path):
    """
    Initializes the project folder with .pysa and taint.config files
    """
    click.echo("Initialising")


@protectsql.command()
def analyze():
	click.echo("Analyzing")
