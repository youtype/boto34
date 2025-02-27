"""
Wrapper for aioboto3 LaunchWizard service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_launch_wizard/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 LaunchWizard client
    launch_wizard_client = session.launch_wizard.client()
    launch_wizard_client: types_aiobotocore_launch_wizard.client.LaunchWizardClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_launch_wizard.client import LaunchWizardClient

from boto34.aioboto3.service_factory import ServiceFactory


class LaunchWizardService(ServiceFactory[LaunchWizardClient]):
    SERVICE_NAME = "launch-wizard"
    _SERVICE_PROP = "launch_wizard"
