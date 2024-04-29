from flask import Flask

from apis import CountryAPI, CountriesAPI

server = Flask(__name__)

server.add_url_rule('/country/', view_func=CountryAPI.as_view('country'))
server.add_url_rule('/countries/', view_func=CountriesAPI.as_view('countries'))

if __name__ == "__main__":
    server.run()