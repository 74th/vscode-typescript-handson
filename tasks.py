import os
import os.path
import time
import json

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

        with open(f"{user_home}/main/.vscode/launch.json") as f:
            launch_json = json.load(f)
        for i, user in enumerate(settings.get("users", [])):
            for n in [0, 1, 2]:
                d = dict(launch_json["configurations"][n])
                d["name"] = d["name"].replace("morimoto", user)
                if "env" in d:
                    d["env"]["PORT"] = str(8080 + i)
                if "url" in d:
                    d["url"] = d["url"].replace("8080", str(8080 + i))
                launch_json["configurations"].append(d)
        with open(f"{user_home}/main/.vscode/launch.json", "w") as f:
            json.dump(launch_json, f, indent=2, separators=(",", ": "))

        with open(f"{user_home}/main/.vscode/tasks.json") as f:
            tasks_json = json.load(f)
        for i, user in enumerate(settings.get("users", [])):
            for n in [2, 3]:
                d = dict(tasks_json["tasks"][n])
                d["label"] = d["label"].replace("morimoto", user)
                d["args"] = [a.replace("morimoto", user) for a in d["args"]]
                tasks_json["tasks"].append(d)
        with open(f"{user_home}/main/.vscode/tasks.json", "w") as f:
            json.dump(tasks_json, f, indent=2, separators=(",", ": "))

        for user in settings.get("users", []):
            c.run(f"cp -rf main {user}")

        if "authorized_keys" in settings:
            c.run(f"{user_do} mkdir -p /home/{os_user}/.ssh")
            c.run(f"{user_do} chmod 755 /home/{os_user}/.ssh")
            with open(f"/home/{os_user}/.ssh/authorized_keys", "w") as f:
                for key in settings["authorized_keys"]:
                    f.write(key + "\n")

            c.run(f"chown -R {os_user}:{os_user} .")


@task
def start_sshd(c):
    c.run("/usr/sbin/sshd -D")


@task
def start(c):
    build_environment(c)
    start_sshd(c)
