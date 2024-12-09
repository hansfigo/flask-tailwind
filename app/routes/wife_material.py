from flask import (Blueprint, jsonify)

wife_blueprint = Blueprint('wife_material',__name__, url_prefix='/wife_material')

wife_material = [
    {
        "id": 1,
        "name": "Kaname Madoka",
        "anime": "Puella Magi Madoka Magica",
    },
    {
          "id": 2,
        "name": "Mami Tomoe",
        "anime": "Puella Magi Madoka Magica",
    }]

@wife_blueprint.route("/", methods=['GET'])
def get_wife_material():
    return jsonify(wife_material)

