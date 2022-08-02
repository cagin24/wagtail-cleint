from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.maestro_multipart_data import MaestroMultipartData
from ...models.maestro_response_200 import MaestroResponse200
from ...models.maestro_response_422 import MaestroResponse422
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: MaestroMultipartData,
    project_name: Union[Unset, str] = UNSET,
    tenant_name: Union[Unset, str] = UNSET,
    services: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/maestro".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(project_name, Unset):
        headers["project-name"] = project_name

    if not isinstance(tenant_name, Unset):
        headers["tenant-name"] = tenant_name

    if not isinstance(services, Unset):
        headers["services"] = services

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[MaestroResponse200, MaestroResponse422]]:
    if response.status_code == 200:
        response_200 = MaestroResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = MaestroResponse422.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[MaestroResponse200, MaestroResponse422]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: MaestroMultipartData,
    project_name: Union[Unset, str] = UNSET,
    tenant_name: Union[Unset, str] = UNSET,
    services: Union[Unset, str] = UNSET,
) -> Response[Union[MaestroResponse200, MaestroResponse422]]:
    """Maestro

     Maestro

    Args:
        project_name (Union[Unset, str]):  Example: http-diarize-lang-sr.
        tenant_name (Union[Unset, str]):  Example: Default.
        services (Union[Unset, str]):  Example: sr, language.
        multipart_data (MaestroMultipartData):

    Returns:
        Response[Union[MaestroResponse200, MaestroResponse422]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        project_name=project_name,
        tenant_name=tenant_name,
        services=services,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: MaestroMultipartData,
    project_name: Union[Unset, str] = UNSET,
    tenant_name: Union[Unset, str] = UNSET,
    services: Union[Unset, str] = UNSET,
) -> Optional[Union[MaestroResponse200, MaestroResponse422]]:
    """Maestro

     Maestro

    Args:
        project_name (Union[Unset, str]):  Example: http-diarize-lang-sr.
        tenant_name (Union[Unset, str]):  Example: Default.
        services (Union[Unset, str]):  Example: sr, language.
        multipart_data (MaestroMultipartData):

    Returns:
        Response[Union[MaestroResponse200, MaestroResponse422]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        project_name=project_name,
        tenant_name=tenant_name,
        services=services,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: MaestroMultipartData,
    project_name: Union[Unset, str] = UNSET,
    tenant_name: Union[Unset, str] = UNSET,
    services: Union[Unset, str] = UNSET,
) -> Response[Union[MaestroResponse200, MaestroResponse422]]:
    """Maestro

     Maestro

    Args:
        project_name (Union[Unset, str]):  Example: http-diarize-lang-sr.
        tenant_name (Union[Unset, str]):  Example: Default.
        services (Union[Unset, str]):  Example: sr, language.
        multipart_data (MaestroMultipartData):

    Returns:
        Response[Union[MaestroResponse200, MaestroResponse422]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        project_name=project_name,
        tenant_name=tenant_name,
        services=services,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: MaestroMultipartData,
    project_name: Union[Unset, str] = UNSET,
    tenant_name: Union[Unset, str] = UNSET,
    services: Union[Unset, str] = UNSET,
) -> Optional[Union[MaestroResponse200, MaestroResponse422]]:
    """Maestro

     Maestro

    Args:
        project_name (Union[Unset, str]):  Example: http-diarize-lang-sr.
        tenant_name (Union[Unset, str]):  Example: Default.
        services (Union[Unset, str]):  Example: sr, language.
        multipart_data (MaestroMultipartData):

    Returns:
        Response[Union[MaestroResponse200, MaestroResponse422]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            project_name=project_name,
            tenant_name=tenant_name,
            services=services,
        )
    ).parsed
