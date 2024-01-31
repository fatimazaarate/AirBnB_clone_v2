#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""

    try:
        if isdir("versions") is False:
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
