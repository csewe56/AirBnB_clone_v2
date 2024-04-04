#!/usr/bin/python3
<<<<<<< HEAD
# Fabric script that generates a .tgz archive from the contents of the web_static folder of AirBnB Clone repo,using the function do_pack

""" module doc
"""
from fabric.api import task, local
=======
""" This is a fabric scripts based on the file 1-pack_web_static.py
    that distributes an archive to your web servers
    using the function name do_deploy
"""
import os.path
>>>>>>> 52a5e32b9c5dc91a764a1ec444435974a924eaec
from datetime import datetime


@task
def do_pack():
<<<<<<< HEAD
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(formatted_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None
=======
    ''' This makes an archive on web_static folder'''

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
>>>>>>> 52a5e32b9c5dc91a764a1ec444435974a924eaec
