from sys import path
from os import system, chdir


def git_branch_origins(branch, repo=None):
    if repo is not None:
        chdir(path[0] + '/' + 'tools')
    system('git branch --set-upstream-to=origin/{branch} {branch}'.format(
        branch=branch
    ))
    return chdir(path[0])


def git_pull_all():
    system('git pull --recurse-submodules')