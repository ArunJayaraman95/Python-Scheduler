# Scheduler :school:
## Overview
Program to create all permutations of schedules possible for my university. When registering for classes, instead of having to go back and forth to see if different class sections conflict with the other class sections, why not put all possible considerations for those sections into a program that generates all possible schedules for you with no time conflicts?!

## Built With
* Python
* Tkinter

## How it works
1. Get list of classes with attributes of `name`,`startTime`,`endTime`,`days`. An example Course would be `Course("Algorithm Analysis", 1730, 1845, [2,4])`. Notice that the `days` parameter is an array of numbers. This corresponds to Monday-Friday with Monday as 1 and Friday as 5. Additionally, the times are provided as integers and are in military time. I initially had this for ease of splitting my grid in tkinter, but I may change the data type to a string later.
2. Calculate all possible combinations of classes (by going thru each classes and included it or not in the check)
3. Check if there are conflicts in any classes for any given combination
4. Only keep non-conflicting schedules
5. To further reduce, only keep schedules that have the max amount of classes. For example, if all non-conflicting combos had from 1-6 courses, only keep those with 6 courses. This is regardless of input. Inputting 10 classes will only yield the maximum out of *accepted* combinations which may be less than 10. 
6. Display these "optimal" classes in a GUI for visual help.
