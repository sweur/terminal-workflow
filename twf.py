#!/usr/bin/env python3
import sys
import json
import subprocess
from pathlib import Path

CONFIG_PATH = Path.home() / ".wf" / "workflows.json"

def load_workflows():
    if not CONFIG_PATH.exists():
        return {}
    return json.loads(CONFIG_PATH.read_text())

def save_workflows(workflows):
    CONFIG_PATH.parent.mkdir(exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(workflows, indent=2))

def run_workflow(name, workflows):
    if name not in workflows:
        print(f"no workflow named '{name}'")
        return
    for cmd in workflows[name]:
        print(f"$ {cmd}")
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            print(f"failed: {cmd}")
            break

def add_workflow(name, workflows):
    print(f"enter commands for '{name}', one per line, blank line to finish:")
    commands = []
    while True:
        line = input("> ")
        if not line.strip():
            break
        commands.append(line)
    workflows[name] = commands
    save_workflows(workflows)
    print(f"saved '{name}' with {len(commands)} step(s)")

def main():
    workflows = load_workflows()
    if len(sys.argv) < 2:
        print("usage: twf <name> | twf list | twf add <name>")
        return

    command = sys.argv[1]
    if command == "list":
        for name in workflows:
            print(name)
    elif command == "add":
        if len(sys.argv) < 3:
            print("usage: wf add <name>")
            return
        add_workflow(sys.argv[2], workflows)
    else:
        run_workflow(command, workflows)

if __name__ == "__main__":
    main()