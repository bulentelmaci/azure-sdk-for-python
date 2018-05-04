# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.images_operations import ImagesOperations
from . import models


class VisualSearchAPIConfiguration(Configuration):
    """Configuration for VisualSearchAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://api.cognitive.microsoft.com/bing/v7.0'

        super(VisualSearchAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-search-visualsearch/{}'.format(VERSION))

        self.credentials = credentials


class VisualSearchAPI(SDKClient):
    """Visual Search API lets you discover insights about an image such as visually similar images, shopping sources, and related searches. The API can also perform text recognition, identify entities (people, places, things), return other topical content for the user to explore, and more. For more information, see [Visual Search Overview](https://docs.microsoft.com/azure/cognitive-services/bing-visual-search/overview).

    :ivar config: Configuration for client.
    :vartype config: VisualSearchAPIConfiguration

    :ivar images: Images operations
    :vartype images: azure.cognitiveservices.search.visualsearch.operations.ImagesOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = VisualSearchAPIConfiguration(credentials, base_url)
        super(VisualSearchAPI, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.images = ImagesOperations(
            self._client, self.config, self._serialize, self._deserialize)