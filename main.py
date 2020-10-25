from fastapi import FastAPI, HTTPException, status
from fastapi import WebSocket, WebSocketDisconnect
from models import *
from db_entities_relations import *
from db_functions import *

app = FastAPI()


#users's endpoints
@app.post("/users/", 
    status_code=status.HTTP_201_CREATED, 
    response_model=UserIn, response_model_exclude_unset=True
)
async def create_user(new_user: UserIn) -> int:
    if check_email_exists(new_user.email):
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, detail="email already exists"
        )
    if check_username_exists(new_user.username):
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, detail="username already exists"
        )
    insert_user(new_user.email, new_user.username, new_user.password, new_user.photo)
    return UserOut(
        username=new_user.username, email=new_user.email,
        operation_result="Succesfully created!")


#lobbies's endpoints


#games's endpoints


#boards's endpoints


#histories's endpoints
