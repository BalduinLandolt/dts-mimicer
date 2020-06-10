# TODO: add docstring
# TODO: add header with author and license to all files


class Collection:
    # TODO: make contents dynamic

    def __init__(self, contents):
        self.__contents = contents

    @property
    def mapping(self):
        return self.__contents


class Resource:
    # TODO: implement
    pass


class Collections:
    """Collection Endpoint Class.

    This class represents the conceptual Collections Endpoint of DTS.
    It organizes its own children, which can be of type `Collection` or `Resource`.

    Usually, `Collections` should be organized by an instance of `BaseEndpoint`

    See https://distributed-text-services.github.io/specifications/Collections-Endpoint.html
    """

    def __init__(self, path, prefix=""):
        self.__path = path
        self.host_prefix = prefix
        self.__children = []
        self.__generate_children()

    @property
    def collection_path(self):
        return self.__path

    @property
    def collection_response(self):  # TODO: make dynamic! (will need classes `Collection` and `Resource`)
        return {
            "@context": {
                "@vocab": "https://www.w3.org/ns/hydra/core#",
                "dc": "http://purl.org/dc/terms/",
                "dts": "https://w3id.org/dts/api#"
            },
            "@id": "sample_collection",
            "totalItems": 2,
            "dts:totalParents": 0,
            "dts:totalChildren": 2,
            "@type": "Collection",
            "title": "A sample collection made up for this mimicker",
            "description": "Contains two sample children",
            "mapping": self.__get_children_mappings()
        }

    @property
    def host_prefix(self):
        return self.__host_prefix

    @host_prefix.setter
    def host_prefix(self, prefix):
        self.__host_prefix = prefix

    @property
    def absolute_path(self):
        p = self.host_prefix + self.collection_path
        # p = p.replace("//", "/")
        return p

    def __get_children_mappings(self):
        return [c.mapping for c in self.__children]

    def __generate_children(self):
        content = {"@id": "sample_01",
                   "title": "Sample 01",
                   "description": "First sample Collection",
                   "@type": "Collection",
                   "totalItems": 1,
                   "dts:totalParents": 1,
                   "dts:totalChildren": 1}
        child = Collection(content)
        self.__children.append(child)
        content = {"@id": "sample_02",
                   "title": "Sample 02",
                   "description": "Second sample Collection",
                   "@type": "Collection",
                   "totalItems": 1,
                   "dts:totalParents": 1,
                   "dts:totalChildren": 1}
        child = Collection(content)
        self.__children.append(child)
