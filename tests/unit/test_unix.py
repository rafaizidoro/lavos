import pytest

from lavos import FEB, JAN, MON, THU, WEEKDAYS, WEEKEND, Lavos


def test_every_minute():
    lav = Lavos()
    cron = lav.every(15).minutes
    assert str(cron) == "*/15 * * * *"


def test_every_hour():
    lav = Lavos()
    cron = lav.every(2).hours
    assert str(cron) == "* */2 * * *"


def test_at_hour():
    lav = Lavos()
    cron = lav.at("12:00").daily
    assert str(cron) == "0 12 * * *"


def test_on_weekday():
    lav = Lavos()
    cron = lav.on(MON).hourly
    assert str(cron) == "0 * * * MON"


def test_on_multiple_weekdays():
    lav = Lavos()
    cron = lav.on(MON, THU).hourly
    assert str(cron) == "0 * * * MON,THU"


def test_every_on_chaining():
    lav = Lavos()
    cron = lav.every(2).hours.on(MON, THU)

    assert str(cron) == "* */2 * * MON,THU"


def test_every_at_chaining():
    lav = Lavos()
    cron = lav.at("15:30").on(THU)
    assert str(cron) == "30 15 * * THU"


def test_weekdays():
    lav = Lavos()
    cron = lav.at("15:30").on(WEEKDAYS)
    assert str(cron) == "30 15 * * MON,TUE,WED,THU,FRI"


def test_weekend():
    lav = Lavos()
    cron = lav.every(2).hours.on(WEEKEND)
    assert str(cron) == "* */2 * * SAT,SUN"


def test_every_with_days():
    lav = Lavos()
    cron = lav.every(3).days
    assert str(cron) == "* * */3 * *"


def test_on_day_of_month():
    lav = Lavos()
    cron = lav.on(15, 16).of(FEB)
    assert str(cron) == "* * 15,16 FEB *"


def test_every_hour_of_weekdays():
    lav = Lavos()
    cron = lav.on(WEEKDAYS).every(3).hours
    assert str(cron) == "* */3 * * MON,TUE,WED,THU,FRI"
