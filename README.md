# twf

<p align="center">
  <img src="twf.jpeg" alt="Terminal Workflow logo" width="500">
</p>

Terminal Workflow (twf) is a tiny CLI for chaining shell commands you run all the time.

Define a sequence once under a name, then run it with `twf <name>`
instead of retyping or copy-pasting the same steps every time.

## Usage

Add a workflow:

    python3 twf.py add deploy

You'll be prompted for commands, one per line. Blank line to finish.

Run it:

    python3 twf.py deploy

List saved workflows:

    python3 twf.py list

## How it works

Workflows are stored in `~/.twf/workflows.json` as a list of shell
commands per name, run in order. If a step fails (nonzero exit),
execution stops there instead of continuing blind.

## Requirements

Python 3.

## License

MIT
