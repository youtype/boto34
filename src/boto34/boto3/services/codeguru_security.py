"""
Wrapper for boto3 CodeGuruSecurity service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguru_security/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codeguru_security.client import CodeGuruSecurityClient

from boto34.boto3.service_factory import ServiceFactory


class CodeGuruSecurityService(ServiceFactory[CodeGuruSecurityClient]):
    """
    CodeGuruSecurity service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguru_security/)
    """
