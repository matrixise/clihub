# -*- coding: utf-8 -*-
"""
    clihub/gist.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>
    :license: BSD, see LICENSE for more details
"""
import requests
import json


class Gist(object):
    @classmethod
    def create(cls, account, files, description=None, private=False):
        hash_files = {}
        for filename in files:
            with open(filename, 'r') as fp:
                hash_files[filename] = {
                    'content': fp.read(),
                }

        values = {
            'description': description or 'Undefined Description',
            'public': not private,
            'files': hash_files
        }
        url = 'https://api.github.com/gists'

        query = requests.post(url,
                              auth=(account.username, account.password),
                              data=json.dumps(values))

        if query.status_code == 201:
            return query.json()['html_url']

    @classmethod
    def delete(cls, account, gist_id):
        url = 'https://api.github.com/gists/{gist_id}'
        url = url.format(gist_id=gist_id)

        requests.delete(url, auth=(account.username, account.password))

    def __init__(self, account):
        self.account = account
