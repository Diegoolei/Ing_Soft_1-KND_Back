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

def return_token_NOT_minister():
    player_number_actual_minister= dbf.get_actual_minister(1)
    player_id_actual_minister = dbf.get_player_id_by_player_number(player_number_actual_minister + 1, 1)
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
        
def return_token_director():
    player_number_actual_director= dbf.get_actual_director(1)
    player_id_actual_director= dbf.get_player_id_by_player_number(player_number_actual_director, 1)
    user_id_actual_director= dbf.get_user_id_by_player_id(player_id_actual_director)

    if(user_id_actual_director == 1): # Argentina
        return logIn.getToken_Argentina()
    elif(user_id_actual_director == 2): # Brasil
        return logIn.getToken_Brasil()
    elif(user_id_actual_director == 3):
        return logIn.getToken_Carol()
    elif(user_id_actual_director == 4):
        return logIn.getToken_Dexter()
    elif(user_id_actual_director == 5):
        return logIn.getToken_Esteban_quito()
    elif(user_id_actual_director == 6):
        return logIn.getToken_FaMAF()
    elif(user_id_actual_director == 7):
        return logIn.getToken_Ganzua()
    elif(user_id_actual_director == 8):   
        return logIn.getToken_Hugo()


# #! Game 1 Select director myself #! FIXME test_select_director_myself
# def test_select_director_myself():
#     response= client.post(
#                     "/games/1/select_director/",
#                     headers= { 
#                         "Authorization": return_token_minister()},
#                     json= {
#                         "playerNumber": 0
#                     }) 
#     assert response.status_code == 412

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
            "Authorization": token
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

        #? NO APPROVE DIRECTOR !#

#?##################### NEW TURN #############################

#! Try to vote with candidate without candidate
def test_vote_candidate_412():
    token= return_token_NOT_minister()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization": token
        },
        json= {
            "vote": True
        }
    )
    assert response.status_code == 412

#! NOT Minister
def test_discard_card_NOT_Minister():
    response= client.put(
        "/games/1/discard_card/",
        headers= {
            "Authorization": return_token_NOT_minister()
        },
        json= {
            "card_discarted": 1
        }
    )
    assert response.status_code == 412

#! Minister try discard card
def test_discard_card_Minister_412():
    response= client.put(
        "/games/1/discard_card/",
        headers= {
            "Authorization": return_token_minister()
        },
        json= {
            "card_discarted": 1
        }
    )
    assert response.status_code == 412

#! Director try discard card
def test_discard_card_Director_412():
    response= client.put(
        "/games/1/discard_card/",
        headers= {
            "Authorization": return_token_minister()
        },
        json= {
            "card_discarted": 1
        }
    )
    assert response.status_code == 412

        #? Game 1 Select candidate !#

def test_select_director_1(): #! FIXME test_select_director_1
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
    assert response.json()["dir_game_response"] == (f" Player {player_nick_selected_candidate} is now director candidate")
    #assert response.json() == "Algo"
    assert response.status_code == 200

        #! Game 1 Vote candidate OK 8
def test_vote_candidate_Argentina_OK():
    token= logIn.getToken_Argentina()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization": token
        },
        json= {
            "vote": True
        }
    )
    #assert response.json()["voteOut_response"] == " Player Argentina has voted"
    assert response.status_code == 200

def test_vote_candidate_Brasil_OK():
    token= logIn.getToken_Brasil()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    #assert response.json()["voteOut_response"] == " Player Brasil has voted"
    assert response.status_code == 200

def test_vote_candidate_Carol_OK():
    token= logIn.getToken_Carol()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    #assert response.json()["voteOut_response"] == " Player Carol has voted"
    assert response.status_code == 200
    
def test_vote_candidate_Dexter_OK():
    token= logIn.getToken_Dexter()
    response= client.put(
        "/games/1/select_director/vote",
        headers= {
            "Authorization":  token
        },
        json= {
            "vote": True
        }
    )
    #assert response.json()["voteOut_response"] == " Player Dexter has voted"
    assert response.status_code == 200   

def test_vote_candidate_Esteban_quito_OK():
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
    #assert response.status_code == 200
    assert response.json()["voteOut_response"] == " Player Esteban_quito has voted"

def test_vote_candidate_FaMAF_OK():
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
    #assert response.json()["voteOut_response"] == " Player FaMAF has voted"
    assert response.status_code == 200

def test_vote_candidate_Ganzua_OK():
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
    #assert response.json()["voteOut_response"] == " Player Ganzua has voted"
    assert response.status_code == 200   

def test_vote_candidate_Hugo_OK():
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
    #assert response.json()["voteOut_response"] == " HOLA"
    assert response.json()["voteOut_response"] == " Player Hugo has voted"
    assert response.status_code == 200

        #? APPROVE DIRECTOR !#

#! Game 1 Discard card OK
# #! Minister
# def test_discard_card_Minister():
#     response= client.put(
#         "/games/1/discard_card/",
#         headers= {
#             "Authorization": return_token_minister()
#         },
#         json= {
#             "card_discarted": 1
#         }
#     )
#     assert response.json()["detail"] == " Player Hugo has voted"
#     assert response.status_code == 200

# #! Director
# def test_discard_card_Director():
#     response= client.put(
#         "/games/1/discard_card/",
#         headers= {
#             "Authorization": return_token_director()
#         },
#         json= {
#             "card_discarted": 1
#         }
#     )
#     assert response.status_code == 200
#     assert response.json()["voteOut_response"] == " Player Hugo has voted"

# def return_first_card_on_deck():
#     board_deck_decoded= dbf.get_decoded_deck(1)
#     return dbf.getFirstCardFromDeck(board_deck_decoded)

# #! Game 1 Post proclamation OK
# def test_post_proclamation_1():
#     response= client.put(
#         "/games/1/proclamation/",
#         headers= {
#             "Authorization": return_token_director()
#         },
#         json= {
#             "proclamationCard_phoenix": return_first_card_on_deck()
#         }
#     )
#     assert response.status_code == 200

#! Game 1 Spell Avada Kedavra

#! Game 1 Spell Prophecy