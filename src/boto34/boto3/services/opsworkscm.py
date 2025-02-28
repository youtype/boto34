"""
Wrapper for boto3 OpsWorksCM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opsworkscm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_opsworkscm.client import OpsWorksCMClient

from boto34.boto3.service_factory import ServiceFactory


class OpsWorksCMService(ServiceFactory[OpsWorksCMClient]):
    """
    OpsWorksCM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opsworkscm/)
    """
