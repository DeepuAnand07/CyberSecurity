import time
import matplotlib.pyplot as plt
from collections import Counter
from pynput import keyboard
from wordcloud import WordCloud
import threading

# File to store the keystrokes
log_file = "keylog.txt"

# Dictionary to store key press counts
key_counts = Counter()

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
                key_counts[key.char] += 1  # Count character keys
            else:
                special_key = f"[{key.name}]"
                f.write(special_key)
                key_counts[special_key] += 1  # Count special keys
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:  # Stop logging when 'esc' is pressed
        return False

# Function to generate bar chart
def visualize_key_frequencies():
    while True:
        if key_counts:
            plt.figure(figsize=(10, 5))
            keys, values = zip(*key_counts.most_common(10))  # Get top 10 pressed keys
            plt.bar(keys, values, color="blue")
            plt.xlabel("Keys")
            plt.ylabel("Frequency")
            plt.title("Key Press Frequency")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show(block=False)
            plt.pause(5)  # Show for 5 seconds
            plt.close()

        time.sleep(10)  # Update every 10 seconds

# Function to generate word cloud
def generate_wordcloud():
    while True:
        with open(log_file, "r") as f:
            text = f.read()

        if text:
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title("Key Press Word Cloud")
            plt.show(block=False)
            plt.pause(15)  # Show for 5 seconds
            plt.close()

        time.sleep(10)  # Update every 10 seconds

# Start visualization in separate threads
threading.Thread(target=visualize_key_frequencies, daemon=True).start()
threading.Thread(target=generate_wordcloud, daemon=True).start()

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
