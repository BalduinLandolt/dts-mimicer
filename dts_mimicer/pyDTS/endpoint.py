from pyDTS.collections import Collections
from pyDTS.constants import EndpointConstants, CollectionsConstants


class BaseEndpoint:
    """API Entry Point

    this Class represents the entry point of the DTS API.

    See: https://distributed-text-services.github.io/specifications/Entry.html
    """

    def __init__(self, path="/dts/api/", host_prefix="localhost"):
        """`BaseEndpoint` Constructor.

        Creates an instance of `BaseEndpoint`.

        Args:
            path (str, optional): The relative path on the server to the API entry point. Defaults to "/dts/api/".
            host_prefix (str, optional): The host address. Defaults to "localhost".
        """
        EndpointConstants.set_host_prefix(host_prefix)
        EndpointConstants.set_endpoint_path(path)
        EndpointConstants.set_collections_path(path + "collections/")
        EndpointConstants.set_navigation_path(path + "navigation/")
        EndpointConstants.set_documents_path(path + "documents/")
        self.__collections = Collections()

    @property
    def entrypoint_response(self):
        """Entrypoint Response.

        Property organizing the get_response of the entry point.

        Returns:
            dict: JSON style (jsonifyable) key-value-pairs.
        """
        return {
            "@context": f"{self.endpoint_path}contexts/EntryPoint.jsonld",
            "@id": self.absolute_path,
            "@type": "EntryPoint",
            "collections": self.__collections.absolute_path,
            "documents": f"{EndpointConstants.get_endpoint_path()}documents/",   # LATER: implement
            "navigation": f"{EndpointConstants.get_endpoint_path()}navigation/"  # LATER: implement
        }

    @property
    def endpoint_path(self):  # TODO: remove?
        """Endpoint Path

        relative path to the API entry point.
        Typically something like "/dts/api/"

        Returns:
            str: path
        """
        return EndpointConstants.get_endpoint_path()

    @property
    def collections_path(self):  # TODO: remove?
        """Collections path.

        Path to the Collections entry point.
        Typically "dts/api/collections/"

        Returns:
            str: path
        """
        return EndpointConstants.get_collections_path()

    @property
    def absolute_path(self):
        """Absolute Path

        The absolute URI to the entry point
        E.g.: "http://localhost:17980/dts/api/"

        Returns:
            str: URI
        """
        return self.host_prefix + self.endpoint_path

    @property
    def host_prefix(self):
        """Host Prefix Property
        
        Organizes the host prefix. (getter and setter)
        E.g.: "localhost"

        Returns:
            str: prefix
        """
        return EndpointConstants.get_host_prefix()

    @host_prefix.setter
    def host_prefix(self, prefix):
        EndpointConstants.set_host_prefix(prefix)

    def get_collections_response(self, id=None, page=None, nav=CollectionsConstants.NAV_CHILDREN):
        """Collections Response

        Property to forward the collections' get_response.

        Args:
            id (str): id from query, if applicable; `None` otherwise. Defaults to `None`.
            page (str): page from query, if applicable; `None` otherwise. Defaults to `None`.
            nav (str): navigation parameter from query; either "children" or "parents". Defaults to "children.

        Returns:
            dict: JSON style get_response.
        """
        return self.__collections.get_collection_response(id, page, nav)
