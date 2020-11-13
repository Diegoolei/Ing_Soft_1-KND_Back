# Socket Communication Specification  
The websocket communication allows to send Python *dictionaries*, in such a way that on the Front end we can transform them into **JSON (JavaScript Object Notation)**.  
We **cannot** send *Models*. We can only send plain strings, or python dictionaries.  
This file specifies what the Front end expects from the websocket.  
## **General structure:**  
Sending pure strings are depreciated. Even basic chat will be sent by dictionary. The structure of all messages will be of the form:  
```
{
    "TYPE": ...,
    "PAYLOAD": ...
}
```
The *keys* `TYPE` and `PAYLOAD` should always be present
The value of `TYPE` signals the type of **action** we're signaling the player, the value in `PAYLOAD` is relevant information (read: *arguments*) necesary to perform the action.

## Register (POST) /users/
No socket communication
## Login (POST) /login/
No socket communication
## User Information (GET) /users/  
No socket communication
## Update Profile (PATCH) /users/change_profile/
No socket communication
## Change Password (PATCH) /users/change_profile/change_password/
No socket communication
## Create New Lobby (POST) /lobby/
No socket communication
## List Lobbies (GET) /lobby/list_lobbies/
No socket communication  

---  

## Join Lobby (POST) /lobby/{lobby_id}/
`{ "TYPE": "NEW_PLAYER_JOINED", "PAYLOAD": nick (str) }`  

**Send to:** All players in lobby  
**Include Endpoint Sender**: NO

---  

## Change Nick (POST) /lobby/{lobby_id}/change_nick
`{ "TYPE": "CHANGED_NICK", "PAYLOAD": payload (dict) }`  

with **payload** = `{ "OLD_NICK": (str), "NEW_NICK": (str) }`  

**Send to:** All players in lobby  
**Include Endpoint Sender**: YES

---  

## Leave Lobby (DELETE) /lobby/{lobby_id}/
`{ "TYPE": "PLAYER_LEFT", "PAYLOAD": nick (str) }`  

**Send to:** All players in lobby  
**Include Endpoint Sender**: NO

---  

## Start Game (DELETE) /lobby/{lobby_id}/start_game/
`{ "TYPE": "START_GAME", "PAYLOAD": game_id (int) }`  

**Send to:** All players in lobby  
**Include Endpoint Sender**: YES

---  

## List Games  
No socket communication  

---  

## Start of Turn *(Various endpoints)*
When we need to choose a new Minister:  
`{ "TYPE": "NEW_MINISTER", "PAYLOAD": player_number (int) }`  

**Send to:** All players in game  
**Include Endpoint Sender**: YES  

**Also** send the available candidates for Director to the Minister  

`{ "TYPE": "REQUEST_CANDIDATE", "PAYLOAD": available_candiates (list of player_number) }`  

**Send to:** Current Minister  
Example: `{ "TYPE": "REQUEST_CANDIDATE", "PAYLOAD": [3, 4, 6] }`  
Note: **player_number**, not *player_id*  

---  

## Select Director (POST) /games/{game_id}/select_director/
We need to ask everyone to vote for the candidate the Minister selected:  

`{ "TYPE": "REQUEST_VOTE", "PAYLOAD": candidate_number (player_number) }`  

**Send to:** All players in game  
**Include Endpoint Sender**: YES  

---  
## Vote (PUT) /games/{game_id}/select_director/vote
### If not all votes are entered:  
No socket communication  
### If last vote:
`{ "TYPE": "ELECTION_RESULT", "PAYLOAD": votes (dict) }`  

with **votes** = `[ player_number (int) : vote (bool) ]`  
with **v**: True => LUMOS  
**Send to:** All players in game  
**Include Endpoint Sender**: YES  

### If candidate was **ACCEPTED**:  
`{ "TYPE": "MINISTER_DISCARD", "PAYLOAD": [card1, card2, card3] (list of 3 str) }`  

with **cardx** = `"PHOENIX_PROCLAMATION"` or `"DEATH_EATER_PROCLAMATION"`  
**Send to:** Current Minister  

### If candidate was **REJECTED** and **CAOS**:  
`{ "TYPE": "CAOS_PROCLAMATION", "PAYLOAD": proclamation (str) }`  

with **proclamation** = `"PHOENIX_PROCLAMATION"` or `"DEATH_EATER_PROCLAMATION"`  
**Send to:** All players in game  
**Include Endpoint Sender**: YES  

---  
## Discard Card (PUT) /games/{game_id}/discard_card/
### If minister is discarding  
`{ "TYPE": "DIRECTOR_DISCARD", "PAYLOAD": [card1, card2] (list of 2 str) }`  

with **cardx** = `"PHOENIX_PROCLAMATION"` or `"DEATH_EATER_PROCLAMATION"`  
**Send to:** Current Director  
### If director is discarding  
No socket communication  

---
## Post Proclamation (PUT) /games/{game_id}/proclamation/
`{ "TYPE": "PROCLAMATION", "PAYLOAD": proclamation (str) }`  

with **proclamation** = `"PHOENIX_PROCLAMATION"` or `"DEATH_EATER_PROCLAMATION"`  
**Send to:** All players in game  
**Include Endpoint Sender**: YES  

---
## End Game *(Various Endpoints)*  
-  

---
## Trigger Spell *(End of Post Proclamation)*  
-  

---
## Adivination (GET) /games/{game_id}/spell/prophecy/  
So we can show that the minister is doing this  
`{ "TYPE": "ADIVINATION_NOTICE", "PAYLOAD": minister_number (player_number) }`  

**Send to:** All players in game  
**Include Endpoint Sender**: NO

--- 
## Avada Kedavra
`{ "TYPE": "AVADA_KEDAVRA", "PAYLOAD": victim_number (player_number) }`  

**Send to:** All players in game  
**Include Endpoint Sender**: NO


--- 
## --
-

--- 
## --
-

--- 
## --
-

--- 
## --
-

--- 
## --
-

--- 
## --
-

--- 
## --
-
