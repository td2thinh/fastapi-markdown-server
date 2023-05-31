from fastapi import APIRouter, HTTPException, Body
from beanie import PydanticObjectId
from database.database import *
from model.tag import *

router = APIRouter()


@router.get("/", response_description="List all tags", response_model=Response)
async def retrieve_all_tags():
    tags = await get_all_tags()
    return {
        "message": {
            "status": "success",
            "code": 200,
        },
        "data": tags,
    }


@router.get(
    "/{tag_id}", response_description="Get a single tag", response_model=Response
)
async def get_one_tag(tag_id: PydanticObjectId):
    tag = await get_tag(tag_id)
    if tag:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
            "data": tag,
        }
    raise HTTPException(404, "Tag not found")


@router.post("/", response_description="Add new tag", response_model=Response)
async def add_one_tag(tag: Tag = Body(...)):
    new_tag = await add_tag(tag)
    if new_tag:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
            "data": new_tag,
        }
    raise HTTPException(500, "Something went wrong")


@router.delete(
    "/{tag_id}", response_description="Delete a tag", response_model=Response
)
async def delete_one_tag(tag_id: PydanticObjectId):
    deleted_tag = await delete_tag(tag_id)
    if deleted_tag:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
        }
    raise HTTPException(404, "Tag not found")


@router.put("/{tag_id}", response_description="Update a tag", response_model=Response)
async def update_one_tag(tag_id: PydanticObjectId, tag: Tag = Body(...)):
    updated_tag = await update_tag(tag_id, tag.dict())
    if updated_tag:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
            "data": updated_tag,
        }
    raise HTTPException(404, "Tag not found")
