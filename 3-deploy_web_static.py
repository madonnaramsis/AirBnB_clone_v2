#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
using the function do_pack."""
from fabric.api import local
from fabric.operations import env, put, run
import time
from os.path import isfile
env.hosts = ['54.210.173.51', '52.73.37.123']


def do_pack():
    """Function to generate a .tgz archive."""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None


def do_deploy(archive_path):
    """Function to deploy."""
    if (isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Function to full deploy process."""
    try:
        path = do_pack()
        return do_deploy(path)
    except:
        return False
