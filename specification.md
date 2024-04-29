# specification

## business requirement

The company has a need for a standardised internal source of country information.

## platform

web framework
- ruby: rails 
- python: Django, Flask, etc 

## solution format

JSON REST API

## api

### methods

#### list all countries

- country data object
    * country name
    * alpha 2 code
    * alpha 3 code
    * currencies

- filtering
    * currency

#### get [single] country

matching on criterion
- alpha 2 code
- alpha 3 code

#### delete countries

soft delete

### sample data

country data 
- small sample (3-4 countries)
- of your choice

##  testing

unit tests required => TDD

## exclusions

- authentication
- authorization

