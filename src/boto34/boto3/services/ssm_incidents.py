"""
Wrapper for boto3 SSMIncidents service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_incidents/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ssm_incidents.client import SSMIncidentsClient

from boto34.boto3.service_factory import ServiceFactory


class SSMIncidentsService(ServiceFactory[SSMIncidentsClient]):
    """
    SSMIncidents service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_incidents/)
    """
