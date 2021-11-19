#!/usr/bin/env python3.7

import threading
import time
import tkinter as tk


class CountdownTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("425x200")
        self.root.title("Countdown timer")

        self.time_entry = tk.Entry(self.root, font=("Open sans", 26))
        self.time_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.start_button = tk.Button(self.root, font=(
            "Open sans", 26), text="Start", command=self.start_thread)
        self.start_button.grid(row=1, column=0, padx=1, pady=1)

        self.stop_button = tk.Button(self.root, font=(
            "Open sans", 26), text="Stop", command=self.stop_thread)
        self.stop_button.grid(row=1, column=1, padx=1, pady=1)

        self.time_label = tk.Label(self.root, font=(
            "Open sans", 26), text="Time: 00:00:00")
        self.time_label.grid(row=2, column=0, columnspan=2, padx=1, pady=1)

        self.stop_loop = False

        self.root.mainloop()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours, minutes, seconds = string_split[0], string_split[1], string_split[2]
        elif len(string_split) == 2:
            minutes, seconds = string_split[0], string_split[1]
        elif len(string_split) == 1:
            seconds = string_split[0]
        else:
            print("Invalid time format!")
            return

        full_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

        while full_seconds > 0 and not self.stop_loop:
            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(
                text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()

            time.sleep(1)
            full_seconds -= 1

        if not self.stop_loop:
            self.time_label.config(
                text="Time is up!")
            self.root.update()

            print("CountdownTimer: TIME IS OVER!")

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def stop_thread(self):
        self.stop_loop = True
        self.time_label.config(text="Time: 00:00:00")


if __name__ == "__main__":
    CountdownTimer()
