import pytz
from pytz import timezone
import iso8601

def destinationtime(start_tz, end_tz, start_time, flight_min):
	starting_time = iso8601.parse_date(start_time)
	start = timezone(start_tz)
	end = timezone(end_tz)

	start_dt = start.localize(starting_time)

	end_time = end.normalize(start_dt + timedelta(minutes=flight_min))

	return end_time

if __name__ == '__main__':
	print destinationtime("America/Los_Angeles", "US/Eastern", "2016-02-25T14:30:00", 300)