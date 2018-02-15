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

from .linked_service import LinkedService


class SapHanaLinkedService(LinkedService):
    """SAP HANA Linked Service.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Linked Service.
    :type annotations: list[object]
    :param type: Constant filled by server.
    :type type: str
    :param server: Host name of the SAP HANA server. Type: string (or
     Expression with resultType string).
    :type server: object
    :param authentication_type: The authentication type to be used to connect
     to the SAP HANA server. Possible values include: 'Basic', 'Windows'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.SapHanaAuthenticationType
    :param user_name: Username to access the SAP HANA server. Type: string (or
     Expression with resultType string).
    :type user_name: object
    :param password: Password to access the SAP HANA server.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'server': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'server': {'key': 'typeProperties.server', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'user_name': {'key': 'typeProperties.userName', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, server, additional_properties=None, connect_via=None, description=None, parameters=None, annotations=None, authentication_type=None, user_name=None, password=None, encrypted_credential=None):
        super(SapHanaLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations)
        self.server = server
        self.authentication_type = authentication_type
        self.user_name = user_name
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'SapHana'
