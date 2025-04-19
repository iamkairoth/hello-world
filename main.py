#!/usr/bin/env python3
import subprocess
import shutil
import os

# Define supported languages and their execution details
LANGUAGES = [
    {
        "name": "Python",
        "file": "languages/python.py",
        "check_cmd": "python3",
        "run_cmd": ["python3", "languages/python.py"]
    },
    {
        "name": "C",
        "file": "languages/c.c",
        "check_cmd": "gcc",
        "run_cmd": ["gcc", "languages/c.c", "-o", "data/c"]
    },
    {
        "name": "Java",
        "file": "languages/java.java",
        "check_cmd": "javac",
        "run_cmd": ["javac", "languages/java.java"]
    },
    {
        "name": "JavaScript",
        "file": "languages/js.js",
        "check_cmd": "node",
        "run_cmd": ["node", "languages/js.js"]
    },
    {
        "name": "Ruby",
        "file": "languages/ruby.rb",
        "check_cmd": "ruby",
        "run_cmd": ["ruby", "languages/ruby.rb"]
    },
    {
        "name": "Go",
        "file": "languages/go.go",
        "check_cmd": "go",
        "run_cmd": ["go", "run", "languages/go.go"]
    },
    {
        "name": "Rust",
        "file": "languages/rust.rs",
        "check_cmd": "rustc",
        "run_cmd": ["rustc", "languages/rust.rs", "-o", "data/rust"]
    }
]

def check_runtime(lang):
    """Check if the required runtime/compiler is installed."""
    return shutil.which(lang["check_cmd"]) is not None

def run_program(lang):
    """Run the Hello World program for a given language."""
    try:
        if lang["name"] == "C":
            # Compile
            compile_result = subprocess.run(
                lang["run_cmd"],
                capture_output=True, text=True, check=True
            )
            # Execute
            run_result = subprocess.run(
                ["./data/c"],
                capture_output=True, text=True, check=True
            )
            return run_result.stdout.strip()
        if lang["name"] == "Rust":
            # Compile
            compile_result = subprocess.run(
                lang["run_cmd"],
                capture_output=True, text=True, check=True
            )
            # Execute
            run_result = subprocess.run(
                ["./data/rust"],
                capture_output=True, text=True, check=True
            )
            return run_result.stdout.strip()
        if lang["name"] == "Java":
            # Compile
            compile_result = subprocess.run(
                lang["run_cmd"],
                capture_output=True, text=True, check=True
            )
            # Execute
            run_result = subprocess.run(
                ["java", "-cp", "languages", "java"],
                capture_output=True, text=True, check=True
            )
            return run_result.stdout.strip()
        else:
            # Run interpreted languages directly
            result = subprocess.run(
                lang["run_cmd"],
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def main():
    # Create data/ directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    print("Hello World CLI")
    print("=============================")
    
    for lang in LANGUAGES:
        if not os.path.exists(lang["file"]):
            print(f"{lang['name']}: Source file not found")
            continue
        if not check_runtime(lang):
            print(f"{lang['name']}: Runtime not installed")
            continue
        
        print(f"\n{lang['name']} Output:")
        output = run_program(lang)
        print(output)

if __name__ == "__main__":
    main()