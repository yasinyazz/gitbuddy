# gitbuddy.py
import subprocess
import os

def run(command):
    """Run a shell command and print the output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    output = result.stdout or result.stderr
    print(output if output else "Done.")

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def main_menu():
    while True:
        clear()
        print("╔══════════════════════════╗")
        print("║       🐙  GitBuddy       ║")
        print("╠══════════════════════════╣")
        print("║  1. Clone a repo         ║")
        print("║  2. Stage & commit       ║")
        print("║  3. Create a branch      ║")
        print("║  4. Switch branch        ║")
        print("║  5. See history          ║")
        print("║  6. Push to remote       ║")
        print("║  7. Status dashboard     ║")
        print("║  q. Quit                 ║")
        print("╚══════════════════════════╝")

        choice = input("\nPick an option: ").strip().lower()

        if choice == '1':
            clone()
        elif choice == '2':
            stage_and_commit()
        elif choice == '3':
            create_branch()
        elif choice == '4':
            switch_branch()
        elif choice == '5':
            history()
        elif choice == '6':
            push()
        elif choice == '7':
            status_dashboard()
        elif choice == 'q':
            print("Bye!")
            break
        else:
            input("Invalid option. Press Enter to try again.")

def clone():
    url = input("Paste the repo URL: ").strip()
    run(f"git clone {url}")
    input("\nPress Enter to go back.")

def stage_and_commit():
    print("\n-- Current status --")
    run("git status")
    input("\nPress Enter to stage all changes (git add .) ...")
    run("git add .")
    message = input("Commit message: ").strip()
    run(f'git commit -m "{message}"')
    input("\nPress Enter to go back.")

def create_branch():
    name = input("New branch name: ").strip()
    run(f"git checkout -b {name}")
    input("\nPress Enter to go back.")

def switch_branch():
    run("git branch")
    name = input("\nBranch to switch to: ").strip()
    run(f"git checkout {name}")
    input("\nPress Enter to go back.")

def history():
    run("git log --oneline --graph --all")
    input("\nPress Enter to go back.")

def status_dashboard():
    clear()
    print("── Current branch ──")
    run("git branch --show-current")
    print("── Changed files ──")
    run("git status --short")
    print("── Last 5 commits ──")
    run("git log --oneline -5")
    input("\nPress Enter to go back.")

def push():
    run("git push")
    input("\nPress Enter to go back.")

if __name__ == "__main__":
    main_menu()
