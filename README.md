# COVID-19-Dashboard-NL
This dashboard shows the amount of reported COVID-19 cases in the Netherlands. This website is still in development and can be viewed at [coronaperdag.nl](https://coronaperdag.nl).

![Slide_though_time](https://github.com/jordy-u/COVID-19-Dashboard-NL/blob/master/doc/images/scroll_through_time.gif)

## Goal
The goal of this project is to show people how the corona virus (SARS-CoV-2) has developed itself in the Netherlands. This is done in a unque way: Users can to scroll through time and see how the virus has spread in every city.

## Data
Data used for this site comes from the RIVM. The RIVM updates her website on a daily basis, but remove older information as well. This project gets its data from this resitory: [CoronaWatchNL](https://github.com/J535D165/CoronaWatchNL).

## Repository structure
The most important folders are:

## public
This folder is accessible on the webserver.

## Backend
This folder has programs to automatise tasks. There programs will run on the server when neccercary.

## tools
This folder contains scripts which are for one-time use, like CSV to JSON conversion scrips. There are save here, because they can come in handy during development.

## Tests
In this folder tests are stored to check the functionality of your server.
