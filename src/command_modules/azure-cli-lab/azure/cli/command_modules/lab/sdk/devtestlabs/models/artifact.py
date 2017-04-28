# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class Artifact(Resource):
    """An artifact.

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
    :ivar title: The artifact's title.
    :vartype title: str
    :ivar description: The artifact's description.
    :vartype description: str
    :ivar publisher: The artifact's publisher.
    :vartype publisher: str
    :ivar file_path: The file path to the artifact.
    :vartype file_path: str
    :ivar icon: The URI to the artifact icon.
    :vartype icon: str
    :ivar target_os_type: The artifact's target OS.
    :vartype target_os_type: str
    :ivar parameters: The artifact's parameters.
    :vartype parameters: object
    :ivar created_date: The artifact's creation date.
    :vartype created_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'title': {'readonly': True},
        'description': {'readonly': True},
        'publisher': {'readonly': True},
        'file_path': {'readonly': True},
        'icon': {'readonly': True},
        'target_os_type': {'readonly': True},
        'parameters': {'readonly': True},
        'created_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'file_path': {'key': 'properties.filePath', 'type': 'str'},
        'icon': {'key': 'properties.icon', 'type': 'str'},
        'target_os_type': {'key': 'properties.targetOsType', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
    }

    def __init__(self, location=None, tags=None):
        super(Artifact, self).__init__(location=location, tags=tags)
        self.title = None
        self.description = None
        self.publisher = None
        self.file_path = None
        self.icon = None
        self.target_os_type = None
        self.parameters = None
        self.created_date = None
