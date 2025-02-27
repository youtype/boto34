"""
Wrapper for aiobotocore NetworkFirewall service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/)

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
    # Returns type annotated aiobotocore NetworkFirewall client
    async with session.network_firewall.create_client() as network_firewall_client:
        network_firewall_client: types_aiobotocore_network_firewall.client.NetworkFirewallClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_network_firewall.client import NetworkFirewallClient
except ImportError:
    NetworkFirewallClient = object  # type: ignore[misc,assignment]


class NetworkFirewallService(
    ServiceFactory[NetworkFirewallClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "network-firewall"
    _SERVICE_PROP = "network_firewall"
