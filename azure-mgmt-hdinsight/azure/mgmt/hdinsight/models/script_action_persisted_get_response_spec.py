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

from msrest.serialization import Model


class ScriptActionPersistedGetResponseSpec(Model):
    """The persisted script action for cluster.

    :param name: The name of script action.
    :type name: str
    :param uri: The URI to the script.
    :type uri: str
    :param parameters: The parameters for the script provided.
    :type parameters: str
    :param roles: The list of roles where script will be executed.
    :type roles: list[str]
    :param application_name: The application name for the script action.
    :type application_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'application_name': {'key': 'applicationName', 'type': 'str'},
    }

    def __init__(self, name=None, uri=None, parameters=None, roles=None, application_name=None):
        super(ScriptActionPersistedGetResponseSpec, self).__init__()
        self.name = name
        self.uri = uri
        self.parameters = parameters
        self.roles = roles
        self.application_name = application_name
