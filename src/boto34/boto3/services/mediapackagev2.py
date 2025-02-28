"""
Wrapper for boto3 Mediapackagev2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackagev2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediapackagev2.client import Mediapackagev2Client

from boto34.boto3.service_factory import ServiceFactory


class Mediapackagev2Service(ServiceFactory[Mediapackagev2Client]):
    """
    Mediapackagev2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackagev2/)
    """
