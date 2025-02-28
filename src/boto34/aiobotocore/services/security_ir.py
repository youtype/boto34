"""
Wrapper for aiobotocore SecurityIncidentResponse service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_security_ir/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_security_ir.client import SecurityIncidentResponseClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SecurityIncidentResponseService(ServiceFactory[SecurityIncidentResponseClient]):
    """
    SecurityIncidentResponse service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_security_ir/)
    """
