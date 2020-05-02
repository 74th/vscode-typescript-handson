import os
import os.path
import time

from invoke import task
import yaml

os_user = "ubuntu"

@task
def build_environment(c):
    settings_file = "/root/settings/settings.yaml"
    if not os.path.exists(settings_file):
        return
    with open(settings_file) as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    sudo = f"sudo -u {os_user}"

    with c.cd(f"/home/{os_user}/"):

        if "repo" in settings:
            repo = settings["repo"]
            c.run(f"{sudo} git init")
            c.run(f"{sudo} git remote add origin {repo}")
            c.run(f"{sudo} git fetch origin")
            c.run(f"{sudo} git checkout origin/master")

        for command in settings.get("commends", []):
            c.run(f"{sudo} {command}")

        for user in settings.get("users", []):
            c.run(f"{sudo} mkdir {user}")
            for file in settings.get("files", []):
                c.run(f"{sudo} cp -rf {file} {user}/")

        if "authorized_keys" in settings:
            os.mkdir(f"/home/{os_user}/.ssh")
            with open(f"/home/{os_user}/.ssh/authorized_keys", "w") as f:
                for key in settings["authorized_keys"]:
                    f.write( key + "\n")

        c.run(f"chown -R {os_user}:{os_user} .")

@task
def keep_container(c):
    time.sleep(60*60*24*365)

@task
def start(c):
    build_environment(c)
    keep_container(c)
