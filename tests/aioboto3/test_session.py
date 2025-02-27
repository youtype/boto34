import pytest
from botocore.exceptions import UnknownServiceError

from boto34.aioboto3 import Session


def get_session() -> Session:
    return Session(
        aws_access_key_id="ABCDEFGABCDEFGABCDEF",
        aws_secret_access_key="YTYHRSshtrsTRHSrsTHRSTrthSRThsrTHsr",
        region_name="us-east-1",
    )


@pytest.mark.asyncio
async def test_session_client(moto_server_url: str) -> None:
    session = get_session()
    async with session.s3.client(endpoint_url=moto_server_url) as s3_client:
        await s3_client.create_bucket(Bucket="test-bucket")
        await s3_client.put_object(Bucket="test-bucket", Key="test-key", Body="test-body")

        response = await s3_client.get_object(Bucket="test-bucket", Key="test-key")
        body = await response["Body"].read()
        assert body == b"test-body"


@pytest.mark.asyncio
async def test_session_resource(moto_server_url: str) -> None:
    session = get_session()
    async with session.s3.resource(endpoint_url=moto_server_url) as s3_resource:
        await s3_resource.create_bucket(Bucket="test-bucket")
        bucket = await s3_resource.Bucket("test-bucket")
        await bucket.put_object(Key="test-key", Body="test-body")
        obj = await bucket.Object("test-key")
        response = await obj.get()
        body = await response["Body"].read()
        assert body == b"test-body"


@pytest.mark.asyncio
async def test_session_proxy_methods() -> None:
    session = get_session()
    assert len(await session.s3.get_available_regions())


@pytest.mark.asyncio
async def test_session_invalid_service(moto_server_url: str) -> None:
    session = get_session()
    s3_session = session.s3
    s3_session.SERVICE_NAME = "invalid"
    with pytest.raises(UnknownServiceError):
        async with s3_session.client(endpoint_url=moto_server_url) as s3_client:
            assert s3_client
