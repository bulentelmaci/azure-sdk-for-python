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

from .resource import Resource


class SearchService(Resource):
    """Describes an Azure Search service and its current state.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource. This can be used with the Azure Resource
     Manager to link resources together.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: The geographic location of the resource. This must be one
     of the supported and registered Azure Geo Regions (for example, West US,
     East US, Southeast Asia, and so forth). This property is required when
     creating a new resource.
    :type location: str
    :param tags: Tags to help categorize the resource in the Azure portal.
    :type tags: dict[str, str]
    :param replica_count: The number of replicas in the Search service. If
     specified, it must be a value between 1 and 12 inclusive for standard SKUs
     or between 1 and 3 inclusive for basic SKU. Default value: 1 .
    :type replica_count: int
    :param partition_count: The number of partitions in the Search service; if
     specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only
     valid for standard SKUs. For 'standard3' services with hostingMode set to
     'highDensity', the allowed values are between 1 and 3. Default value: 1 .
    :type partition_count: int
    :param hosting_mode: Applicable only for the standard3 SKU. You can set
     this property to enable up to 3 high density partitions that allow up to
     1000 indexes, which is much higher than the maximum indexes allowed for
     any other SKU. For the standard3 SKU, the value is either 'default' or
     'highDensity'. For all other SKUs, this value must be 'default'. Possible
     values include: 'default', 'highDensity'. Default value: "default" .
    :type hosting_mode: str or ~azure.mgmt.search.models.HostingMode
    :ivar status: The status of the Search service. Possible values include:
     'running': The Search service is running and no provisioning operations
     are underway. 'provisioning': The Search service is being provisioned or
     scaled up or down. 'deleting': The Search service is being deleted.
     'degraded': The Search service is degraded. This can occur when the
     underlying search units are not healthy. The Search service is most likely
     operational, but performance might be slow and some requests might be
     dropped. 'disabled': The Search service is disabled. In this state, the
     service will reject all API requests. 'error': The Search service is in an
     error state. If your service is in the degraded, disabled, or error
     states, it means the Azure Search team is actively investigating the
     underlying issue. Dedicated services in these states are still chargeable
     based on the number of search units provisioned. Possible values include:
     'running', 'provisioning', 'deleting', 'degraded', 'disabled', 'error'
    :vartype status: str or ~azure.mgmt.search.models.SearchServiceStatus
    :ivar status_details: The details of the Search service status.
    :vartype status_details: str
    :ivar provisioning_state: The state of the last provisioning operation
     performed on the Search service. Provisioning is an intermediate state
     that occurs while service capacity is being established. After capacity is
     set up, provisioningState changes to either 'succeeded' or 'failed'.
     Client applications can poll provisioning status (the recommended polling
     interval is from 30 seconds to one minute) by using the Get Search Service
     operation to see when an operation is completed. If you are using the free
     service, this value tends to come back as 'succeeded' directly in the call
     to Create Search service. This is because the free service uses capacity
     that is already set up. Possible values include: 'succeeded',
     'provisioning', 'failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.search.models.ProvisioningState
    :param sku: The SKU of the Search Service, which determines price tier and
     capacity limits. This property is required when creating a new Search
     Service.
    :type sku: ~azure.mgmt.search.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'replica_count': {'maximum': 12, 'minimum': 1},
        'partition_count': {'maximum': 12, 'minimum': 1},
        'status': {'readonly': True},
        'status_details': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'replica_count': {'key': 'properties.replicaCount', 'type': 'int'},
        'partition_count': {'key': 'properties.partitionCount', 'type': 'int'},
        'hosting_mode': {'key': 'properties.hostingMode', 'type': 'HostingMode'},
        'status': {'key': 'properties.status', 'type': 'SearchServiceStatus'},
        'status_details': {'key': 'properties.statusDetails', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, location=None, tags=None, replica_count=1, partition_count=1, hosting_mode="default", sku=None):
        super(SearchService, self).__init__(location=location, tags=tags)
        self.replica_count = replica_count
        self.partition_count = partition_count
        self.hosting_mode = hosting_mode
        self.status = None
        self.status_details = None
        self.provisioning_state = None
        self.sku = sku
