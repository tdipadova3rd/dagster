from typing import List, Optional

from pydantic import BaseModel

from ...utils import kubernetes


class Migrate(BaseModel):
    enabled: bool
    customMigrateCommand: Optional[List[str]]
    extraContainers: List[kubernetes.Container]
