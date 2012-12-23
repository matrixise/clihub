#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


Usage:
    clihub login <username> <password>
    clihub logout
    clihub repo new <name> [--wiki] [--issue]
    clihub repo delete <name>

Options:
    -h, --help      Show this screen
    --version       Show version

"""
import sys
from docopt import docopt
from ..account import Account
from ..repository import Repository
from ..release import version


def main():
    arguments = docopt(__doc__, version=version)
    print arguments
    if arguments.get('login'):
        return Account.save_to_config(arguments.get('<username>'),
                                      arguments.get('<password>'))

    if arguments.get('logout'):
        return Account.remove_config()

    if arguments.get('repo'):
        account = Account.load_from_config()
        if not account:
            print "There is no config file"
            sys.exit(1)
        if arguments.get('new'):
            Repository.create(account, arguments.get('<name>'))
        if arguments.get('delete'):
            Repository(account, arguments.get('<name>')).delete()

if __name__ == '__main__':
    main()