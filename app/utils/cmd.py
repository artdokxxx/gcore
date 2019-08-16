import subprocess


def run_command(cmd):
    res = subprocess.check_output(cmd.split())
    res = res.decode().split('\n')

    return list(filter(None, res))
