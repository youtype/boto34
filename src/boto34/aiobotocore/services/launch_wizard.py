"""
Wrapper for aiobotocore LaunchWizard service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore LaunchWizard client
    async with session.launch_wizard.create_client() as launch_wizard_client:
        launch_wizard_client: types_aiobotocore_launch_wizard.client.LaunchWizardClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_launch_wizard.client import LaunchWizardClient
except ImportError:
    LaunchWizardClient = object  # type: ignore[misc,assignment]


class LaunchWizardService(
    ServiceFactory[LaunchWizardClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "launch-wizard"
    _SERVICE_PROP = "launch_wizard"
