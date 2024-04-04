#!/usr/bin/python3
""" This is a fabric scripts based on the file 1-pack_web_static.py
    that distributes an archive to your web servers
    using the function name do_deploy
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    ''' This makes an archive on web_static folder'''

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
