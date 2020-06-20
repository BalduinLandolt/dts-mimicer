

class EndpointConstants:
    _host_prefix = "localhost"
    _endpoint_path = "/dts/api/"
    _collections_path = _endpoint_path + "collections/"
    _navigation_path = _endpoint_path + "navigation/"
    _documents_path = _endpoint_path + "documents/"

    @staticmethod
    def get_host_prefix():
        return EndpointConstants._host_prefix

    @staticmethod
    def set_host_prefix(prefix):
        EndpointConstants._host_prefix = prefix

    @staticmethod
    def get_endpoint_path():
        return EndpointConstants._endpoint_path

    @staticmethod
    def set_endpoint_path(path):
        EndpointConstants._endpoint_path = path

    @staticmethod
    def get_collections_path():
        return EndpointConstants._collections_path

    @staticmethod
    def set_collections_path(path):
        EndpointConstants._collections_path = path

    @staticmethod
    def get_navigation_path():
        return EndpointConstants._navigation_path

    @staticmethod
    def set_navigation_path(path):
        EndpointConstants._navigation_path = path

    @staticmethod
    def get_documents_path():
        return EndpointConstants._documents_path

    @staticmethod
    def set_documents_path(path):
        EndpointConstants._documents_path = path


class CollectionsConstants:
    TYPE_COLLECTION = "Collection"

    TYPE_RESOURCE = "Resource"

    CONTEXT = {
        "@vocab": "https://www.w3.org/ns/hydra/core#",
        "dc": "http://purl.org/dc/terms/",
        "dts": "https://w3id.org/dts/api#"
    }

    NAV_CHILDREN = "children"

    NAV_PARENTS = "parents"