"""
Wrapper for boto3 LicenseManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 LicenseManager client
    license_manager_client = session.license_manager.client()
    license_manager_client: types_boto3_license_manager.client.LicenseManagerClient
    ```
"""

from __future__ import annotations

from types_boto3_license_manager.client import LicenseManagerClient

from boto34.boto3.service_factory import ServiceFactory


class LicenseManagerService(ServiceFactory[LicenseManagerClient]):
    SERVICE_NAME = "license-manager"
    _SERVICE_PROP = "license_manager"
