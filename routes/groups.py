from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint

from datetime import datetime
from logger import logger

from sqlalchemy.exc import IntegrityError

from schemas import GroupSchema, GroupViewSchema, ErrorSchema, GroupSearchSchema, GroupListViewSchema, GroupDeleteSchema
from schemas import view_group_list, view_group
from models import Session, Group

# Define documentation tags
group_tag = Tag(name="Groups", description="Add, visualize and remove groups")
groups_api = APIBlueprint('/groups', __name__, url_prefix='', abp_tags=[group_tag])

# # ==============================|| Groups Endpoints ||============================== #


@groups_api.post('/groups', tags=[group_tag],
           responses={"200": GroupViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_group(form: GroupSchema):
    """Add a new Group to the database

    Return representation of products and comments
    """
    group = Group(name=form.name)
    logger.debug(f"Add group named: '{group.name}'")
    try:
        session = Session()
        session.add(group)
        session.commit()
        logger.debug(f"Add group named: '{group.name}'")
        return view_group(group), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Group of same name already saved :/"
        logger.warning(
            f"Error adding group named: '{group.name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Not possible to save item :/"
        logger.warning(
            f"Error adding group named: '{group.name}', {error_msg}")
        return {"mesage": error_msg}, 400


@groups_api.get('/groups', tags=[group_tag],
          responses={"200": GroupViewSchema, "404": ErrorSchema})
def get_group(query: GroupSearchSchema):
    """Faz a busca por um Group a partir do id do grupo

    Retorna uma representação do Grupo.
    """
    group_id = query.id
    logger.debug(f"Colect data from group #{group_id}")
    session = Session()
    group = session.query(Group).filter(Group.id == group_id).first()
    if not group:
        error_msg = "Group not found in the database :/"
        logger.warning(f"Error finding group '{group_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Group found: '{group.name}'")
        return view_group(group), 200


@groups_api.get('/group_all', tags=[group_tag],
          responses={"200": GroupListViewSchema, "404": ErrorSchema})
def get_produtos():
    """List all groups

    Retorns a list of groups.
    """
    logger.debug(f"Fetching group list")
    session = Session()
    groups = session.query(Group).all()
    if not groups:
        error_msg = "Groups not found in the database :/"
        logger.warning(f"Error fetching groups {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retorning group list")
        return view_group_list(groups), 200


@groups_api.delete('/groups', tags=[group_tag],
             responses={"200": GroupDeleteSchema, "404": ErrorSchema})
def del_produto(query: GroupSearchSchema):
    """Deletes a group with id.

    Returns a confirmation message.
    """
    group_id = query.id

    logger.debug(f"Deleting group #{group_id}")
    session = Session()

    if group_id:
        count = session.query(Group).filter(Group.id == group_id).delete()

    session.commit()
    if count:
        logger.debug(f"Deleting group #{group_id}")
        return {"message": "Group removed!", "id": group_id}
    else:
        error_msg = "Groups not found in the database :/"
        logger.warning(f"Error deleting group #'{group_id}', {error_msg}")
        return {"message": error_msg}, 400