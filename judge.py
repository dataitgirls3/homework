# -*- coding: utf-8 -*-
import os
import sys
import subprocess


def build_test_cmd(homework, github_id):
    return ['pytest', '-v', f'{homework}/test_{homework}.py', '--githubid', github_id]


def main():
    is_pull_request = os.environ.get('TRAVIS_PULL_REQUEST', 'false').lower() != 'false'
    if is_pull_request:
        travis_branch = os.environ.get('TRAVIS_PULL_REQUEST_BRANCH', None)
        homework, github_id = travis_branch.strip().split('_')
        github_id = github_id.replace('.py', '')
        cmds = [build_test_cmd(homework, github_id)]
    else:
        cmds = []
        for homework in os.listdir('.'):
            if not homework.startswith('homework'):
                continue
            for solution in os.listdir(f'./{homework}/solutions'):
                if not solution.startswith(homework):
                    continue
                github_id = solution.strip().split('_')[1].replace('.py', '')
                cmds.append(build_test_cmd(homework, github_id))

    for cmd in cmds:
        exitcode = subprocess.call(cmd)
        if exitcode != 0:
           sys.exit(exitcode) 


if __name__ == '__main__':
    main()
