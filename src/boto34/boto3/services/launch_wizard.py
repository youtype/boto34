"""
Wrapper for boto3 LaunchWizard service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_launch_wizard/)

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
    # Returns type annotated boto3 LaunchWizard client
    launch_wizard_client = session.launch_wizard.client()
    launch_wizard_client: types_boto3_launch_wizard.client.LaunchWizardClient
    ```
"""

from __future__ import annotations

from types_boto3_launch_wizard.client import LaunchWizardClient

from boto34.boto3.service_factory import ServiceFactory


class LaunchWizardService(ServiceFactory[LaunchWizardClient]):
    SERVICE_NAME = "launch-wizard"
    _SERVICE_PROP = "launch_wizard"
