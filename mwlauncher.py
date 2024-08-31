import subprocess
import threading
import time
import os
import signal

def run_steam_game():
    """Launches the Morrowind game via Steam."""
    try:
        subprocess.run(["xdg-open", "steam://rungameid/22320"])
    except subprocess.SubprocessError as e:
        print(f"Failed to launch Steam game: {e}")

def run_openmw():
    """Launches OpenMW and waits for it to exit."""
    try:
        process = subprocess.Popen(["openmw"])
        process.wait()  # Wait until OpenMW process ends
    except subprocess.SubprocessError as e:
        print(f"Failed to launch OpenMW: {e}")

def kill_steam_game():
    """Attempts to find and kill the Morrowind process."""
    try:
        while True:
            # Use pgrep to find the PID of the process by name
            try:
                pids = subprocess.check_output(
                    ["pgrep", "-f", "Morrowind Launcher.exe"]
                ).strip().split()

                if pids:
                    for pid in pids:
                        os.kill(int(pid), signal.SIGTERM)
                        print(f"Killed Steam game with PID {pid.decode('utf-8')}")
                    break

            except subprocess.CalledProcessError:
                print("Morrowind process not found, perhaps it's already closed.")
                break

            time.sleep(1)

    except OSError as e:
        print(f"Failed to kill Steam game process: {e}")

if __name__ == "__main__":
    # Start both the Steam game and OpenMW simultaneously
    steam_thread = threading.Thread(target=run_steam_game)
    openmw_thread = threading.Thread(target=run_openmw)

    steam_thread.start()
    openmw_thread.start()

    # Wait for OpenMW to finish
    openmw_thread.join()

    # Then kill the Steam game
    kill_steam_game()

