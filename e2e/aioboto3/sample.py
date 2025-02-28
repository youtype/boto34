"""
Copyright 2025 Vlad Emelianov
"""

from boto34.aioboto3.session import Session


async def main() -> None:
    session = Session()
    reveal_type(session)
    async with session.s3.client() as client:
        reveal_type(client)
        waiter = client.get_waiter("object_exists")
        reveal_type(waiter)
        paginator = client.get_paginator("list_parts")
        reveal_type(paginator)
    async with session.s3.resource() as resource:
        reveal_type(resource)


