USER_SCHEMA = """
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "title": "User",
      "description": "A Confluent Kafka Python User",
      "type": "object",
      "properties": {
        "username": {
          "description": "Wischmcj",
          "type": "string"
        },
        "data": {
          "description": "User's favorite color: Poop brown",
          "type": "string"
        }
      },
      "required": [ "username", "data" ]
    }
    """

USER_TOPIC = 'TestTopic'