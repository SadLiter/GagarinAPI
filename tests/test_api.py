from app import app


class TestGagarinAPI:
    def test_random_fact(self):
        client = app.test_client()
        response = client.get('/random_fact')
        assert response.status_code == 200

    def test_all_facts(self):
        client = app.test_client()
        response = client.get('/all_facts')
        assert response.status_code == 200
        assert len(response.json) == 2

    def test_random_fact_by_category(self):
        client = app.test_client()
        response = client.get('/random_fact_by_category?category=space')
        assert response.status_code == 200
        assert response.json['category'] == 'space'
