"""
Wrapper for boto3 CloudHSMV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudhsmv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudhsmv2.client import CloudHSMV2Client

from boto34.boto3.service_factory import ServiceFactory


class CloudHSMV2Service(ServiceFactory[CloudHSMV2Client]):
    """
    CloudHSMV2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudhsmv2/)
    """
