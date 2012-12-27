#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    clihub login <username> <password>
    clihub logout
    clihub repo new <name> [--no-wiki] [--no-issues]
    clihub repo delete <name>
    clihub gist new [--description=DESCRIPTION] [--private] FILES...
    clihub gist delete <name>
    clihub issue new <repository> <title> [--description=DESCRIPTION]

Options:
    -h, --help      Show this screen
    --version       Show version

"""
from docopt import docopt
from ..account import Account
from ..repository import Repository
from ..gist import Gist
from ..issue import Issue
from ..release import version


def main():
    arguments = docopt(__doc__, version=version)
    if arguments.get('login'):
        return Account.save_to_config(arguments.get('<username>'),
                                      arguments.get('<password>'))

    if arguments.get('logout'):
        return Account.remove_config()

    if arguments.get('repo'):
        with Account.load_from_config() as account:
            if arguments.get('new'):
                has_issues = not arguments.get('--no-issues')
                has_wiki = not arguments.get('--no-wiki')
                Repository.create(account, arguments.get('<name>'),
                                  has_issues=has_issues,
                                  has_wiki=has_wiki)
            if arguments.get('delete'):
                Repository(account, arguments.get('<name>')).delete()

    if arguments.get('gist'):
        with Account.load_from_config() as account:
            if arguments.get('new'):
                description = arguments.get('--description') or 'Undefined Description'
                private = arguments.get('--private') or False
                gist = Gist.create(account, arguments.get('FILES'),
                                   description=description,
                                   private=private)
                print gist
            if arguments.get('delete'):
                Gist.delete(account, arguments.get('<name>'))

    if arguments.get('issue'):
        with Account.load_from_config() as account:
            if arguments.get('new'):
                Issue.create(account, arguments.get('<repository>'), arguments.get('<title>'), arguments.get('--description'))

if __name__ == '__main__':
    main()
