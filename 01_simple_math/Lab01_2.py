#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab01_2
# 229223 Sec 001

millisec = int(input("Input milliseconds: ")) # Ex. 186400500

mil_day = 1000 * 60 * 60 * 24  # 86400000 millisec/day
day = millisec // mil_day      # => 2
dayms = millisec % mil_day     # => 2.157413194 

millisec -= day*mil_day        # => 13600500

mil_hour = 1000 * 60 * 60      # 3600000 millisec/hour
hour = millisec // mil_hour    # => 3
hourms = millisec % mil_hour   # => 3.777916667

millisec -= hour*mil_hour      # => 2800500

mil_min = 1000 * 60            # 60000 millisec/minute
min = millisec // mil_min      # => 46
minms = millisec % mil_min     # => 46.675

millisec -= min*mil_min        # => 40500

mil_sec = 1000
sec = millisec // mil_sec      # => 40
secms = millisec % mil_sec     # => 40.5

millisec -= sec*mil_sec        # => 500


#print(day,'day(s),', hour,'hour(s),', min,'minute(s),', sec,'second(s), and', millisec,'millisec(s)')
print(f"{day} day(s), {hour} hour(s), {min} min(s), {sec} second(s), and {millisec} millisec(s)")