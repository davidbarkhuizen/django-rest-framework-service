from flask import jsonify, request, views

def content_type_error(request):

    content_type = request.headers.get("Content-Type")
    
    if content_type == "application/json":
        return None

    return jsonify({
        "error": "Unknown Content Type: {}".format(content_type)
    }), 415

class CountryAPI(views.MethodView):
    
    def get(self):
        # return jsonify({"error": "ERROR"}), 400
        return jsonify({"a": "b"}), 200

    def post(self):

        if (error := content_type_error(request)) is not None:
            return error

        return jsonify({}), 200


class CountriesAPI(views.MethodView):
    def get(self):

        # optionally filter on currency
        all_countries = []
        return jsonify(all_countries), 200

    def delete(self):
        # delete specific country
        return jsonify({}), 200
