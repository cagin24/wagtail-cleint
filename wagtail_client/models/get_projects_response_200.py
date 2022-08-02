from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_projects_response_200_projects_item import GetProjectsResponse200ProjectsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectsResponse200")


@attr.s(auto_attribs=True)
class GetProjectsResponse200:
    """
    Attributes:
        project_count (Union[Unset, float]):  Example: 1.
        projects (Union[Unset, List[GetProjectsResponse200ProjectsItem]]):  Example: [{'id': 1, 'name': 'stream-wasp',
            'tenant': 'Default'}].
    """

    project_count: Union[Unset, float] = UNSET
    projects: Union[Unset, List[GetProjectsResponse200ProjectsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_count = self.project_count
        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_count is not UNSET:
            field_dict["project-count"] = project_count
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_count = d.pop("project-count", UNSET)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = GetProjectsResponse200ProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        get_projects_response_200 = cls(
            project_count=project_count,
            projects=projects,
        )

        get_projects_response_200.additional_properties = d
        return get_projects_response_200

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
