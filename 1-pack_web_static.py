#!/usr/bin/python3
""" webstatic fabric """
import time
from fabric.api import local
import os.path


def do_pack():
    """ pack my static"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(timestamp)
    try:
        if not os.path.exists('versions'):
            l = local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
