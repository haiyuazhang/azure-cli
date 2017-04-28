# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .labs_operations import LabsOperations
from .global_schedules_operations import GlobalSchedulesOperations
from .artifact_sources_operations import ArtifactSourcesOperations
from .arm_templates_operations import ArmTemplatesOperations
from .artifacts_operations import ArtifactsOperations
from .costs_operations import CostsOperations
from .custom_images_operations import CustomImagesOperations
from .formulas_operations import FormulasOperations
from .gallery_images_operations import GalleryImagesOperations
from .notification_channels_operations import NotificationChannelsOperations
from .policy_sets_operations import PolicySetsOperations
from .policies_operations import PoliciesOperations
from .schedules_operations import SchedulesOperations
from .service_runners_operations import ServiceRunnersOperations
from .users_operations import UsersOperations
from .disks_operations import DisksOperations
from .environments_operations import EnvironmentsOperations
from .secrets_operations import SecretsOperations
from .virtual_machines_operations import VirtualMachinesOperations
from .virtual_machine_schedules_operations import VirtualMachineSchedulesOperations
from .virtual_networks_operations import VirtualNetworksOperations

__all__ = [
    'LabsOperations',
    'GlobalSchedulesOperations',
    'ArtifactSourcesOperations',
    'ArmTemplatesOperations',
    'ArtifactsOperations',
    'CostsOperations',
    'CustomImagesOperations',
    'FormulasOperations',
    'GalleryImagesOperations',
    'NotificationChannelsOperations',
    'PolicySetsOperations',
    'PoliciesOperations',
    'SchedulesOperations',
    'ServiceRunnersOperations',
    'UsersOperations',
    'DisksOperations',
    'EnvironmentsOperations',
    'SecretsOperations',
    'VirtualMachinesOperations',
    'VirtualMachineSchedulesOperations',
    'VirtualNetworksOperations',
]
