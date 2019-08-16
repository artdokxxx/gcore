from datetime import datetime

from app.utils.cmd import run_command


class GitUtil(object):
    def __init__(self):
        self.cmd_last_commit = 'git log -n 1'

    def __format_cmd(self, fmt='%H'):
        return f'{self.cmd_last_commit} --pretty=format:"{fmt}"'

    def get_last_commit_hash(self):
        return run_command(
            self.__format_cmd('%H')
        )[0][1:-1]

    def get_last_commit_date(self):
        dt = run_command(
            self.__format_cmd('%ai')
        )[0]
        dt = datetime.strptime(dt[1:-1], '%Y-%m-%d %H:%M:%S %z')
        return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    def get_current_branch(self):
        return run_command(
            'git rev-parse --abbrev-ref HEAD'
        )[0]

    def get_last_commit_tags(self):
         return run_command(
            'git tag -l --points-at HEAD'
        )
