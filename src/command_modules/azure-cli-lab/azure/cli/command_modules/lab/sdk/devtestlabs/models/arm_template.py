# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class ArmTemplate(Resource):
    """An Azure Resource Manager template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    :ivar display_name: The display name of the ARM template.
    :vartype display_name: str
    :ivar description: The description of the ARM template.
    :vartype description: str
    :ivar publisher: The publisher of the ARM template.
    :vartype publisher: str
    :ivar icon: The URI to the icon of the ARM template.
    :vartype icon: str
    :ivar contents: The contents of the ARM template.
    :vartype contents: object
    :ivar created_date: The creation date of the armTemplate.
    :vartype created_date: datetime
    :ivar parameters_value_files_info: File name and parameter values
     information from all azuredeploy.*.parameters.json for the ARM template.
    :vartype parameters_value_files_info: list of
     :class:`ParametersValueFileInfo
     <devtestlabs.models.ParametersValueFileInfo>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'readonly': True},
        'description': {'readonly': True},
        'publisher': {'readonly': True},
        'icon': {'readonly': True},
        'contents': {'readonly': True},
        'created_date': {'readonly': True},
        'parameters_value_files_info': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'icon': {'key': 'properties.icon', 'type': 'str'},
        'contents': {'key': 'properties.contents', 'type': 'object'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'parameters_value_files_info': {'key': 'properties.parametersValueFilesInfo', 'type': '[ParametersValueFileInfo]'},
    }

    def __init__(self, location=None, tags=None):
        super(ArmTemplate, self).__init__(location=location, tags=tags)
        self.display_name = None
        self.description = None
        self.publisher = None
        self.icon = None
        self.contents = None
        self.created_date = None
        self.parameters_value_files_info = None
