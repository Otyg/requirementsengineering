from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class AlternativeStep:
    id: int
    step: str

    @staticmethod
    def from_dict(obj: Any) -> 'AlternativeStep':
        _id = int(obj.get("id"))
        _step = str(obj.get("step"))
        return AlternativeStep(_id, _step)

@dataclass
class ErrorStep:
    id: int
    step: str

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorStep':
        _id = int(obj.get("id"))
        _step = str(obj.get("step"))
        return ErrorStep(_id, _step)

@dataclass
class Relation:
    id: str
    relation_type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Relation':
        _id = str(obj.get("id"))
        _relation_type = str(obj.get("relation_type"))
        return Relation(_id, _relation_type)

@dataclass
class Root:
    id: str
    name: str
    actors: List[str]
    objective: str
    preconditions: str
    postconditions: str
    steps: List[Step]
    relations: List[Relation]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _actors = [str(y) for y in obj.get("actors")]
        _objective = str(obj.get("objective"))
        _preconditions = str(obj.get("preconditions"))
        _postconditions = str(obj.get("postconditions"))
        _steps = [Step.from_dict(y) for y in obj.get("steps")]
        _relations = [Relation.from_dict(y) for y in obj.get("relations")]
        return Root(_id, _name, _actors, _objective, _preconditions, _postconditions, _steps, _relations)

@dataclass
class Step:
    id: int
    actor: str
    step: str
    alternative_steps: List[AlternativeStep]
    error_steps: List[ErrorStep]

    @staticmethod
    def from_dict(obj: Any) -> 'Step':
        _id = int(obj.get("id"))
        _actor = str(obj.get("actor"))
        _step = str(obj.get("step"))
        _alternative_steps = [AlternativeStep.from_dict(y) for y in obj.get("alternative_steps")]
        _error_steps = [ErrorStep.from_dict(y) for y in obj.get("error_steps")]
        return Step(_id, _actor, _step, _alternative_steps, _error_steps)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
