from flask import Flask
from routes import random_fact, all_facts, random_fact_by_category

app = Flask(__name__)

app.add_url_rule('/random_fact', 'random_fact', random_fact, methods=['GET'])
app.add_url_rule('/all_facts', 'all_facts', all_facts, methods=['GET'])
app.add_url_rule('/random_fact_by_category', 'random_fact_by_category', random_fact_by_category, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
