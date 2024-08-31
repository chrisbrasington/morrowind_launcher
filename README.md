# Morrowind Launcher Script

This script allows you to play The Elder Scrolls III: Morrowind using OpenMW while still tracking your playtime on Steam.

## Purpose

Since OpenMW is a "non-Steam" game, it won't track your playtime or show your status as playing Morrowind on Steam. By launching the official Morrowind game via Steam and keeping it on the launcher screen, Steam will track your playtime and show your status as playing "The Elder Scrolls III: Morrowind." The script automatically closes the Steam game when you exit OpenMW, saving you the hassle of manually closing both.

## Usage

1. Run the script:
   ```bash
   python3 mwlauncher.py
   ```
2. The script will:
   - Start Morrowind via Steam and keep it on the launcher.
   - Launch OpenMW for actual gameplay.
   - Automatically close the Steam instance of Morrowind when OpenMW quits.

## Requirements

- Steam with Morrowind installed
- OpenMW installed
- Python 3.x

---

This version explains the functionality and purpose succinctly while providing necessary instructions for use.
