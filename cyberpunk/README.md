# Cyberpunk Tabletop Widgets

We've got our favorite utilities for netrunning, hacking, and rocking into the future.

## Requirements and Running
Our Cyberpunk utilities are easy and breezy to run -- and that's by design. We're TT gaming as netrunners, we don't need to _be_ netrunners to use these tools.

Right now `map_grid.py` is the only thing that uses a non-standard Python library, but we've got a `requirements.txt` for what we need. To install: 
```pip install -r requirements.txt```

## SUDOKU GENERATOR

This has been scaled out for the public! Grab (your own version here!)[https://github.com/lasermatts/PyDoku]

What netrunner doesn't love math, command lines, and puzzles?

The `python sudoku.py` script runs in your command line (because hackers do their morning puzzle in the terminal) and outputs a 4x4, 6x6, or 9x9 puzzle. 

## Map Grid

This lays the groundwork for a more complex battlemap tool. Right now your MC moves around the map, and you have a few maps to choose from. Highly customizable and expandible and there are a ton of directions to take this in.

All it takes is a `python map_grid.py` in Terminal and you're off to the races choom :) 

## Dice Roller

A TT Gaming Classic, brought to you through your command line. Open a terminal, provide a number of dice and their sidedness and get a result. It'll even check if you've provided a valid input.

Simple and easy to launch with a `python dice_roller.py` in the command line.