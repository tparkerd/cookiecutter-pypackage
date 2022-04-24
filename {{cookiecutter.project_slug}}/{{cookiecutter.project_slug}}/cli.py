"""Console script for {{cookiecutter.project_slug}}."""
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import logging
import sys
import time
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
from . import __version__, log


{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    description = "Console script for {{cookiecutter.project_slug}}"
    parser = argparse.ArgumentParser(description=description,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-V", "--version", action="version", version=f'%(prog)s {__version__} ')
    parser.add_argument("-f", "--force", action="store_true", help="Force file creation. Overwrite any existing files.")
    parser.add_argument("-n", "--dry-run", dest='dryrun', action="store_true", help="Perform a trial run. Only console and syslog are updated.")
    parser.add_argument("path", metavar='PATH', type=str, nargs=1, help='Input directory to process')
    args = parser.parse_args()

    log.configure(module_name = 'main',**vars(args))

    if args.dryrun:
        logging.info(f"DRY-RUN MODE ENABLED")

    # Disable progress bars if verbose mode enabled
    if args.verbose:
        args.progress = False
        
    start_time = time.perf_counter()
    # returncode = do_work()  # TODO: replace me
    logging.info(f'Total execution time: {time.perf_counter() - start_time} seconds')
    return returncode

{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
