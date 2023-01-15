import click
import platform
import pkg_resources
from colorama import init

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.pass_context
@click.option('-d', '--debug', is_flag=True, default=False, help='Enable debug')
def electricity(ctx, debug):
    """Electricity monitor."""
    if ctx.invoked_subcommand is None:
        click.secho(ctx.get_help())
        return


@electricity.command(short_help='show version')
@click.pass_context
def version(ctx):
    """Show electricity monitor version"""
    ver = pkg_resources.require("electricity-monitor")[0].version
    ver_obj = {
        'product': 'electricity-monitor',
        'description': 'Electricity Monitor Command-Line Tool',
        'version': ver,
        'python': platform.python_version()
    }
    ver_str = '%s, %s, %s' % (ver_obj['product'], ver_obj['description'],
                              ver_obj['version'])
    click.echo(ver_str)


def print_command(cmd, level=0):
    click.echo(' ' + (' ' * level * 2) + ' ', nl=False)
    click.echo(cmd.name)
    if type(cmd) == click.core.Group:
        for k in sorted(cmd.commands.keys()):
            print_command(cmd.commands[k], level + 1)


@electricity.command(short_help='show help')
@click.pass_context
@click.option('-t', '--tree', is_flag=True, default=False, help='show commands tree')
def help(ctx, tree):
    """Show electricity monitor help"""
    if tree:
        print_command(ctx.parent.command)
    else:
        click.secho(ctx.parent.get_help())


if __name__ == '__main__':
    electricity()
else:
    init(autoreset=True)
