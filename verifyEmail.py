import re

#\w = [a-z|A-Z|0-9]

emailAddr = "mm@aol.com lo@.edu @realtime.org mcu@gmail.com"

print("Email Matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailAddr)))

