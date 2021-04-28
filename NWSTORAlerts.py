import feedparser
from datetime import datetime, timedelta, timezone
from time import mktime
from dateutil.parser import parse

with open('process_alerts.txt') as processed_alerts_file:
    processed_alerts_data = processed_alerts_file.read()

for line in processed_alerts_data.

d = feedparser.parse("https://alerts.weather.gov/cap/us.php?x=0")
entries_count = len(d.entries)
#print (entries_count)
if entries_count == 0:
    print("No data downloaded from weather.gov.")
    quit()
posted_summaries = []
earliest_dt = datetime.now(timezone.utc).astimezone() - timedelta(minutes=20)
for entry in d.entries:
    entry_dt = parse(entry.updated)
    if entry_dt > earliest_dt and not (entry.summary in posted_summaries) and ("Tornado Warning" in entry.title):
        posted_summaries.append(entry.summary)
        #print("Earliest dt that should be reported: %s, entry updated: %s" % (earliest_dt, entry_dt))
        print("Warning: %s, %s" % (entry.cap_event, entry.title))
        print("Last Updated: %s, Expires: %s" % (entry.updated,entry.cap_expires))
        print("Summary: %s\n" % entry.summary)
        print("Unique ID: %s\n" % entry.id)
        print(entry)