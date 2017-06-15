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

from .workload_protectable_item import WorkloadProtectableItem


class IaaSVMProtectableItem(WorkloadProtectableItem):
    """IaaS VM workload-specific backup item.

    :param backup_management_type: Type of backup managemenent to backup an
     item.
    :type backup_management_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected'
    :type protection_state: str or :class:`ProtectionStatus
     <azure.mgmt.recoveryservicesbackup.models.ProtectionStatus>`
    :param protectable_item_type: Polymorphic Discriminator
    :type protectable_item_type: str
    :param virtual_machine_id: Fully qualified ARM ID of the virtual machine.
    :type virtual_machine_id: str
    """

    _validation = {
        'protectable_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'protectable_item_type': {'key': 'protectableItemType', 'type': 'str'},
        'virtual_machine_id': {'key': 'virtualMachineId', 'type': 'str'},
    }

    _subtype_map = {
        'protectable_item_type': {'Microsoft.ClassicCompute/virtualMachines': 'AzureIaaSClassicComputeVMProtectableItem', 'Microsoft.Compute/virtualMachines': 'AzureIaaSComputeVMProtectableItem'}
    }

    def __init__(self, backup_management_type=None, friendly_name=None, protection_state=None, virtual_machine_id=None):
        super(IaaSVMProtectableItem, self).__init__(backup_management_type=backup_management_type, friendly_name=friendly_name, protection_state=protection_state)
        self.virtual_machine_id = virtual_machine_id
        self.protectable_item_type = 'IaaSVMProtectableItem'