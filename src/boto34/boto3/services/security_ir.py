"""
Wrapper for boto3 SecurityIncidentResponse service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_security_ir/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_security_ir.client import SecurityIncidentResponseClient

from boto34.boto3.service_factory import ServiceFactory


class SecurityIncidentResponseService(ServiceFactory[SecurityIncidentResponseClient]):
    """
    SecurityIncidentResponse service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_security_ir/)
    """
