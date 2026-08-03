import tkinter as tk
from datetime import datetime

# Average global deaths per day (approximate)
DEATHS_PER_DAY = 170000

def get_death_estimate():
    now = datetime.now()

    seconds_passed = (
        now.hour * 3600 +
        now.minute * 60 +
        now.second
    )

    estimated = int((seconds_passed / 86400) * DEATHS_PER_DAY)

    chat.insert(tk.END, "You: How many people have died today?\n\n")
    chat.insert(
        tk.END,
        f"Bot: Approximately {estimated:,} people have died worldwide today.\n"
        "(This is an estimate based on the average number of deaths per day.)\n\n"
    )

root = tk.Tk()
root.title("World Death Counter Chat")
root.geometry("650x450")

chat = tk.Text(root, font=("Arial", 12), wrap="word")
chat.pack(padx=10, pady=10, fill="both", expand=True)

button = tk.Button(
    root,
    text="Ask",
    font=("Arial", 12),
    command=get_death_estimate
)
button.pack(pady=10)

root.mainloop()
