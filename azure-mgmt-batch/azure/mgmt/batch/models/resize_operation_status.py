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


class ResizeOperationStatus(Model):
    """Details about the current or last completed resize operation.

    Describes either the current operation (if the pool AllocationState is
    Resizing) or the previously completed operation (if the AllocationState is
    Steady).

    :param target_dedicated_nodes: The desired number of dedicated compute
     nodes in the pool.
    :type target_dedicated_nodes: int
    :param target_low_priority_nodes: The desired number of low-priority
     compute nodes in the pool.
    :type target_low_priority_nodes: int
    :param resize_timeout: The timeout for allocation of compute nodes to the
     pool or removal of compute nodes from the pool. The default value is 15
     minutes. The minimum value is 5 minutes. If you specify a value less than
     5 minutes, the Batch service returns an error; if you are calling the REST
     API directly, the HTTP status code is 400 (Bad Request).
    :type resize_timeout: timedelta
    :param node_deallocation_option: Determines what to do with a node and its
     running task(s) if the pool size is decreasing. The default value is
     requeue. Possible values include: 'Requeue', 'Terminate',
     'TaskCompletion', 'RetainedData'
    :type node_deallocation_option: str or
     ~azure.mgmt.batch.models.ComputeNodeDeallocationOption
    :param start_time: The time when this resize operation was started.
    :type start_time: datetime
    :param errors: Details of any errors encountered while performing the last
     resize on the pool. This property is set only if an error occurred during
     the last pool resize, and only when the pool allocationState is Steady.
    :type errors: list[~azure.mgmt.batch.models.ResizeError]
    """

    _attribute_map = {
        'target_dedicated_nodes': {'key': 'targetDedicatedNodes', 'type': 'int'},
        'target_low_priority_nodes': {'key': 'targetLowPriorityNodes', 'type': 'int'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'node_deallocation_option': {'key': 'nodeDeallocationOption', 'type': 'ComputeNodeDeallocationOption'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'errors': {'key': 'errors', 'type': '[ResizeError]'},
    }

    def __init__(self, target_dedicated_nodes=None, target_low_priority_nodes=None, resize_timeout=None, node_deallocation_option=None, start_time=None, errors=None):
        super(ResizeOperationStatus, self).__init__()
        self.target_dedicated_nodes = target_dedicated_nodes
        self.target_low_priority_nodes = target_low_priority_nodes
        self.resize_timeout = resize_timeout
        self.node_deallocation_option = node_deallocation_option
        self.start_time = start_time
        self.errors = errors
