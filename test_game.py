from main import app
from fastapi.testclient import TestClient
from fastapi import Form
import pytest

client = TestClient(app)

# run with $ make

#################################################### LogIn ####################################################
#################################################### LogIn ####################################################
#################################################### LogIn ####################################################

#! USER 1
def test_register_Amber():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "amber@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Amber"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Amber",
                            "userOut_email": "amber@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Amber():
    response = client.post("/login/", data={"username":"amber@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token

#! USER 2
def test_register_Benny():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "benny@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Benny"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Benny",
                            "userOut_email": "benny@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Benny():
    response = client.post("/login/", data={"username":"benny@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token

#! USER 3
def test_register_Candy():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "candy@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Candy"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Candy",
                            "userOut_email": "candy@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Candy():
    response = client.post("/login/", data={"username":"candy@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token


#! USER 4
def test_register_Demian():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "demian@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Demian"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Demian",
                            "userOut_email": "demian@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Demian():
    response = client.post("/login/", data={"username":"demian@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token


#! USER 5
def test_register_Esteban():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "esteban@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Esteban"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Esteban",
                            "userOut_email": "esteban@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Esteban():
    response = client.post("/login/", data={"username":"esteban@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token


#! USER 6
def test_register_Fiora():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "fiora@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Fiora"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Fiora",
                            "userOut_email": "fiora@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Fiora():
    response = client.post("/login/", data={"username":"fiora@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token


#! USER 7
def test_register_Gian():
    response = client.post(
                    "/users/",
                    json = { 
                    "userIn_email": "gian@gmail.com", 
                    "userIn_password": "12345678", 
                    "userIn_username": "Gian"
                    }
                    )
    assert response.status_code == 201
    assert response.json() == {"userOut_username":"Gian",
                            "userOut_email": "gian@gmail.com",
                            "userOut_operation_result": " Succesfully created!"}

def getToken_Gian():
    response = client.post("/login/", data={"username":"gian@gmail.com", "password":"12345678" })
    token = "Bearer " + response.json()["access_token"]
    return token


#################################################### Logged in Lobby Tests ####################################################
#################################################### Logged in Lobby Tests ####################################################
#################################################### Logged in Lobby Tests ####################################################


            ########################################    Create New Lobby   ########################################


def test_create_new_lobby():
    token = getToken_Amber()
    response = client.post(
                    "/lobby/",
                    headers = { "Authorization": token },
                    json = { 
                    "lobbyIn_name": "Party Hard", 
                    "lobbyIn_max_players": 10, 
                    "lobbyIn_min_players": 5
                    }
                    )
    assert response.status_code == 201
    assert response.json()["lobbyOut_result"] == " Your new lobby has been succesfully created!"


            ########################################    Join Lobby   ########################################
            

#! Player 2
def test_join_lobby_Benny():
    token = getToken_Benny()
    uri= "/lobby/1/" # For default: Party Hard
    response = client.post(
        uri,
        headers= { "Authorization": token },
        json= {}
    )
    assert response.status_code == 202
    assert response.json()["joinLobby_result"] == " Welcome to Party Hard"

#! Player 3
def test_join_lobby_Candy():
    token = getToken_Candy()
    uri= "/lobby/1/" # For default: Party Hard
    response = client.post(
        uri,
        headers= { "Authorization": token },
        json= {}
    )
    assert response.status_code == 202
    assert response.json()["joinLobby_result"] == " Welcome to Party Hard"

#! Player 4
def test_join_lobby_Demian():
    token = getToken_Demian()
    uri= "/lobby/1/" # For default: Party Hard
    response = client.post(
        uri,
        headers= { "Authorization": token },
        json= {}
    )
    assert response.status_code == 202
    assert response.json()["joinLobby_result"] == " Welcome to Party Hard"

#! Player 5
def test_join_lobby_Esteban():
    token = getToken_Esteban()
    uri= "/lobby/1/" # For default: Party Hard
    response = client.post(
        uri,
        headers= { "Authorization": token },
        json= {}
    )
    assert response.status_code == 202
    assert response.json()["joinLobby_result"] == " Welcome to Party Hard"

#! Player 6
# def test_join_lobby_Fiora():
#     token = getToken_Fiora()
#     lobby_id= 1 # For default: Party Hard
#     uri= "/lobby/"+str(lobby_id)
#     response = client.post(
#         uri,
#         headers= { "Authorization": token },
#         json= {}
#     )
#     assert response.status_code == 202
#     assert response.json()["joinLobby_result"] == " Welcome to Party Hard"


#################################################### Logged in Game Tests ####################################################
#################################################### Logged in Game Tests ####################################################
#################################################### Logged in Game Tests ####################################################


def test_start_new_game_from_lobby():
    token= getToken_Amber()
    #lobby_id= create_new_lobby()
    lobby_id= 1 # For default: Party Hard
    uri= "/lobby/"+str(lobby_id)+"/start_game"
    response= client.delete(
        uri,
        headers= { "Authorization": token },
        json= {
            "lobby_id": lobby_id
        }
    )
    assert response.status_code == 200
    assert response.json()["gameOut_result"] == " Your game has been started"