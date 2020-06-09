from flask import jsonify


class Collections:

    def __init__(self, path):
        self.__path = path

    @property
    def collection_path(self):
        return self.__path

    @property
    def collection_reply(self):
        return ["todo!"]
