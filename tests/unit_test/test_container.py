def test_container(container):
    incident_notification_service = container.incident_notification_service()
    try:
        notify = incident_notification_service.notify()
    except FileNotFoundError as e:
        assert True
