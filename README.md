# Django Audit Logger

`django-audit-logger` is a reusable Django app that automatically audits model changes (create, update, delete) across all models in your Django project. It integrates with Kafka for log streaming and allows flexible configuration auditing for important models. The app captures useful metadata such as the user who made the changes, request IP, URL, and more.

## Features

- **Automatic Auditing**: Automatically register all Django models for audit logging after migrations.
- **Kafka Integration**: Uses `confluent_kafka` to send audit logs to Kafka topics.
- **Configuration Auditing**: Manually register important models for configuration auditing.
- **User Context Middleware**: Captures information about the user, request IP, and user agent via middleware.
- **Customizable**: You can extend or override middleware, and control the Kafka producer behavior.

## Installation

1. **INSTALL the package using pip**:

   ```bash
   pip install django-audit-kafkalogger
   
2. **Add it to your Django INSTALLED_APPS**:

    In your `settings.py`, configure the apps:
    ```python
   INSTALLED_APPS = [
       # Other installed apps
       'audit_logger',
   ]

3. **Add the MIDDLEWARE**:

    In your `settings.py`, configure the middlewares:
    ```python
   MIDDLEWARE = [
       # Other middlewares
       'audit_logger.middlewares.AuditUserMiddleware',
   ]

4. **Add KAFKA CONFIGURATION**:
    
    In your `settings.py`, configure the Kafka broker and topics:
    ```python
    KAFKA_BROKER_URL = 'localhost:9092'  # Replace with your Kafka broker URL
    KAFKA_TOPIC_LOGS = 'audit_logs'      # Topic for log auditing
    KAFKA_TOPIC_ERRORS = 'audit_errors'  # Topic for error logging
    KAFKA_TOPIC_CONFIG = 'audit_config'  # Topic for configuration auditing


