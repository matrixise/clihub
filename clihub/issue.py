# -*- coding: utf-8 -*-
"""
    clihub/issue.py
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>
    :license: BSD, see LICENSE for more details
"""
import requests
import json


class Issue(object):
    @classmethod
    def create(cls, account, repository_name, title, body):
        values = {
            'title': title,
            'body': body,
        }
        url = 'https://api.github.com/repos/{username}/{repository}/issues'.format(username=account.username,
                                                                                   repository=repository_name)

        query = requests.post(url,
                              auth=(account.username, account.password),
                              data=json.dumps(values))

        if query.status_code == 201:
            print query.json()['url']
