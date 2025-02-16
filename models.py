from bson import ObjectId


class Fact:
    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category

    def save(self, db):
        fact_data = {
            "title": self.title,
            "content": self.content,
            "category": self.category
        }
        db.facts.insert_one(fact_data)

    @staticmethod
    def get_random(db):
        return db.facts.aggregate([{"$sample": {"size": 1}}]).next()

    @staticmethod
    def get_all(db):
        return list(db.facts.find())

    @staticmethod
    def get_random_by_category(db, category):
        return db.facts.aggregate([
            {"$match": {"category": category}},
            {"$sample": {"size": 1}}
        ]).next()

    @staticmethod
    def serialize(facts):
        for fact in facts:
            fact['_id'] = str(fact['_id'])
        return facts
