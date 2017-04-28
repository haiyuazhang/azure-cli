# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class NotificationSettings(Model):
    """Notification settings for a schedule.

    :param status: If notifications are enabled for this schedule (i.e.
     Enabled, Disabled). Possible values include: 'Disabled', 'Enabled'
    :type status: str or :class:`NotificationStatus
     <devtestlabs.models.NotificationStatus>`
    :param time_in_minutes: Time in minutes before event at which notification
     will be sent.
    :type time_in_minutes: int
    :param webhook_url: The webhook URL to which the notification will be
     sent.
    :type webhook_url: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'time_in_minutes': {'key': 'timeInMinutes', 'type': 'int'},
        'webhook_url': {'key': 'webhookUrl', 'type': 'str'},
    }

    def __init__(self, status=None, time_in_minutes=None, webhook_url=None):
        self.status = status
        self.time_in_minutes = time_in_minutes
        self.webhook_url = webhook_url
