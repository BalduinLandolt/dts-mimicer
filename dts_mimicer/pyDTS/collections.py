from abc import ABC
from pyDTS.constants import CollectionsConstants, EndpointConstants


# QUESTION: Does Resource have members? might be relevant when navigation "parent"

# LATER: missing attributes: dublincore, extensions

# TODO: add docstring
# TODO: add header with author and license to all files


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
            par = self.parent[0]
            return par.get_member(CollectionsConstants.NAV_PARENTS)
        else:
            return []

    @property
    def children_members(self):
        if self.children:
            return [c.get_member(CollectionsConstants.NAV_CHILDREN) for c in self.children]
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
        return self.id == id  # QUESTION: should I also allow fuzzy match?


class Collection(AbstractCollectionItem):
    def __init__(self, id, parent, children, title, description):
        super(Collection, self).__init__(id=id,
                                         parent=parent,
                                         children=children,
                                         type=CollectionsConstants.TYPE_COLLECTION,
                                         title=title,
                                         description=description)

    # TODO: check, which further methods can be made abstract

    def get_response(self, page, nav):
        return {
            "@context": CollectionsConstants.CONTEXT,
            "@id": self.id,
            "@type": self.type,
            "title": self.title,
            "description": self.description,
            "totalItems": len(self.children) if nav == CollectionsConstants.NAV_CHILDREN else len(self.parent),
            "dts:totalParents": len(self.parent),
            "dts:totalChildren": len(self.children),
            "member": self.get_members(nav)
        }

    def get_member(self, nav):
        return {
            "@id": self.id,
            "@type": self.type,
            "title": self.title,
            "description": self.description,
            "totalItems": len(self.children) if nav == CollectionsConstants.NAV_CHILDREN else len(self.parent),
            "dts:totalParents": len(self.parent),
            "dts:totalChildren": len(self.children)
        }

    def get_members(self, nav):
        if nav == CollectionsConstants.NAV_CHILDREN:
            return self.children_members
        else:
            return self.parent_member

    def add_child(self, child):
        self.children.append(child)


class Resource(AbstractCollectionItem):
    def __init__(self, id, parent, title, description):
        super(Resource, self).__init__(id=id,
                                       parent=parent,
                                       children=[],
                                       type=CollectionsConstants.TYPE_RESOURCE,
                                       title=title,
                                       description=description)

    def get_response(self, page, nav):
        return {
            "@context": CollectionsConstants.CONTEXT,
            "@id": self.id,
            "@type": self.type,
            "title": self.title,
            "description": self.description,
            "totalItems": len(self.children) if nav == CollectionsConstants.NAV_CHILDREN else len(self.parent),
            "dts:totalParents": len(self.parent),
            "dts:totalChildren": len(self.children),
            "dts:passage": self.passage,
            "dts:references": self.references,
            "dts:download": self.download,
            "dts:citeDepth": self.cite_depth,  # TODO: add
            "dts:citeStructure": self.cite_structure  # TODO: add
            # "member": self.get_members(nav)
        }

    # def get_member(self, nav):  # TODO: make resource specific
    #     return {
    #         "@id": self.id,
    #         "title": self.title,
    #         "description": self.description,
    #         "@type": self.type,
    #         "totalItems": len(self.children) if nav == Constants.NAV_CHILDREN else len(self.parent),
    #         "dts:totalParents": len(self.parent),
    #         "dts:totalChildren": len(self.children)
    #     }

    @property
    def passage(self):
        return EndpointConstants.get_documents_path() + "?id=" + self.id

    @property
    def references(self):
        return EndpointConstants.get_navigation_path() + "?id=" + self.id

    @property
    def download(self):
        return "todo!"  # TODO: add

    @property
    def cite_depth(self):
        return "todo!"  # TODO: add

    @property
    def cite_structure(self):
        return "todo!"  # TODO: add

    def get_members(self, nav):  # TODO: make resource specific
        if nav == CollectionsConstants.NAV_CHILDREN:
            return self.children_members
        else:
            return self.parent_member

    def get_member(self, nav):
        return {
            "@id": self.id,
            "@type": self.type,
            "title": self.title,
            "description": self.description,
            "totalItems": len(self.children) if nav == CollectionsConstants.NAV_CHILDREN else len(self.parent),
            "dts:totalParents": len(self.parent),
            "dts:totalChildren": len(self.children),
            "dts:passage": self.passage,  # TODO: correct?
            "dts:references": self.references,  # TODO: correct?
            "dts:download": self.download,  # TODO: add
            "dts:citeDepth": self.cite_depth,  # TODO: add
            "dts:citeStructure": self.cite_structure  # TODO: add
        }


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

    def __init__(self):
        self.__root = self.__generate_root()

    @property
    def collection_path(self):
        return EndpointConstants.get_collections_path()

    @property
    def host_prefix(self):
        return EndpointConstants.get_host_prefix()

    @host_prefix.setter
    def host_prefix(self, prefix):
        EndpointConstants.set_host_prefix(prefix)

    @property
    def absolute_path(self):
        p = self.host_prefix + self.collection_path
        return p

    def __get_children_mappings(self):
        return [c.get_members for c in self.__children]

    def __generate_children(self):
        col_1 = Collection(id="sample_01",
                           parent=[],
                           children=[],
                           title="Sample 01",
                           description="First sample Collection")
        col_2 = Collection(id="sample_02",
                           parent=[],
                           children=[],
                           title="Sample 02",
                           description="Second sample Collection")
        res_1 = Resource(id="sample_res_01",
                         parent=[col_1],
                         title="Sample Resource 1",
                         description="Sample Textual Resource")
        col_1.add_child(res_1)
        return [
            col_1,
            col_2
        ]

    def __generate_root(self):
        children = self.__generate_children()
        root = Collection(
            id="root_collection",
            parent=[],
            children=children,
            title="Root Collection",
            description="A Sample Root Collection")
        for c in children:
            c.parent = [root]
        return root

    def get_collection_response(self, id, page, nav):
        # TODO: actually handle page
        print(f"id: {id} - page: {page} - nav: {nav}")  # LATER: remove eventually
        if id:
            col = self.get_collection(id)
        else:
            col = self.__root
        return col.get_response(page, nav)
