import string
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox

def analyze_word_count():
    # Read the selected file
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Tokenize the text
        translator = str.maketrans('', '', string.punctuation)
        words = text.lower().translate(translator).split()

        # Calculate word count
        word_count = Counter(words)

        # Total word count
        total_words = sum(word_count.values())

        # Most common words
        most_common = word_count.most_common(5)

        # Display analysis results
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Total words: {total_words}\n")
        results_text.insert(tk.END, "Most common words:\n")
        for word, count in most_common:
            results_text.insert(tk.END, f"{word} - {count}\n")
    except IOError:
        messagebox.showerror("Error", "Failed to read the file.")

# Create the main window
window = tk.Tk()
window.title("Word Count Analyzer")

# Create the file selection button
select_button = tk.Button(window, text="Select File", command=analyze_word_count)
select_button.pack(pady=10)

# Create the text area to display the results
results_text = tk.Text(window, height=10, width=50)
results_text.pack(pady=10)

# Start the main event loop
window.mainloop()
