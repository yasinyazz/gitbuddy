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

## Installation (Linux — Arch/Manjaro)

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

## Installation (Ubuntu / Debian)

1. Clone this repo:
   git clone https://github.com/yasinyazz/gitbuddy.git
   cd gitbuddy

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

## Installation (any Linux — no pip needed)

1. Clone this repo and go into the folder
2. Run this to create a shortcut:
```
   echo "alias gitbuddy='python3 $(pwd)/gitbuddy.py'" >> ~/.bashrc
   source ~/.bashrc
```
3. Type `gitbuddy` from anywhere!

## Usage

Just run `gitbuddy` in any folder that has a Git repo and follow the menu.
