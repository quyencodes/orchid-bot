from datetime import datetime, timezone, timedelta

"""
@param {string} unix - Unix timestamp
@param {string} format - Formatting of the Discord timestamp (refer to formatting dictionary)
@return {string} - Returns a dynamic date-time display in the discord text-channel
"""


def discord_timestamp(unix, format=None):
  # Discord Timestamp Formatting - https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa
  if format is None:
    return f"<t:{unix}>"

  formatting = {
    'default': '',
    'short_time': 't',
    'long_time': 'T',
    'short_date': 'd',
    'long_date': 'D',
    'short_both': 'f',
    'long_both': 'F',
    'relative': 'R'
  }
  return f"<t:{unix}:{formatting[format]}>"


"""
Recreation of https://www.unixtimestamp.com/ in a python function
@param {string} year - Number format for year (YYYY)
@param {string} month - Number format for month (MM)
@param {string} day - Number format for day (DD)
@param {string} hour - Number format for hour (HH)
@param {string} minutes - Number format for minutes (MM)
@param {string} seconds - Number format for seconds (SS)
@return {string} - unix timestamp code
"""


def utc_unix_timestamp(year, month, day, hour, minutes, seconds):
  dt = datetime(int(year), int(month), int(
    day), int(hour), int(minutes), int(seconds))

  dt_utc = dt.replace(tzinfo=timezone.utc)

  timestamp = int(dt_utc.timestamp())

  return timestamp


"""
@param {string} - year
@param {string} - month
@param {string} - day
@return {string} - this week's sunday datetime object
"""


def get_day_of_week(selectedDay):
  dayMap = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
  }

  # Get the utc reset time
  current_utc_time = datetime.now(timezone.utc)

  # Get the difference between Sunday and the Current Day
  days_until_y = (dayMap[selectedDay] - current_utc_time.weekday() + 1) % 7

  # Find the Sunday datetime object
  datetime_obj = current_utc_time + timedelta(days=days_until_y)

  return datetime_obj
