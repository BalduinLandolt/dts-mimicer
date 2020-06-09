class BaseEndpoint:

    @property
    def reply(self):
        return self._reply

    @property
    def endpoint_path(self):
        return self._endpoint_path

    @endpoint_path.setter
    def endpoint_path(self, path: str):
        s = str(path)
        if not s.startswith("/"):
            s = "/" + path
        if not s.endswith("/"):
            path += "/"
        self._endpoint_path = s

    _endpoint_path = "/dts/api/"

    _reply = {
        "@context": f"{_endpoint_path}contexts/EntryPoint.jsonld",
        "@id": _endpoint_path,
        "@type": "EntryPoint",
        "collections": f"{_endpoint_path}collections/",
        "documents": f"{_endpoint_path}documents/",
        "navigation": f"{_endpoint_path}navigation/"
    }
