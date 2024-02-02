#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
using the function do_pack."""
from fabric.api import env, put, run, local
from datetime import datetime
from os.path import exists

env.hosts = ['100.26.237.224', '100.25.204.41']
env.user = 'ubuntu'

# Global variable to store the archive path
archive_path = None
pack_executed = False


def do_pack():
    """Function to generate a .tgz archive."""
    local("mkdir -p versions")
    date = datetime.now()
    date = date.strftime("%Y%m%d%H%M%S")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except:
        return None


def do_deploy(archive_path):
    """Function to deploy."""
    if not archive_path or not exists(archive_path):
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
    except:
        return False


def deploy():
    """Function to full deploy process."""
    global archive_path, pack_executed

    if not pack_executed:
        archive_path = do_pack()
        pack_executed = True

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
