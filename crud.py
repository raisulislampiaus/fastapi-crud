# crud.py

from sqlalchemy.orm import Session
from models import Item
from database import SessionLocal

def create_item(item_data: dict):
    db = SessionLocal()
    db_item = Item(**item_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

def get_all_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

def get_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    return item

def update_item(item_id: int, item_data: dict):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    for field, value in item_data.items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    db.close()
    return {"message": "Item deleted successfully"}
