"""
Wrapper for boto3 GroundStation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_groundstation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_groundstation.client import GroundStationClient

from boto34.boto3.service_factory import ServiceFactory


class GroundStationService(ServiceFactory[GroundStationClient]):
    """
    GroundStation service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_groundstation/)
    """
