# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class ComputeVmProperties(Model):
    """Properties of a virtual machine returned by the Microsoft.Compute API.

    :param statuses: Gets the statuses of the virtual machine.
    :type statuses: list of :class:`ComputeVmInstanceViewStatus
     <devtestlabs.models.ComputeVmInstanceViewStatus>`
    :param os_type: Gets the OS type of the virtual machine.
    :type os_type: str
    :param vm_size: Gets the size of the virtual machine.
    :type vm_size: str
    :param network_interface_id: Gets the network interface ID of the virtual
     machine.
    :type network_interface_id: str
    :param os_disk_id: Gets OS disk blob uri for the virtual machine.
    :type os_disk_id: str
    :param data_disk_ids: Gets data disks blob uri for the virtual machine.
    :type data_disk_ids: list of str
    :param data_disks: Gets all data disks attached to the virtual machine.
    :type data_disks: list of :class:`ComputeDataDisk
     <devtestlabs.models.ComputeDataDisk>`
    """

    _attribute_map = {
        'statuses': {'key': 'statuses', 'type': '[ComputeVmInstanceViewStatus]'},
        'os_type': {'key': 'osType', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'network_interface_id': {'key': 'networkInterfaceId', 'type': 'str'},
        'os_disk_id': {'key': 'osDiskId', 'type': 'str'},
        'data_disk_ids': {'key': 'dataDiskIds', 'type': '[str]'},
        'data_disks': {'key': 'dataDisks', 'type': '[ComputeDataDisk]'},
    }

    def __init__(self, statuses=None, os_type=None, vm_size=None, network_interface_id=None, os_disk_id=None, data_disk_ids=None, data_disks=None):
        self.statuses = statuses
        self.os_type = os_type
        self.vm_size = vm_size
        self.network_interface_id = network_interface_id
        self.os_disk_id = os_disk_id
        self.data_disk_ids = data_disk_ids
        self.data_disks = data_disks
