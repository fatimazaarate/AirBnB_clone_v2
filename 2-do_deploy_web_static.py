#!/usr/bin/python3
"""
a Fabric script that distributes an archive to my web servers
"""
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['34.224.3.13', '3.83.18.210']


def do_deploy(archive_path):
    """deploys the archive to my servers"""

    # Check if the specified archive_path exists
    if exists(archive_path) is False:
        return False

    # Extract filename and filename without extension
    file_name = archive_path.split('/')[-1]
    filename_without_ext = file_name.split('.')[0]

    # Upload the archive to the /tmp/ directory on the server
    put(archive_path, "/tmp/")

    # Create a directory for the new release
    run("mkdir -p /data/web_static/releases/{}/"
        .format(filename_without_ext))

    # Extract the archive to the new release directory
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(file_name, filename_without_ext))

    # Remove the uploaded archive from /tmp/
    run("rm /tmp/{}".format(file_name))

    # Move the contents of web_static subdirectory to release directory
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/"
        .format(filename_without_ext, filename_without_ext))

    # Remove the now-empty web_static subdirectory
    run("rm -rf /data/web_static/releases/{}/web_static"
        .format(filename_without_ext))

    # Remove the symbolic link to the current release
    run("rm -rf /data/web_static/current")

    # Create a new symbolic link to the latest release
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(filename_without_ext))

    # Deployment successful
    print("New version deployed!")
    return True
