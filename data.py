import json

# Test comment
# Another test comment


class TestData:

    BASE_URL = "https://jsonplaceholder.typicode.com"
    POSTS = BASE_URL + "/posts"
    COMMENTS = BASE_URL + "/comments/1"
    ALBUMS = BASE_URL + "/albums"
    TODOS = BASE_URL + "/todos/17"
    USERS = BASE_URL + "/users/10"

    JSON_ALL_POSTS = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["userId", "id", "title", "body"],
            "minItems": 1,
            "maxItems": 100
        }
    }

    HEADER = {'content-type': 'application/json; charset=UTF-8'}

    HEADER_INVALID = {'content-type': 'application/xml'}
    PAYLOAD_INVALID = {"someField": 100}

    COMMENTS_PAYLOAD = {"postId": 100, "id": 501, "name": "Test", "email": "test@test.test", "body": "test body"}
    ALBUM_PAYLOAD = {"userId": 2, "id": 101, "title": "Test title"}
    TODOS_PAYLOAD = {"title": "quo laboriosam deleniti aut qui"}

    @staticmethod
    def get_json_payload(payload):
        return json.dumps([payload])

    @staticmethod
    def get_raw_json(source):
        raw_json = source.json()
        if isinstance(raw_json, list):
            return raw_json[0]
        else:
            return raw_json['0']
