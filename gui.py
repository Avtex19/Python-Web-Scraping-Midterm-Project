import tkinter as tk
from tkinter import ttk
import pandas as pd
from utils.analyzer import most_common_tag, most_quoted_author, average_tags_per_quote
from utils.file_handler import load_from_json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class QuoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Quote Explorer")

        self.data = pd.DataFrame(load_from_json("output/quotes.json"))

        self.create_widgets()
        self.display_stats()

    def create_widgets(self):
        # Table
        self.tree = ttk.Treeview(self.master, columns=("Text", "Author", "Tags"), show='headings')
        self.tree.heading("Text", text="Text")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Tags", text="Tags")

        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=(row["text"], row["author"], ", ".join(row["tags"])))

        self.tree.pack(expand=True, fill="both")

        # Stats
        self.stats_label = tk.Label(self.master, text="", justify=tk.LEFT, font=("Arial", 12))
        self.stats_label.pack(pady=10)

        # Plot
        self.plot_btn = tk.Button(self.master, text="Show Tag Frequency", command=self.plot_tags)
        self.plot_btn.pack(pady=5)

    def display_stats(self):
        tag, count = most_common_tag(self.data.to_dict(orient="records"))
        author, author_count = most_quoted_author(self.data.to_dict(orient="records"))
        avg = average_tags_per_quote(self.data.to_dict(orient="records"))

        self.stats_label.config(text=f"📌 Most Common Tag: {tag} ({count} times)\n"
                                     f"👤 Most Quoted Author: {author} ({author_count} quotes)\n"
                                     f"🏷️ Average Tags per Quote: {avg:.2f}")

    def plot_tags(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        tag_counts = {}
        for tags in self.data['tags']:
            for tag in tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        tags, counts = zip(*sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10])

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(range(len(tags)), counts)
        ax.set_title("Top 10 Tags")
        ax.set_ylabel("Frequency")
        ax.set_xticks(range(len(tags)))
        ax.set_xticklabels(tags, rotation=45, ha='right')

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
