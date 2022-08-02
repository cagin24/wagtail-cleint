from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectsResponse200ProjectsItem")


@attr.s(auto_attribs=True)
class GetProjectsResponse200ProjectsItem:
    """
    Attributes:
        id (Union[Unset, float]):  Example: 1.
        name (Union[Unset, str]):  Example: stream-wasp.
        tenant (Union[Unset, str]):  Example: Default.
    """

    id: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    tenant: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        tenant = self.tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tenant is not UNSET:
            field_dict["tenant"] = tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        tenant = d.pop("tenant", UNSET)

        get_projects_response_200_projects_item = cls(
            id=id,
            name=name,
            tenant=tenant,
        )

        get_projects_response_200_projects_item.additional_properties = d
        return get_projects_response_200_projects_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
