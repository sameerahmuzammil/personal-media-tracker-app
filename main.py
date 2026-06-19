from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Query, Form, Request
from sqlmodel import Session, SQLModel, create_engine, select, Field

class Media(SQLModel, table=True):
    media_id: int = Field(default=None, primary_key=True)
    author: str = Field(default="N/A")
    media_name: str = Field(nullable=False)
    genre: str = Field(nullable=False)
    media_category: str = Field(index=True, nullable=False)
    status : str = Field(nullable=False)
    stars : int = Field(ge=1, le=5)

sqlite_file_name = "media.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

templates = Jinja2Templates(directory="templates")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#i have to make a session, and sessiondep
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

#on startup, a database is created (on_event is outdated, use lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

#add an item
@app.post("/media/")
def create_media(item: Media, session: SessionDep) -> Media:
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

#read an item
@app.get("/media/{media_id}")
def read_media_item(media_id: int, session: SessionDep) -> Media:
    item = session.get(Media, media_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found :(")
    return item

#read all the items
@app.get("/media/")
def read_all_media(session: SessionDep) -> list[Media]:
    all_media = session.exec(select(Media)).all()
    return all_media

#update an item
@app.patch("/media/{media_id}")
def update_media_item(media_id: int, media_update: Media, session: SessionDep) -> Media:
    item = session.get(Media, media_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found :(")
    update_data = media_update.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_data)
    session.commit()
    session.refresh(item)
    return item

#delete an item
@app.delete("/media/{media_id}")
def delete_media_item(media_id: int, session: SessionDep):
    item = session.get(Media, media_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found :(")
    session.delete(item)
    session.commit()
    return {"ok": True}

#delete all items
@app.delete("/media/")
def delete_all_media(session: SessionDep):
    all_media = session.exec(select(Media)).all()
    if not all_media:
        raise HTTPException(status_code=404, detail="Item not found :(")
    for item in all_media:
        session.delete(item)
    session.commit()
    return {"ok": True}

@app.get("/", response_class=HTMLResponse)
def show_media_list(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")