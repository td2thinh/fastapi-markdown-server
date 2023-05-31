from fastapi import APIRouter, HTTPException, Body
from beanie import PydanticObjectId
from database.database import *
from model.note import *

router = APIRouter()


@router.get("/", response_description="List all notes", response_model=Response)
async def retrieve_notes():
    notes = await get_all_notes()
    return {
        "message": {
            "status": "success",
            "code": 200,
        },
        "data": notes,
    }


@router.get(
    "/{note_id}", response_description="Get a single note", response_model=Response
)
async def get_note_by_id(note_id: PydanticObjectId):
    note = await get_note(note_id)
    if note:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
            "data": note,
        }
    raise HTTPException(404, "Note not found")


@router.post("/", response_description="Add new note", response_model=Response)
async def add_note_data(note: Note = Body(...)):
    new_note = await add_note(note)
    if new_note:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
            "data": new_note,
        }
    raise HTTPException(500, "Something went wrong")


@router.put("/{note_id}", response_description="Update a note", response_model=Response)
async def update_note_by_id(note_id: PydanticObjectId, note: Note = Body(...)):
    updated_note = await update_note(note_id, note)
    if updated_note:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
            "data": updated_note,
        }
    raise HTTPException(404, "Note not found")


@router.delete(
    "/{note_id}", response_description="Delete a note", response_model=Response
)
async def delete_note_by_id(note_id: PydanticObjectId):
    deleted_note = await delete_note(note_id)
    if deleted_note:
        return {
            "message": {
                "status": "success",
                "code": 200,
            },
        }
    raise HTTPException(404, "Note not found")
