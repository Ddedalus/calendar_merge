import os

import requests
from ics import Calendar

f_url = "http://tabula.warwick.ac.uk/api/v1/timetable/calendar/{}.ics"
hubert_url = f_url.format(os.environ['HUBERT_TABULA_ID'])
c = Calendar(requests.get(hubert_url).text)

e = list(c.timeline)[-1]
print("Event '{}' started {}".format(e.name, e.begin.humanize()))
