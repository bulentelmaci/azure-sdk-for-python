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


class ComputeProfile(Model):
    """Describes the compute profile.

    :param roles: The list of roles in the cluster.
    :type roles: list[~azure.mgmt.hdinsight.models.Role]
    """

    _attribute_map = {
        'roles': {'key': 'roles', 'type': '[Role]'},
    }

    def __init__(self, roles=None):
        super(ComputeProfile, self).__init__()
        self.roles = roles
