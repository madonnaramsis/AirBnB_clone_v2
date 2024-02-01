#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
using the function do_pack."""
from fabric.api import local
from datetime import datetime


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
