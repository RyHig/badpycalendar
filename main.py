#!/usr/bin/env python

import calendar
import datetime
import time
import os
import tkinter as tk
from tkhtmlview import HTMLLabel
from enum import Enum

SECONDS = 1000
NUMBER_OF_REPEATS = 5


# NOTE: This is dumb i get it... But i wanted to try the enum class.
# Would probably be better to just compare the int value instead of casting it to an enum.
# idc though.
class months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


def getMonthName(month_int: int) -> str:
    try:
        match months(month_int):
            case months.January:
                return "January"
            case months.February:
                return "February"
            case months.March:
                return "March"
            case months.April:
                return "April"
            case months.May:
                return "May"
            case months.June:
                return "June"
            case months.July:
                return "July"
            case months.August:
                return "August"
            case months.September:
                return "September"
            case months.October:
                return "October"
            case months.November:
                return "November"
            case months.December:
                return "December"
            case _:
                return "New month, new you."
    except:
        return "New month, new you."


class customCalendar(calendar.HTMLCalendar):
    weekday_abbr = ["M", "T", "W", "R", "F", "Sa", "Su"]

    # WARNING: I am not sure it is correct to inherit a class then completely
    # manipulate it. It feels wrong, but there didn't seem to be a way to get around this.
    def formatweekday(self, day):
        return '<th class="%s">%s</th>' % (
            self.cssclasses_weekday_head[day],
            self.weekday_abbr[day],
        )


def tkinter_update(root, counter=0):
    if counter == NUMBER_OF_REPEATS:
        os._exit(status=0)
    else:
        root.after(SECONDS, tkinter_update, root, counter + 1)


def main():
    curr_calendar = customCalendar()
    time_tuple = datetime.datetime.now().timetuple()
    width, height = 400, 400
    root = tk.Tk()
    # this doesn't do anything :^)
    root.title(f"{getMonthName(time_tuple[1])}, {time_tuple[0]}")
    # TODO: 2 screens of different sizes... Xrandr creates a 1920+2560 window (4480)
    # My initial hack was based on a screenwidth of the same size... Need to think
    # on this.
    x = root.winfo_screenwidth() - 400
    root.geometry(f"{width}x{height}+{x}+0")
    my_label = HTMLLabel(
        root, html=curr_calendar.formatmonth(time_tuple[0], time_tuple[1])
    )
    my_label.pack(expand=True)

    root.after(0, tkinter_update, root)
    root.mainloop()


if __name__ == "__main__":
    main()
