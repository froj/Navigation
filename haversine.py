from math import *
import re


def haversin(theta):
    return (1 - cos(theta)) / 2


def haversine(lat1, lon1, lat2, lon2):
    return haversin(lat2 - lat1) + cos(lat1) * cos(lat2) * haversin(lon2 - lon1)

def haversine_deg(lat1, lon1, lat2, lon2):
    return haversine(radians(lat1), radians(lon1), radians(lat2), radians(lon2))

def distance(lat1, lon1, lat2, lon2):
    ''' in nautical miles. input in degrees.
    '''
    return degrees(2 * asin(sqrt(haversine_deg(lat1, lon1, lat2, lon2)))) * 60

def parse_coordinate(input_str):
    latitude = 0
    longitude = 0

    pattern = "^\s*(\d+)[°\s]+([0-5]??\d)(['\.\s])\s*(0?)(\d*)'?\"?\s*([NnSs-]?)\s*(\d+)[°\s]+([0-5]??\d)(['\.\s])\s*(0?)(\d*)'?\"?\s*([EeWw-]?)"
    result = re.match(pattern, input_str)

    if result:
        latitude = int(result.group(1))
        latitude += int(result.group(2)) / 60

        if result.group(3) == "'":
            if result.group(4) == '0' or int(result.group(5)) > 59:
                latitude += int(result.group(5)) / 60000
            else:
                latitude += int(result.group(5)) / 3600

        elif result.group(3) == ".":
            if not result.group(4) == '0':
                latitude += int(result.group(5)) / 60000

        direction = result.group(6)

        if direction == 'S' or direction == 's' or direction == '-':
            latitude = -latitude


        longitude = int(result.group(7))
        longitude += int(result.group(8)) / 60

        if result.group(9) == "'":
            if result.group(10) == '0' or int(result.group(11)) > 59:
                longitude += int(result.group(11)) / 60000
            else:
                longitude += int(result.group(11)) / 3600

        elif result.group(9) == ".":
            if not result.group(10) == '0':
                longitude += int(result.group(11)) / 60000

        direction = result.group(12)

        if direction == 'S' or direction == 's' or direction == '-':
            longitude = -longitude

    return (latitude, longitude)
