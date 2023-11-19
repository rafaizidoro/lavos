from abc import ABC, abstractmethod

MON = "MON"
TUE = "TUE"
WED = "WED"
THU = "THU"
FRI = "FRI"
SAT = "SAT"
SUN = "SUN"

JAN = "JAN"
FEB = "FEB"
MAR = "MAR"
APR = "APR"
MAY = "MAY"
JUN = "JUN"
JUL = "JUL"
AUG = "AUG"
SEP = "SEP"
OCT = "OCT"
NOV = "NOV"
DEC = "DEC"

DAYS_OF_WEEK = [MON, TUE, WED, THU, FRI, SAT, SUN]
WEEKDAYS = [MON, TUE, WED, THU, FRI]
WEEKEND = [SAT, SUN]
MONTHS = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

class FormatStrategy(ABC):
    @abstractmethod
    def format_expression(self, expression: dict) -> str:
        pass


class UnixFormatStrategy(FormatStrategy):
    def format_expression(self, expression: dict) -> str:
        return "{minute} {hour} {day_of_month} {month} {day_of_week}".format(
            **expression
        )


class AwsFormatStrategy(FormatStrategy):
    def format_expression(self, expression: dict) -> str:
        match (expression["day_of_month"], expression["day_of_week"]):
            case (_, "*"):
                expression["day_of_week"] = "?"
            case ("*", _):
                expression["day_of_month"] = "?"
            case _:
                expression["day_of_week"] = "?"

        return "{minute} {hour} {day_of_month} {month} {day_of_week} {year}".format(
            **expression
        )


class Lavos:
    def __init__(self, format: str = "unix"):
        self.formater = (
            UnixFormatStrategy() if format == "unix" else AwsFormatStrategy()
        )

        self.expression = {
            "minute": "*",
            "hour": "*",
            "day_of_month": "*",
            "month": "*",
            "day_of_week": "*",
            "year": "*",
        }

        self.every_accum = None

    def every(self, value=1):
        self.every_accum = value
        return self

    def on(self, *args):
        weekdays = []
        months = []
        days = []

        # WEEKDAYS or WEEKEND
        if isinstance(args[0], list):
            args = args[0]

        for arg in args:
            if arg in DAYS_OF_WEEK:
                weekdays.append(str(arg))
            elif arg in MONTHS:
                months.append(str(arg))
            else:
                days.append(str(arg))

        if weekdays:
            self.expression["day_of_week"] = ",".join(weekdays)

        if months:
            self.expression["month"] = ",".join(months)

        if days:
            self.expression["day_of_month"] = ",".join(days)

        return self

    def of(self, *args):
        for arg in args:
            if arg not in MONTHS:
                raise ValueError("Invalid month: {}".format(arg))

        return self.on(*args)

    def at(self, time):
        hour, minute = time.split(":")

        self.expression["minute"] = str(int(minute))
        self.expression["hour"] = str(int(hour))

        return self

    def after(self, time):
        return self

    def _apply_every(self, key):
        if not self.every_accum:
            raise ValueError("Must call .every() before .{}".format(key))
        self.expression[key] = "*/" + str(self.every_accum)
        self.every_accum = None
        return self

    @property
    def days(self):
        return self._apply_every("day_of_month")

    @property
    def minutes(self):
        return self._apply_every("minute")

    @property
    def hours(self):
        return self._apply_every("hour")

    @property
    def month(self):
        return self._apply_every("month")

    @property
    def daily(self):
        self.expression["day_of_month"] = "*"
        self.expression["day_of_week"] = "*"

        return self

    @property
    def hourly(self):
        self.expression["hour"] = "*"
        self.expression["minute"] = "0"
        return self

    @property
    def monthly(self):
        self.expression["month"] = "*"
        return self

    @property
    def weekdays(self):
        self.expression["day_of_week"] = ",".join([MON, TUE, WED, THU, FRI])
        self.expression["day_of_month"] = self.default_value
        return self

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return self.dump()

    def dump(self):
        return self.formater.format_expression(self.expression)
