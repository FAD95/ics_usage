from datetime import date
import icalendar # $ pip install icalendar

ICS_PATH = "files/"
with open(ICS_PATH, 'r', encoding=('utf-8')) as f:

    today = date.today()
    calendar = icalendar.Calendar.from_ical(f.read())
    for event in calendar.walk('VEVENT'):
        if event.get('summary').startswith('EventSummaryName'):
            print(event.get('summary'))
            print(event.get('dtstart').dt)
            print(event.get('dtend').dt)
            print(event.get('dtend').dt-event.get('dtstart').dt)
