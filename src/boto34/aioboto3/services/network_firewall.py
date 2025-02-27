"""
Wrapper for aioboto3 NetworkFirewall service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_network_firewall/)

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
    # Returns type annotated aioboto3 NetworkFirewall client
    network_firewall_client = session.network_firewall.client()
    network_firewall_client: types_aiobotocore_network_firewall.client.NetworkFirewallClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_network_firewall.client import NetworkFirewallClient

from boto34.aioboto3.service_factory import ServiceFactory


class NetworkFirewallService(ServiceFactory[NetworkFirewallClient]):
    SERVICE_NAME = "network-firewall"
    _SERVICE_PROP = "network_firewall"
