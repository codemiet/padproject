import datetime


def get_booleanParameter(prompt):
    while True:
        try:
            return {"true": True, "y": True, "yes": True, "false": False, "n": False, "no": False}[
                input(prompt).lower()]
        except KeyError:
            print("Invalid input please enter Yes or No!")


def get_intParameter(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a station ID!")


def get_dateParameter(prompt):
    while True:
        try:
            date = datetime.date.fromisoformat(input(prompt))
            return str(date)
        except ValueError or TypeError:
            print("That's not a date!")
