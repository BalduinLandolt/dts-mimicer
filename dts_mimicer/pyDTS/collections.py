class Collections:

    def __init__(self, path, prefix=""):
        self.__path = path
        self.host_prefix = prefix

    @property
    def collection_path(self):
        return self.__path

    @property
    def collection_reply(self):  # TODO: make dynamic! (will need classes `Collection` and `Resource`)
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
            "mapping": [
                {
                    "@id": "sample_01",
                    "title": "Sample 01",
                    "description": "First sample Collection",
                    "@type": "Collection",
                    "totalItems": 1,
                    "dts:totalParents": 1,
                    "dts:totalChildren": 1
                },
                {
                    "@id": "sample_02",
                    "title": "Sample 02",
                    "description": "Second sample Collection",
                    "@type": "Collection",
                    "totalItems": 1,
                    "dts:totalParents": 1,
                    "dts:totalChildren": 1
                }
            ]
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
