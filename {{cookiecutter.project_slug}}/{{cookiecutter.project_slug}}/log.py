"""Logging module"""
import logging
from logging.handlers import SysLogHandler

from rich.logging import RichHandler

from . import __version__

def configure(module_name = None, **kwargs):
    """Set up log files and associated handlers"""
    # Configure logging, stderr and file logs
    logging_level = logging.INFO
    if kwargs["verbose"]:
        logging_level = logging.DEBUG

    # TODO: set default log format
    logFormatter = logging.Formatter("%(asctime)s - [%(levelname)-4.8s] - %(filename)s %(lineno)d - %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    # System log
    # TODO: format syslog output
    # NOTE: add module/package name to each line in log (so grep can be used to filter)
    # NOTE: '/dev/log' is specific to Linux systems (*not* including MacOS!)
    sysLogHandler = SysLogHandler(address = '/dev/log')
    sysLogHandler.setFormatter(logFormatter)
    sysLogHandler.setLevel(logging_level)
    rootLogger.addHandler(sysLogHandler)

    # User console log
    # TODO: decide on user-friendly logging format for Rich
    consoleHandler = RichHandler(
        level=logging_level,
        show_time=True,
        omit_repeated_times=True,
        show_level=True,
        show_path=True,
        rich_tracebacks=True,
    )
    consoleHandler.setFormatter(logging.Formatter("%(message)s"))
    # consoleHandler.setLevel(logging_level)
    rootLogger.addHandler(consoleHandler)

    # TODO: Add logging to userspace file
    # NOTE: consider using a TSV style log for easier parsing


    # TODO: Add logging to database
    # # Database log

    logging.debug(f'Running {module_name} {__version__}')
    logging.debug(f"Command: {kwargs}")

