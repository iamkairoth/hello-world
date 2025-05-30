# Hello World CLI

## Table of Contents

- Overview
- Background
- How It Works
- Supported Languages
- Project Structure
- Installation and Setup
- Installing Language Runtimes

## Overview

This project is a command-line interface (CLI) tool that demonstrates the classic "Hello, World" program in multiple programming languages. Written in Python, the tool orchestrates the execution of "Hello, World" programs in Python, C, Java, JavaScript, Ruby, Go, and Rust, displaying their outputs in the terminal. It automatically detects installed language runtimes and handles execution seamlessly, making it easy to compare how different languages print "Hello, World."

## Background

This project marks a new beginning, blending my passion for coding and storytelling. "Hello, World" isn’t just a program—it’s my journey from rock bottom to rebirth, shared through code, poetry, and transformation. Join me on Substack, where I explore coding tutorials, poetry, personal growth, and more with 2 free posts and 1 paid deep dive each week. Subscribe to support this adventure and dive into sections like Code, Write, and Unravel: https://iamkairoth.substack.com/p/hello-world

## How It Works

The CLI is driven by a Python script (`main.py`) that:

- Checks for installed runtimes/compilers (e.g., `python3`, `gcc`, `javac`) using the `shutil.which` function.
- Executes each language's "Hello, World" program stored in the `languages/` directory using Python's `subprocess` module.
- Displays the output for each language, clearly labeled, in the terminal.
- Handles errors gracefully, skipping languages with missing runtimes or source files.

## Supported Languages

- **Python**: Runs via `python3`.
- **C**: Compiles and runs using `gcc`.
- **Java**: Compiles with `javac` and runs with `java`.
- **JavaScript**: Runs via `node`.
- **Ruby**: Runs via `ruby`.
- **Go**: Runs via `go run`.
- **Rust**: Compiles and runs using `rustc`.
- \[More languages to be added soon\]

## Project Structure

```
hello-world/
├── main.py                 # Main Python CLI script
├── languages/              # Directory for language-specific code
│   ├── helloWorld.py       # Python Hello World
│   ├── c.c                 # C Hello World
│   ├── HelloWorld.java     # Java Hello World
│   ├── helloWorld.js       # JavaScript Hello World
│   ├── ruby.rb             # Ruby Hello World
│   ├── go.go               # Go Hello World
│   ├── rust.rs             # Rust Hello World
├── data/                   # Directory for data
│   ├── c                   # C Data
│   ├── rust                # Rust Data
└── README.md               # This file
```

## Installation and Setup

To run the CLI, you need Python 3 and the runtimes/compilers for the desired languages. Below is a guide to set up the project on a Unix-like system (e.g., Ubuntu, macOS). For Windows, use equivalent package managers or installers.

### Prerequisites

- **Python 3** (required to run `main.py`):

  ```bash
  sudo apt install python3  # Ubuntu/Debian
  ```

- Clone or create the project directory:

  ```bash
  mkdir hello-world
  cd hello-world
  mkdir languages
  ```

### Set Up the CLI

1. Save the `main.py` script and language files (`helloWorld.py`, `c.c`, `HelloWorld.java`, etc.) in the project directory.

2. Make `main.py` executable:

   ```bash
   chmod +x main.py
   ```

3. Run the CLI:

   ```bash
   ./main.py
   ```

## Installing Language Runtimes

Install the runtimes/compilers for the supported languages. Below are commands for Ubuntu/Debian. For macOS, replace `apt` with `brew`. For other systems, consult the language's official documentation.

- **C (gcc)**:

  ```bash
  sudo apt install gcc
  ```

- **Java (OpenJDK)**:

  ```bash
  sudo apt install openjdk-17-jdk
  ```

- **JavaScript (Node.js)**:

  ```bash
  sudo apt install nodejs
  ```

- **Ruby**:

  ```bash
  sudo apt install ruby
  ```

- **Go**:

  ```bash
  sudo apt install golang
  ```

- **Rust**:

  ```bash
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  source $HOME/.cargo/env
  ```