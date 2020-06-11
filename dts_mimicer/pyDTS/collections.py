from abc import ABC, abstractmethod

# TODO: add docstring
# TODO: add header with author and license to all files


class Constants:
    TYPE_COLLECTION = "Collection"

    TYPE_RESOURCE = "Resource"

    CONTEXT = {
        "@vocab": "https://www.w3.org/ns/hydra/core#",
        "dc": "http://purl.org/dc/terms/",
        "dts": "https://w3id.org/dts/api#"
    }


class AbstractCollectionItem(ABC):
    def __init__(self, id, parent, children, type, title, description):
        self.id = id
        self.parent = parent
        self.children = children
        self.type = type
        self.title = title
        self.description = description
        Collections.register_collection(self)

    def __str__(self):
        return f"<{self.type}: {self.id} -- {self.title} -- {self.description}>"

    @property
    def parent_member(self):
        if self.parent:
            return self.parent.member
        else:
            return []

    @property
    def children_members(self):
        if self.children:
            return [c.member for c in self.children]
        else:
            return []

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    def match_id(self, id):
        return self.id == id


class Collection(AbstractCollectionItem):
    # TODO: check, which further methods can be made abstract

    @property
    def response(self):
        return {
            "@context": Constants.CONTEXT,
            "@id": self.id,
            "totalItems": len(self.children) + len(self.parent), # FIXME: should be either or, depending on nav parameter
            "dts:totalParents": len(self.parent),
            "dts:totalChildren": len(self.children),
            "@type": self.type,
            "title": self.title,
            "description": self.description,
            "member": self.members  # -> null!
        }

    @property
    def member(self):
        return {
            "@id": self.id,
            "title": self.title,
            "description": self.description,
            "@type": self.type,
            "totalItems": len(self.children) + len(self.parent), # FIXME: see above
            "dts:totalParents": len(self.parent),
            "dts:totalChildren": len(self.children)
        }

    @property
    def members(self): # FIXME: see above
        res = []
        res.extend(self.parent_member.copy())
        res.extend(self.children_members.copy())
        return res


class Resource(AbstractCollectionItem):
    # TODO: implement
    pass


class Collections:
    """Collection Endpoint Class.

    This class represents the conceptual Collections Endpoint of DTS.
    It organizes its own children, which can be of type `Collection` or `Resource`.

    Usually, `Collections` should be organized by an instance of `BaseEndpoint`

    See https://distributed-text-services.github.io/specifications/Collections-Endpoint.html
    """

    __registered_collections = []

    @staticmethod
    def register_collection(collection):
        Collections.__registered_collections.append(collection)

    @staticmethod
    def get_collection(id):
        for c in Collections.__registered_collections:
            if c.match_id(id):
                return c

    def __init__(self, path, prefix=""):
        self.__path = path
        self.host_prefix = prefix
        self.__root = self.__generate_root()

    @property
    def collection_path(self):
        return self.__path

    @property
    def collection_response(self):
        return self.__root.response

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
        return [c.members for c in self.__children]

    def __generate_children(self):
        col_1 = Collection(id="sample_01",
                           parent=[self],
                           children=[],
                           type=Constants.TYPE_COLLECTION,
                           title="Sample 01",
                           description="First sample Collection")
        col_2 = Collection(id="sample_02",
                           parent=[self],
                           children=[],
                           type=Constants.TYPE_COLLECTION,
                           title="Sample 02",
                           description="Second sample Collection")
        return [
            col_1,
            col_2
        ]

    def __generate_root(self):
        return Collection(
            id="root_collection",
            parent=[],
            children=self.__generate_children(),
            type=Constants.TYPE_COLLECTION,
            title="Root Collection",
            description="A Sample Root Collection"
        )
