def test_notify_incident(client):
    response = client.post(
        "/incident-notification",
        json={},
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["data"] is not None
