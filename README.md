# Terminal Workflow

<p align="center">
  <img src="twf.png" alt="Terminal Workflow logo" width="500">
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

MIT License

Copyright (c) 2026 sweur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
