import config
config.database = "test_data_base.sqlite"

from main import app
from fastapi.testclient import TestClient
from fastapi import Form
import test_1logIn as logIn
import test_2lobby as lobby
import db_functions as dbf
import db_entities_relations as dbe
import pytest

client = TestClient(app)

#################################################### Logged in Game Tests ####################################################
#################################################### Logged in Game Tests ####################################################
#################################################### Logged in Game Tests ####################################################


            ########################################       ########################################


# Game 1 has 8 players
#(player_number: md.PlayerNumber, game_id: int, user_id: int = Depends(auth.get_current_active_user)) -> int:

def return_token_minister():
    player_number_actual_minister= dbf.get_actual_minister(1)
    player_id_actual_minister = dbf.get_player_id_by_player_number(player_number_actual_minister, 1)
    user_id_actual_minister = dbf.get_user_id_by_player_id(player_id_actual_minister)

    if(user_id_actual_minister == 1): # Argentina
        return logIn.getToken_Argentina()
    elif(user_id_actual_minister == 2): # Brasil
        return logIn.getToken_Brasil()
    elif(user_id_actual_minister == 3):
        return logIn.getToken_Carol()
    elif(user_id_actual_minister == 4):
        return logIn.getToken_Dexter()
    elif(user_id_actual_minister == 5):
        return logIn.getToken_Esteban_quito()
    elif(user_id_actual_minister == 6):
        return logIn.getToken_FaMAF()
    elif(user_id_actual_minister == 7):
        return logIn.getToken_Ganzua()
    elif(user_id_actual_minister == 8):   
        return logIn.getToken_Hugo()

#! Game 1 Select director myself

#! Game 1 Select director Ok
def test_select_director():
    current_game= 1
    director_candidate= 1
    response= client.post(
                    "/games/1/select_director/",
                    headers= { 
                        "Authorization": return_token_minister()},
                    json= {
                        "playerNumber": director_candidate
                    })
    player_id_selected_candidate= dbf.get_player_id_by_player_number(director_candidate, current_game)
    player_nick_selected_candidate= dbf.get_player_nick_by_id(player_id_selected_candidate)
    assert response.status_code == 200
    assert response.json()["dir_game_response"] == (f" Player {player_nick_selected_candidate} is now director candidate")

#! Game 1 Vote candidate NO 4
def test_vote_candidate_Argentina():
    token= logIn.getToken_Argentina()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization": token
        },
        json= {
            "vote": False
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Argentina has voted"

def test_vote_candidate_Brasil():
    token= logIn.getToken_Brasil()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": False
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Brasil has voted"

def test_vote_candidate_Carol():
    token= logIn.getToken_Carol()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": False
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Carol has voted"

def test_vote_candidate_Dexter():
    token= logIn.getToken_Dexter()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": False
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Dexter has voted"

#! Game 1 Vote candidate OK 4
def test_vote_candidate_Esteban_quito():
    token= logIn.getToken_Esteban_quito()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Esteban_quito has voted"

def test_vote_candidate_FaMAF():
    token= logIn.getToken_FaMAF()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player FaMAF has voted"

def test_vote_candidate_Ganzua():
    token= logIn.getToken_Ganzua()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Ganzua has voted"

def test_vote_candidate_Hugo():
    token= logIn.getToken_Hugo()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Hugo has voted"

        #! NO APPROVE DIRECTOR !#

#! Game 1 Discard card OK

#! Game 1 Post proclamation OK

#! Game 1 Spell Avada Kedavra

#! Game 1 Spell Prophecy


