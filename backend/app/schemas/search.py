from pydantic import BaseModel


class DistrictSuggestion(BaseModel):
    district_name: str
    state_name: str


class StateSuggestion(BaseModel):
    state_name: str