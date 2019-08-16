from app.utils import GitUtil


class ProjectInfoService(object):

    def __init__(self):
        self.git_handler = GitUtil()

    def get_info(self):
        tags = self.git_handler.get_last_commit_tags()

        return {
            'commit': self.git_handler.get_last_commit_hash(),
            'commit_date': self.git_handler.get_last_commit_date(),
            'branch': self.git_handler.get_current_branch(),
            'version': tags[-1] if tags else ''
        }
