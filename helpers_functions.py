# Add imports
import random
import db_functions as dbf
######################################################################################################################
################################################ USER FUNCTIONS #######################################################
######################################################################################################################


def valid_format_username(uname) -> bool:
    return 3 < len(uname) < 21
  
def valid_format_password(password) -> bool:
    return 7 < len(password) < 33


######################################################################################################################
################################################ GAME FUNCTIONS #######################################################
######################################################################################################################

# This function encodes the list "deck" and return an int
def encode_deck(deckList : list):
    """
    Returns a encoded deck as int
   
    First bit with 1 of deckInt point the size of deck. Doesn't encode a card
    """
    # deckList = [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    # returns : 228805 = 0b110111110111000101
    # deckList [1,1,0,0] => deckInt 0b[1]1100 first bit with 1 points to start of deck
    deckInt = 1   # Represents an empty deck
    for card in deckList:
        if (card == 0):
            deckInt = (deckInt << 1)    # add phoenix card
        else:
            deckInt = (deckInt << 1) + 1    # add death_eater card
    return deckInt # Return encoded "deck" for database


def decode_deck(deckInt : int):
    """
    Returns a decoded deck as list
    """
    # deckInt = 228805 = 0b110111110111000101
    # returns: [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    deckList = list(bin(deckInt))[3:]
    return [int(item) for item in deckList] # Return decoded "deck" for easy use with lists on functions


def generate_new_deck(proclaimed_fenix: int = 0, proclaimed_death_eater: int = 0):
    """
    generate_new_deck(): If the arguments are empty, so the function create a new deck as default
    
    Returns a shuffled deck based on the rules of the game, excluding the cards that were proclaimed
    17 Total cards : 6 phoenix (zero) and 11 death_eather (one) 
    Example: [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
    """
    print(" Generating a new deck...")
    decklist = list()
    for _ in range(11 - proclaimed_death_eater):
        decklist.append(1)
    for _ in range(6 - proclaimed_death_eater):
        decklist.append(0)
    random.shuffle(decklist)    # Order
    #print(decklist)
    #print("-> Deck order OK ≧◉ᴥ◉≦\n")
    return encode_deck(decklist)


def caos_promulgate_card(game_id: int):

    promulgated_card = dbf.remove_card_for_proclamation(game_id)
    board = dbf.add_proclamation_card_on_board(promulgated_card, game_id) 

    # Informs all the players what proclamation has been posted
    socketDic= { "TYPE": "CHAOS", "PAYLOAD": promulgated_card }
    await wsManager.broadcastInGame(game_id, socketDic)
    
    if(board[0] >= 5): # Phoenixes win when they manage to post 5 of their proclamations
        players = dbf.get_players_game(game_id) # [PLAYERS]
        result= {}
        for player in players:
            role= dbf.get_player_role(player.player_id)
            result[player.player_nick]= role
        socketDict2= { "WINNER": 0, "PAYLOAD": result }
        socketDict={ "TYPE": "END_GAME", "PAYLOAD": socketDict2 }
        await wsManager.broadcastInGame(game_id, socketDict)
 
        raise_exception(
            status.HTTP_307_TEMPORARY_REDIRECT,
            " Free Dobby appears and congratulates the Phoenixes with a sock, hagrid is happy too ♥ Dracco Malfloy disturbs an Hippogriff peace, gets 'beaked' and cries"
        )
   
    elif(board[1] >= 6):  # DE win when they manage to post 6 of their proclamations
        players = dbf.get_players_game(game_id) # [PLAYERS]
        result= {}
        for player in players:
            role= dbf.get_player_role(player.player_id)
            result[player.player_nick]= role
        socketDict2= { "WINNER": 0, "PAYLOAD": result }
        socketDict={ "TYPE": "END_GAME", "PAYLOAD": socketDict2 }
        await wsManager.broadcastInGame(game_id, socketDict)
        
        raise_exception(
            status.HTTP_307_TEMPORARY_REDIRECT,
            " Sirius Black is dead, Hagrid and Dobby (with a dirty and broken sock) die"
        )

        coded_game_deck= dbf.get_coded_deck(game_id)
        decoded_game_deck= dbf.get_decoded_deck(coded_game_deck)

        if(len(decoded_game_deck) < 3): # shuffles the deck if there are less than 3 cards
            # Checks how many proclamations are posted (if they have been posted, they cant be in the deck)
            total_phoenix= dbf.get_total_proclamations_phoenix(game_id)
            total_death_eater= dbf.get_total_proclamations_death_eater(game_id)
            new_deck= hf.generate_new_deck(total_phoenix, total_death_eater)
            dbf.set_new_deck(new_deck, game_id)
        
