"""
Wrapper for aiobotocore SSMIncidents service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_incidents/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm_incidents.client import SSMIncidentsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSMIncidentsService(ServiceFactory[SSMIncidentsClient]):
    """
    SSMIncidents service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_incidents/)
    """
