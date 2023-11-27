from pydantic import BaseModel
from typing import Optional, List
from models.group import Group


class GroupSchema(BaseModel):
    """ Define how new group will be represented
    """
    name: str = "Group 1"

class GroupSearchSchema(BaseModel):
    id: Optional[int] = 1

class GroupViewSchema(BaseModel):
    """ Define how group will be returned
    """
    id: int = 1
    name: str = "Group 1"
    # created_at: 
    # updated_at:

def view_group(group: Group):
    """ Retorna uma representação do grupo seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": group.id,
        "name": group.name,
        "created_at": group.created_at,
        "updated_at": group.updated_at
    }

class GroupListViewSchema(BaseModel):
    groups: List[GroupViewSchema]

def view_group_list(groups):
    result = []
    for group in groups:
        result.append(view_group(group))
    return {"groups": result}

class GroupDeleteSchema(BaseModel):
    message: str
    id: int