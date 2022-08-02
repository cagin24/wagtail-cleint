from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.add_project_multipart_data import AddProjectMultipartData
from ...models.add_project_response_200 import AddProjectResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: AddProjectMultipartData,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(name, Unset):
        headers["name"] = name

    if not isinstance(tenant, Unset):
        headers["tenant"] = tenant

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AddProjectResponse200]:
    if response.status_code == 200:
        response_200 = AddProjectResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AddProjectResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: AddProjectMultipartData,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
) -> Response[AddProjectResponse200]:
    """Add Project

     Add Project

    Args:
        name (Union[Unset, str]):  Example: wasp.
        tenant (Union[Unset, str]):  Example: Default.
        multipart_data (AddProjectMultipartData):

    Returns:
        Response[AddProjectResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        name=name,
        tenant=tenant,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: AddProjectMultipartData,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
) -> Optional[AddProjectResponse200]:
    """Add Project

     Add Project

    Args:
        name (Union[Unset, str]):  Example: wasp.
        tenant (Union[Unset, str]):  Example: Default.
        multipart_data (AddProjectMultipartData):

    Returns:
        Response[AddProjectResponse200]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        name=name,
        tenant=tenant,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: AddProjectMultipartData,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
) -> Response[AddProjectResponse200]:
    """Add Project

     Add Project

    Args:
        name (Union[Unset, str]):  Example: wasp.
        tenant (Union[Unset, str]):  Example: Default.
        multipart_data (AddProjectMultipartData):

    Returns:
        Response[AddProjectResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        name=name,
        tenant=tenant,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: AddProjectMultipartData,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
) -> Optional[AddProjectResponse200]:
    """Add Project

     Add Project

    Args:
        name (Union[Unset, str]):  Example: wasp.
        tenant (Union[Unset, str]):  Example: Default.
        multipart_data (AddProjectMultipartData):

    Returns:
        Response[AddProjectResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            name=name,
            tenant=tenant,
        )
    ).parsed
