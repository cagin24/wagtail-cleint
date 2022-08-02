from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectResponse200ContentProject")


@attr.s(auto_attribs=True)
class GetProjectResponse200ContentProject:
    """
    Attributes:
        name (Union[Unset, str]):  Example: stream-wasp.
        nodes (Union[Unset, List[Any]]):
    """

    name: Union[Unset, str] = UNSET
    nodes: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        nodes: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        nodes = cast(List[Any], d.pop("nodes", UNSET))

        get_project_response_200_content_project = cls(
            name=name,
            nodes=nodes,
        )

        get_project_response_200_content_project.additional_properties = d
        return get_project_response_200_content_project

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
