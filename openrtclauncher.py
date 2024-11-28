#!/usr/bin/env python3
import subprocess
import threading
import time
import os
import signal

def run_steam_game():
    """Launches the RollerCoaster Tycoon game via Steam."""
    try:
        subprocess.run(["xdg-open", "steam://rungameid/285310"])
    except subprocess.SubprocessError as e:
        print(f"Failed to launch Steam game: {e}")

def run_openrct2():
    """Launches OpenRCT2 and waits for it to exit."""
    try:
        process = subprocess.Popen(["openrct2"])
        process.wait()  # Wait until OpenRCT2 process ends
    except subprocess.SubprocessError as e:
        print(f"Failed to launch OpenRCT2: {e}")

def kill_steam_game():
    """Attempts to find and kill the RollerCoaster Tycoon 2 process."""
    try:
        while True:
            # Use pgrep to find the PID of the process by name
            try:
                pids = subprocess.check_output(
                    ["pgrep", "-f", "RCT.EXE"]
                ).strip().split()

                if pids:
                    for pid in pids:
                        os.kill(int(pid), signal.SIGTERM)
                        print(f"Killed Steam game with PID {pid.decode('utf-8')}")
                    break

            except subprocess.CalledProcessError:
                print("RollerCoaster Tycoon 2 process not found, perhaps it's already closed.")
                break

            time.sleep(1)

    except OSError as e:
        print(f"Failed to kill Steam game process: {e}")

if __name__ == "__main__":
    # Start both the Steam game and OpenRCT2 simultaneously
    steam_thread = threading.Thread(target=run_steam_game)
    openrct2_thread = threading.Thread(target=run_openrct2)

    steam_thread.start()
    openrct2_thread.start()

    # Wait for OpenRCT2 to finish
    openrct2_thread.join()

    # Then kill the Steam game
    kill_steam_game()

