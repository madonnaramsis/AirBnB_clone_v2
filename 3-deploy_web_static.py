#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
using the function do_pack."""
from fabric.api import env, put, run, local
from datetime import datetime
from os.path import exists
env.hosts = ['54.210.173.51', '52.73.37.123']


def do_pack():
    """Function to generate a .tgz archive."""
    local("mkdir -p versions")
    date = datetime.now()
    date = date.strftime("%Y%m%d%H%M%S")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except Exception:
        return None


def do_deploy(archive_path):
    """Function to deploy."""
    if not archive_path and not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file, name))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Function to full deploy process."""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
