from model.note import Note
from model.tag import Tag
from typing import List, Union
from beanie import PydanticObjectId

note_collection = Note
tag_collection = Tag


# CRUD for tag collection
async def add_tag(tag_data: Tag) -> Tag:
    tag = await tag_collection.insert_one(tag_data)
    return tag


async def get_tag(tag_id: PydanticObjectId) -> Tag:
    tag = await tag_collection.get(tag_id)
    return tag


async def get_all_tags() -> List[Tag]:
    tags = await tag_collection.all().to_list()
    return tags


async def delete_tag(tag_id: PydanticObjectId) -> bool:
    tag = await tag_collection.get(tag_id)
    if tag:
        await tag.delete()
        return True
    return False


async def update_tag(tag_id: PydanticObjectId, data: dict) -> Union[bool, Tag]:
    des_body = {key: value for key, value in data.items() if value is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    tag = await tag_collection.get(tag_id)
    if tag:
        await tag.update(update_query)
        return tag
    return False


async def get_all_notes() -> List[Note]:
    notes = await note_collection.all().to_list()
    return notes


async def get_note(
    note_id: PydanticObjectId,
) -> Note:
    note = await note_collection.get(note_id)
    return note


async def add_note(
    note_data: Note,
) -> Note:
    note = await note_collection.insert_one(note_data)
    return note


async def update_note(note_id: PydanticObjectId, data: dict) -> Union[bool, Note]:
    des_body = {key: value for key, value in data.items() if value is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    note = await note_collection.get(note_id)
    if note:
        await note.update(update_query)
        return note
    return False


async def delete_note(
    note_id: PydanticObjectId,
) -> bool:
    note = await note_collection.get(note_id)
    if note:
        await note.delete()
        return True
    return False
