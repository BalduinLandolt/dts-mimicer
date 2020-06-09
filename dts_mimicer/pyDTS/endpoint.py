from pyDTS.collections import Collections


class BaseEndpoint:

    def __init__(self, path="/dts/api/", host_prefix=""):
        self.__endpoint_path = path
        self.__collections = Collections(self.endpoint_path + "collections/")
        self.host_prefix = host_prefix

    @property
    def entrypoint_reply(self):
        return {
            "@context": f"{self.__endpoint_path}contexts/EntryPoint.jsonld",
            "@id": self.absolut_path,
            "@type": "EntryPoint",
            "collections": self.__collections.absolut_path,
            "documents": f"{self.__endpoint_path}documents/",
            "navigation": f"{self.__endpoint_path}navigation/"
        }

    @property
    def endpoint_path(self):
        return self.__endpoint_path

    @property
    def collections_path(self):
        return self.__collections.collection_path

    @property
    def absolut_path(self):
        p = self.host_prefix + self.endpoint_path
        #p = p.replace("//", "/")
        return p

    @property
    def host_prefix(self):
        return self.__absolut_path_prefix
    @host_prefix.setter
    def host_prefix(self, prefix):
        self.__absolut_path_prefix = prefix
        self.__collections.host_prefix = prefix

    @property
    def collections_reply(self):
        return "todo"
