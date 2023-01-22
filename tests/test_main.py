def test_app(test_app):
    response = test_app.get("")
    assert response.status_code == 200
