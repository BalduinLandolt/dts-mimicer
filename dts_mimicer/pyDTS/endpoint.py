from pyDTS.collections import Collections, Constants


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
        self.__endpoint_path = path
        self.__collections = Collections(self.endpoint_path + "collections/")
        self.__host_prefix = host_prefix

    @property
    def entrypoint_response(self):
        """Entrypoint Response.

        Property organizing the response of the entry point.

        Returns:
            dict: JSON style (jsonifyable) key-value-pairs.
        """
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
        """Endpoint Path

        relative path to the API entry point.
        Typically something like "/dts/api/"

        Returns:
            str: path
        """
        return self.__endpoint_path

    @property
    def collections_path(self):
        """Collections path.

        Path to the Collections entry point.
        Typically "dts/api/collections/"

        Returns:
            str: path
        """
        return self.__collections.collection_path

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
        return self.__host_prefix

    @host_prefix.setter
    def host_prefix(self, prefix):
        self.__host_prefix = prefix
        self.__collections.host_prefix = prefix

    def get_collections_response(self, id=None, page=None, nav=Constants.NAV_CHILDREN):
        """Collections Response

        Property to forward the collections' response.

        Args:
            id (str): id from query, if applicable; `None` otherwise. Defaults to `None`.
            page (str): page from query, if applicable; `None` otherwise. Defaults to `None`.
            nav (str): navigation parameter from query; either "children" or "parents". Defaults to "children.

        Returns:
            dict: JSON style response.
        """
        return self.__collections.get_collection_response(id, page, nav)
