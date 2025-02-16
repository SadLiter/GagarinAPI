from flask import jsonify, request, Response
import json
from models import Fact
from config import db

def random_fact():
    fact = Fact.get_random(db)
    fact['_id'] = str(fact['_id'])
    return jsonify(fact)

def all_facts():
    facts = Fact.get_all(db)
    facts = Fact.serialize(facts)
    return Response(
        json.dumps(facts, ensure_ascii=False),
        mimetype='application/json'
    )

def random_fact_by_category():
    category = request.args.get('category')
    fact = Fact.get_random_by_category(db, category)
    fact['_id'] = str(fact['_id'])
    return jsonify(fact)
