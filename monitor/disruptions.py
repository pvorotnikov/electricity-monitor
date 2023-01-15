import click
import requests
from time import sleep
from monitor.main import electricity


@electricity.command(short_help='show disruptions for subscription ids')
@click.pass_context
@click.argument('ids', metavar='<id> [<id>]', nargs=-1, required=True)
def disruptions(ctx, ids):
    """
    Show disruptions for subscription ids.

    <id> is the subscription number.

    Example: electricity disruptions 1234567890
    """
    for id in ids:
        data = get_disruptions(id)
        click.echo(data)


@electricity.command(short_help='monitor disruptions for subscription ids')
@click.pass_context
@click.argument('ids', metavar='<id> [<id>]', nargs=-1, required=True)
def monitor(ctx, ids):
    """
    Monitor disruptions for subscription ids.

    <id> is the subscription number.

    Example: electricity monitor 1234567890
    """
    while True:
        for id in ids:
            data = get_disruptions(id)
            click.echo(data)
        sleep(5 * 60)


def get_disruptions(id):
    form_data = {'action': 'viewitn', 'itn': id}
    response = requests.post(
        'https://info.electrohold.bg/webint/vok/avplan.php', data=form_data)
    return response.text
