from functions import timestamp

dmt_data = [{
    'name': 'Primary Weapon / Secondary Equipment',
    'start_time': {
      'year': '2023',
      'month': '12',
      'day': '30',
      'hour': '00',
      'minutes': '00',
      'seconds': '00',
    },
    'end_time': {
      'year': '2024',
      'month': '1',
      'day': '30',
      'hour': '23',
      'minutes': '59',
      'seconds': '00',
    },
  },
  {
    'name': 'Tops, Bottoms, Overalls, and Capes',
    'start_time': {
      'year': '2024',
      'month': '01',
      'day': '06',
      'hour': '00',
      'minutes': '00',
      'seconds': '00',
    },
    'end_time': {
      'year': '2024',
      'month': '01',
      'day': '06',
      'hour': '23',
      'minutes': '59',
      'seconds': '00',
    },
  },
    {
    'name': 'Shoes',
    'start_time': {
      'year': '2024',
      'month': '01',
      'day': '13',
      'hour': '00',
      'minutes': '00',
      'seconds': '00',
    },
    'end_time': {
      'year': '2024',
      'month': '01',
      'day': '13',
      'hour': '23',
      'minutes': '59',
      'seconds': '00',
    },
  },
    {
    'name': 'Accessories + Emblem',
    'start_time': {
      'year': '2024',
      'month': '01',
      'day': '20',
      'hour': '00',
      'minutes': '00',
      'seconds': '00',
    },
    'end_time': {
      'year': '2024',
      'month': '01',
      'day': '20',
      'hour': '23',
      'minutes': '59',
      'seconds': '00',
    },
  },
    {
    'name': 'Gloves',
    'start_time': {
      'year': '2024',
      'month': '01',
      'day': '27',
      'hour': '00',
      'minutes': '00',
      'seconds': '00',
    },
    'end_time': {
      'year': '2024',
      'month': '01',
      'day': '27',
      'hour': '23',
      'minutes': '59',
      'seconds': '00',
    },
  },
    {
    'name': 'Hats',
    'start_time': {
      'year': '2024',
      'month': '02',
      'day': '03',
      'hour': '00',
      'minutes': '00',
      'seconds': '00',
    },
    'end_time': {
      'year': '2024',
      'month': '02',
      'day': '03',
      'hour': '23',
      'minutes': '59',
      'seconds': '00',
    },
  }
]

class DMT(object):
  def __init__(self, name, start_time, end_time):
    self.name = name
    self.start_time = start_time
    self.end_time = end_time

  def get_name(self):
    return self.name

  def get_discord_timestamp(self):
    start_year, start_month, start_day, start_hour, start_min, start_seconds = self.start_time['year'], self.start_time['month'], self.start_time['day'], self.start_time['hour'], self.start_time['minutes'], self.start_time['seconds']
    start_unixcode = timestamp.utc_unix_timestamp(start_year, start_month, start_day, start_hour, start_min, start_seconds)

    end_year, end_month, end_day, end_hour, end_min, end_seconds = self.end_time['year'], self.end_time['month'], self.end_time['day'], self.end_time['hour'], self.end_time['minutes'], self.end_time['seconds']
    end_unixcode = timestamp.utc_unix_timestamp(end_year, end_month, end_day, end_hour, end_min, end_seconds)

    return timestamp.discord_timestamp(start_unixcode) + '-' + timestamp.discord_timestamp(end_unixcode, 'short_time') + f"\t({timestamp.discord_timestamp(start_unixcode, 'relative')})"


# exports
weapon = DMT(dmt_data[0]['name'], dmt_data[0]['start_time'], dmt_data[0]['end_time'])

overall = DMT(dmt_data[1]['name'], dmt_data[1]['start_time'], dmt_data[1]['end_time'])

shoes = DMT(dmt_data[2]['name'], dmt_data[2]['start_time'], dmt_data[2]['end_time'])

accessories = DMT(dmt_data[3]['name'], dmt_data[3]['start_time'], dmt_data[3]['end_time'])

gloves = DMT(dmt_data[4]['name'], dmt_data[4]['start_time'], dmt_data[4]['end_time'])

hats = DMT(dmt_data[5]['name'], dmt_data[5]['start_time'], dmt_data[5]['end_time'])
