from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_response_200_content import GetProjectResponse200Content
from ..models.get_project_response_200_diagram import GetProjectResponse200Diagram
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectResponse200")


@attr.s(auto_attribs=True)
class GetProjectResponse200:
    """
    Attributes:
        content (Union[Unset, GetProjectResponse200Content]):
        diagram (Union[Unset, GetProjectResponse200Diagram]):
        id (Union[Unset, float]):  Example: 1.
        name (Union[Unset, str]):  Example: stream-wasp.
        tenant (Union[Unset, str]):  Example: Default.
    """

    content: Union[Unset, GetProjectResponse200Content] = UNSET
    diagram: Union[Unset, GetProjectResponse200Diagram] = UNSET
    id: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    tenant: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        diagram: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.diagram, Unset):
            diagram = self.diagram.to_dict()

        id = self.id
        name = self.name
        tenant = self.tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if diagram is not UNSET:
            field_dict["diagram"] = diagram
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
        _content = d.pop("content", UNSET)
        content: Union[Unset, GetProjectResponse200Content]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = GetProjectResponse200Content.from_dict(_content)

        _diagram = d.pop("diagram", UNSET)
        diagram: Union[Unset, GetProjectResponse200Diagram]
        if isinstance(_diagram, Unset):
            diagram = UNSET
        else:
            diagram = GetProjectResponse200Diagram.from_dict(_diagram)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        tenant = d.pop("tenant", UNSET)

        get_project_response_200 = cls(
            content=content,
            diagram=diagram,
            id=id,
            name=name,
            tenant=tenant,
        )

        get_project_response_200.additional_properties = d
        return get_project_response_200

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
