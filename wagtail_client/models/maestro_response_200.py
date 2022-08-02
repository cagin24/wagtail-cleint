from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaestroResponse200")


@attr.s(auto_attribs=True)
class MaestroResponse200:
    """
    Attributes:
        error_message (Union[Unset, str]):
        results (Union[Unset, Any]):
        status (Union[Unset, str]):  Example: ok.
    """

    error_message: Union[Unset, str] = UNSET
    results: Union[Unset, Any] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_message = self.error_message
        results = self.results
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["error-message"] = error_message
        if results is not UNSET:
            field_dict["results"] = results
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_message = d.pop("error-message", UNSET)

        results = d.pop("results", UNSET)

        status = d.pop("status", UNSET)

        maestro_response_200 = cls(
            error_message=error_message,
            results=results,
            status=status,
        )

        maestro_response_200.additional_properties = d
        return maestro_response_200

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
