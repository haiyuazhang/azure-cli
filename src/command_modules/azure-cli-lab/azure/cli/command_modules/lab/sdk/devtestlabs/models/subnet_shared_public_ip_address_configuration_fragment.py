# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class SubnetSharedPublicIpAddressConfigurationFragment(Model):
    """Configuration for public IP address sharing.

    :param allowed_ports: Backend ports that virtual machines on this subnet
     are allowed to expose
    :type allowed_ports: list of :class:`PortFragment
     <devtestlabs.models.PortFragment>`
    """

    _attribute_map = {
        'allowed_ports': {'key': 'allowedPorts', 'type': '[PortFragment]'},
    }

    def __init__(self, allowed_ports=None):
        self.allowed_ports = allowed_ports
