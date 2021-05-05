from subprocess import Popen, PIPE
from datetime import datetime
import os


def exec_command(command: str):
    with Popen(command, shell=True, stdout=PIPE) as p:
        output, errors = p.communicate()
        lines = output.decode('utf-8').splitlines()
    return lines


def read_git_log(number: int = 20):
    commits = []
    current_git_log = {}
    for log in exec_command("git log -{number}".format(number=number)):
        if log.startswith("commit"):
            if len(current_git_log) != 0:
                commits.append(current_git_log)
                current_git_log = {}
            current_git_log["commit"] = log[7:14]
        if log.startswith("Author:"):
            current_git_log["author"] = log[8:].split(" <")[0]
        if log.startswith('Date:'):
            current_git_log["date"] = datetime.strptime(log[8:], '%a %b %d %H:%M:%S %Y %z')
        if log.startswith("    "):
            current_git_log["message"] = log[4:]

    if len(current_git_log) != 0:
        commits.append(current_git_log)

    return commits


def env_dependency_file():
    filename = None

    if 'CONDA_DEPENDENCY_FILE' in os.environ:
        print(exec_command('pwd'))
        filename = os.environ['CONDA_DEPENDENCY_FILE']
    elif os.path.exists('environment.yml'):
        filename = 'environment.yml'
    elif os.path.exists('requirements.txt'):
        filename = 'requirements.txt'

    if filename is not None:
        with open(filename, 'r') as file:
            return file.read()
    else:
        return 'No dependency file can be found.'
