from .base_model import BaseModel

class EndPoint:
    def __init__(self, endpoint, http_method, description, endpoint_keywords, **kwargs):
        self.endpoint = endpoint
        self.http_method = http_method
        self.description = description
        self.endpoint_keywords = endpoint_keywords

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {
            'endpoint': self.endpoint,
            'http_method': self.http_method,
            'description': self.description,
            'endpoint_keywords': self.endpoint_keywords,
        }

class Api(BaseModel):
    collection_name = 'apis'

    def __init__(self, name=None, description=None, base_url=None, api_keywords=None, endpoints=None, popularity=None, service_level=None, latency=None, reliability=None, https=None, authentication=None, cors=None, docs=None, category=None, type=None, **kwargs):
        self.name = name
        self.description = description
        self.base_url = base_url
        self.api_keywords = api_keywords or []
        self.popularity = popularity
        self.service_level = service_level
        self.latency = latency
        self.reliability = reliability
        self.https = https
        self.authentication = authentication
        self.cors = cors
        self.docs = docs
        self.category = category
        self.type = type or 'REST'

        self.endpoints = []
        if endpoints is not None:
            for endpoint in endpoints:
                if isinstance(endpoint, EndPoint):
                    self.endpoints.append(endpoint)
                else:
                    self.endpoints.append(EndPoint(**endpoint))

        # Initialize with parent class
        super().__init__(**kwargs)

    def to_dict(self):
        doc = super().to_dict()
        doc['endpoints'] = [endpoint.to_dict() for endpoint in self.endpoints]
        return doc
