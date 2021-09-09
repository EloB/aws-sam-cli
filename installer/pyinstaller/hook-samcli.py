from PyInstaller.utils import hooks
from installer.pyinstaller.hidden_imports import SAM_CLI_HIDDEN_IMPORTS

hiddenimports = SAM_CLI_HIDDEN_IMPORTS

<<<<<<< HEAD
hiddenimports = [
    "cookiecutter.extensions",
    "jinja2_time",
    "text_unidecode",
    "samtranslator",
    "samcli.commands.init",
    "samcli.commands.validate.validate",
    "samcli.commands.build",
    "samcli.commands.local.local",
    "samcli.commands.package",
    "samcli.commands.deploy",
    "samcli.commands.logs",
    "samcli.commands.publish",
    # default hidden import 'pkg_resources.py2_warn' is added
    # since pyInstaller 4.0.
    "pkg_resources.py2_warn",
    "aws_lambda_builders.workflows",
    "configparser",
]
=======
>>>>>>> cef0bfaaa544fcd4dd555b3ce6dcb9c76cc12839
datas = (
    hooks.collect_data_files("samcli")
    + hooks.collect_data_files("samtranslator")
    + hooks.collect_data_files("aws_lambda_builders")
    + hooks.collect_data_files("text_unidecode")
)
