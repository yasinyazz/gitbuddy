# 🐙 GitBuddy

A beginner-friendly Git helper that runs in your terminal.  
No more memorising commands — just pick from a menu!

## What it does

- Clone a repo
- Stage & commit changes
- Create and switch branches
- View your commit history
- Push to remote
- Status dashboard (current branch, changed files, recent commits)

## Requirements

- Python 3
- Git installed on your system

---

## Installation

### 🐧 Linux — Arch / Manjaro

1. Clone this repo:
```
   git clone https://github.com/yasinyazz/gitbuddy.git
   cd gitbuddy
```
2. Install pipx if you don't have it:
```
   sudo pacman -S python-pipx
```
3. Install GitBuddy:
```
   pipx install --editable .
```
4. Run it from anywhere:
```
   gitbuddy
```

---

### 🐧 Linux — Ubuntu / Debian / Mint

1. Clone this repo:
```
   git clone https://github.com/yasinyazz/gitbuddy.git
   cd gitbuddy
```
2. Install pip if you don't have it:
```
   sudo apt install python3-pip
```
3. Install GitBuddy:
```
   pip install --editable .
```
4. Run it from anywhere:
```
   gitbuddy
```

---

### 🐧 Linux — any distro (no pip needed)

1. Clone this repo and go into the folder:
```
   git clone https://github.com/yasinyazz/gitbuddy.git
   cd gitbuddy
```
2. Run this to create a shortcut:
```
   echo "alias gitbuddy='python3 $(pwd)/gitbuddy.py'" >> ~/.bashrc
   source ~/.bashrc
```
3. Type `gitbuddy` from anywhere!

---

### 🪟 Windows

1. **Install Python** if you don't have it:
   Download from [python.org/downloads](https://www.python.org/downloads/)  
   ⚠️ During install, tick **"Add Python to PATH"** — this is easy to miss!

2. **Install Git** if you don't have it:
   Download from [git-scm.com/download/win](https://git-scm.com/download/win)  
   Use all the default options during install.

3. **Open Command Prompt or PowerShell** and clone this repo:
```
   git clone https://github.com/yasinyazz/gitbuddy.git
   cd gitbuddy
```

4. Install GitBuddy:
```
   pip install --editable .
```

5. Run it from anywhere:
```
   gitbuddy
```

   If `gitbuddy` isn't recognised, try:
```
   python -m gitbuddy
```

#### Windows — no install option

If you just want to try it without installing:
```
python gitbuddy.py
```
Run this from inside the `gitbuddy` folder. No setup needed.

---

## Usage

Run `gitbuddy` in any folder that has a Git repo and follow the menu.

## Troubleshooting

| Problem | Fix |
|---|---|
| `gitbuddy: command not found` | Try closing and reopening your terminal |
| `python not found` on Windows | Make sure "Add Python to PATH" was ticked during Python install |
| `pip not found` on Linux | See your distro's install section above |
| Push asks for password | Use a GitHub Personal Access Token, not your GitHub password — [generate one here](https://github.com/settings/tokens/new) |
