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
    if os.path.exists(f"/home/{os_user}/.git"):
        return

    with open(settings_file) as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)

    c.run(f"chmod 755 /home/ubuntu")
    c.run(f"chown ubuntu:ubuntu /home/ubuntu")

    user_do = f"sudo -u {os_user}"
    user_home = f"/home/{os_user}"

    with c.cd(user_home):

        c.run(f"{user_do} cp /etc/skel/.profile /etc/skel/.bashrc ./")

        c.run(f"{user_do} mkdir main")
        with c.cd("main"):
            if "repo" in settings:
                repo = settings["repo"]
                c.run(f"{user_do} git clone {repo} .")

            for command in settings.get("commands", []):
                c.run(f"{user_do} {command}")

            for copy_file in settings.get("copy_files", []):
                copy_file = f"{user_home}/main/{copy_file}"
                dir_path = os.path.dirname(copy_file)
                orig_file_name = os.path.basename(copy_file)
                with open(copy_file) as f:
                    origin_content = f.read()
                for user in settings.get("users", []):
                    file_name = orig_file_name.replace("morimoto", user)
                    content = origin_content.replace("morimoto", user)
                    with open(f"{dir_path}/{file_name}", "w") as f:
                        f.write(content)
        for user in settings.get("users", []):
            c.run(f"cp -rf main {user}")

        if "authorized_keys" in settings:
            c.run(f"{user_do} mkdir -p /home/{os_user}/.ssh")
            c.run(f"{user_do} chmod 755 /home/{os_user}/.ssh")
            with open(f"/home/{os_user}/.ssh/authorized_keys", "w") as f:
                for key in settings["authorized_keys"]:
                    f.write( key + "\n")

            c.run(f"chown -R {os_user}:{os_user} .")

@task
def start_sshd(c):
    c.run("/usr/sbin/sshd -D")

@task
def start(c):
    build_environment(c)
    start_sshd(c)
