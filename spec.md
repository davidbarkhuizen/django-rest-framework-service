-# specification

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

#### list all countries => get all countries

- country data object
    * country name
    * alpha 2 code
    * alpha 3 code
    * currencies

- filtering
    * currency

#### delete countries => delete countries

soft delete

#### get [single] country => get country

matching on criterion
- alpha 2 code
- alpha 3 code

### sample data

country data 
- small sample (3-4 countries)
- of your choice

##  testing

unit tests required => TDD

## exclusions

- authentication
- authorization

