from flask import jsonify


class Collections:

    def __init__(self, path, prefix=""):
        self.__path = path
        self.host_prefix = prefix

    @property
    def collection_path(self):
        return self.__path

    @property
    def collection_reply(self):
        return ["todo!"]

    @property
    def host_prefix(self):
        return self.__host_prefix

    @host_prefix.setter
    def host_prefix(self, prefix):
        self.__host_prefix = prefix

    @property
    def absolut_path(self):
        p = self.host_prefix + self.collection_path
        #p = p.replace("//", "/")
        return p
