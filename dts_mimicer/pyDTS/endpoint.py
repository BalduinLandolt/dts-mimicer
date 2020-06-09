from pyDTS.collections import Collections


class BaseEndpoint:

    def __init__(self, path="/dts/api/", host_prefix=""):
        self.__endpoint_path = path
        self.__collections = Collections(self.endpoint_path + "collections/")
        self.__host_prefix = host_prefix

    @property
    def entrypoint_response(self):
        return {
            "@context": f"{self.__endpoint_path}contexts/EntryPoint.jsonld",
            "@id": self.absolute_path,
            "@type": "EntryPoint",
            "collections": self.__collections.absolute_path,
            "documents": f"{self.__endpoint_path}documents/",   # TODO: implement
            "navigation": f"{self.__endpoint_path}navigation/"  # TODO: implement
        }

    @property
    def endpoint_path(self):
        return self.__endpoint_path

    @property
    def collections_path(self):
        return self.__collections.collection_path

    @property
    def absolute_path(self):
        return self.host_prefix + self.endpoint_path

    @property
    def host_prefix(self):
        return self.__host_prefix

    @host_prefix.setter
    def host_prefix(self, prefix):
        self.__host_prefix = prefix
        self.__collections.host_prefix = prefix

    @property
    def collections_response(self):
        return self.__collections.collection_response
