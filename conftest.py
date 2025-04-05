import logging.config
from os import path

lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(lof_file_path)


pytest_plugins = [
    "src.fixtures"
]


def pytest_addoption(parser):
    parser.addini("browser_name", "Browser name for tests")
    parser.addini("headless", "Run browser in headless mode")
    parser.addini("wait", "Run browser in wait mode")
