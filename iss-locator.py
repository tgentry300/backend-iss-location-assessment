#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ISS locator
"""
__author__ = "tgentry300"

import requests
import turtle
import time

# from pprint import pprint


def astronauts():
    """Finds number and location of astronauts"""
    r = requests.get('http://api.open-notify.org/astros.json')
    print "Number of Astronauts: {}".format(r.json()['number'])

    for person in r.json()['people']:
        print "Person: {}\nCraft: {}".format(person['name'], person['craft'])


def get_station_coords():
    """Gets station coords and time, returns these"""
    coords = []
    r = requests.get('http://api.open-notify.org/iss-now.json')
    latitude = r.json()['iss_position']['latitude']
    longitude = r.json()['iss_position']['longitude']
    timestamp = r.json()['timestamp']
    coords.append(latitude)
    coords.append(longitude)

    return coords, timestamp


def turtle_to_coords():
    """sets turtle up"""
    space_station = turtle.Turtle()
    yellow_dot = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(700, 350)
    screen.bgpic('map.gif')
    screen.addshape('iss.gif')
    screen.setworldcoordinates(-180, -180, 180, 180)

    space_station.shape('iss.gif')
    coordinates = get_station_coords()[0]

    space_station.goto(float(coordinates[1]), float(coordinates[0]))

    yellow_dot.setpos(-86.1581, 39.7684)
    yellow_dot.dot('yellow')
    screen.exitonclick()


def find_indy_time():
    # payload = {'lat': -86.1581, 'lon': 39.7684}
    payload = {'lat': 50, 'lon': 50}
    r = requests.get('http://api.open-notify.org/iss-pass.json',
                     params=payload)
    print time.ctime(r.json()['request']['datetime'])


def main():
    astronauts()
    print get_station_coords()
    find_indy_time()
    turtle_to_coords()


if __name__ == '__main__':
    main()
