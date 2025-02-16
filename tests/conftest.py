import pytest
from config import db
from models import Fact


@pytest.fixture
def test_facts():
    db.facts.delete_many({})
    test_facts = [
        {"title": "First Orbital Flight",
         "content": "Yuri Gagarin became the first person to complete an orbital flight around the Earth.",
         "category": "space"},
        {"title": "Place of Birth",
         "content": "Yuri Gagarin was born on March 9, 1934, in the village of Klushino, Russia.",
         "category": "biography"},
        {"title": "Age at Flight", "content": "Yuri Gagarin was 27 years old when he became the first person in space.",
         "category": "space"},
        {"title": "Spacecraft", "content": "Gagarin's flight was carried out on the spacecraft 'Vostok 1'.",
         "category": "space"},
        {"title": "Flight Duration", "content": "Gagarin's first flight lasted 108 minutes.",
         "category": "space"},
        {"title": "Hero Title",
         "content": "After the flight into space, Gagarin was awarded the title Hero of the Soviet Union.",
         "category": "biography"},
        {"title": "Meeting with American Astronauts",
         "content": "Gagarin was the first Soviet cosmonaut to meet with American astronauts after their flights.",
         "category": "biography"},
        {"title": "Flight Training",
         "content": "Yuri Gagarin underwent rigorous training, including study at military aviation schools.",
         "category": "biography"},
        {"title": "Role in Space Program",
         "content": "Gagarin played a key role in popularizing the Soviet space program.",
         "category": "biography"},
        {"title": "Death", "content": "Yuri Gagarin died in a plane crash on March 27, 1967.",
         "category": "biography"}
    ]

    for fact in test_facts:
        fact_obj = Fact(fact['title'], fact['content'], fact['category'])
        fact_obj.save(db)