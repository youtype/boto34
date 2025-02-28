"""
Wrapper for boto3 XRay service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_xray/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_xray.client import XRayClient

from boto34.boto3.service_factory import ServiceFactory


class XRayService(ServiceFactory[XRayClient]):
    """
    XRay service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_xray/)
    """
