# NANNY CARE

## By solution makers

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)

## Description

An application where parents/guardians can easily get nannies to take care of their kids.

## Requirements

A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

-Python version 3.8
    -Django
    -Pip
    -virtualenv

## Installation

Open Terminal {Ctrl+Alt+T} on ubuntu
git clone `https://github.com/John-Njau/Nanny-Care.git`
cd
code . or atom . based on prefered text editor

## Running Project

On terminal where you have opened the cloned project
`sudo pip3 install virtualenv`

To install virtual enviroment
 `virtualenv venv`

To create virtual enviroment
`source venv/bin/activate`

To activate virtual enviroment
`pip install -r requirements.txt`

To install requirements
Setup your database User, Password, Host, Port and Database Name.
`make makemigrations`

To create migrations
`make migrate`

To migrate database  
`make` - to start the server

## Running Tests

To run test for the project
`$ make test`

## Technologies Used

python3.8

django

HTML

css

Javascript

Cloudninary (for hosting images)

Heroku (for hosting the project)

## Licence

MIT License

Copyright (c) [2022] [Mary Atieno,John Njau,Abigael Wachira,Kate Vanili,Abdi Ali]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
