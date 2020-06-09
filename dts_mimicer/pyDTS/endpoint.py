from pyDTS.collections import Collections


class BaseEndpoint:

    def __init__(self, path="/dts/api/"):
        self.__endpoint_path = path
        self.__collections = Collections(self.endpoint_path + "collections/")
        self.__reply = {
            "@context": f"{self.__endpoint_path}contexts/EntryPoint.jsonld",
            "@id": self.__endpoint_path,
            "@type": "EntryPoint",
            "collections": self.__collections.collection_path,
            "documents": f"{self.__endpoint_path}documents/",
            "navigation": f"{self.__endpoint_path}navigation/"
        }

    @property
    def entrypoint_reply(self):
        return self.__reply

    @property
    def endpoint_path(self):
        return self.__endpoint_path

    @property
    def collections_path(self):
        return self.__collections.collection_path

    @property
    def collections_reply(self):
        return self.__collections.collection_reply
