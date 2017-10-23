KAKURO
by Christian Mitrofan

A simple kakuro game written with python 2.7.The puzzle is solved as a csp(constraint satisfaction problem)
using some files from an AI class i took at university

Variables: Xi_j All the white blocks with their position

Domains: For all the variables {1,2,3...,9}

Neighbors: For every variable the neighbors are the other variables that are in the same row or column

Constraints:All the variables in a line(rows and columns) must be different and
the sum (of all the variables) of a row must equal to the grey block at the start of the row,
the sum of a column must equal to the grey block above the column

For the GUI I used tkinder.

*Entry widget for every block(even the grey and black ones)

*Grid for layout management of the entry and button widgets

*Canvas widget for the victory screen

I used py2exe to turn the program to an executable
