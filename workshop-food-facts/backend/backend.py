from flask import Flask, request, jsonify
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from resolvers import schema
app = Flask(__name__)

@app.route("/playground")
def hello_world():
    return PLAYGROUND_HTML, 200

@app.route("/api", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema=schema,
        data=data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)
