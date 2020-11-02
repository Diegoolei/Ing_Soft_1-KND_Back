from pony.orm import db_session, select, count, flush
import db_entities_relations as dbe 
import models as md
import helpers_functions as hf
from typing import Optional
from datetime import datetime
import random

##############################################################################################
##############################################################################################
######################################user functions##########################################
##############################################################################################
##############################################################################################


@db_session
def check_email_exists(new_email):
    return dbe.User.exists(user_email=new_email)


@db_session
def check_username_exists(new_uname):
    return dbe.User.exists(user_name=new_uname)


@db_session
def get_user_by_email(email):
    return dbe.User.get(user_email=email)


@db_session
def get_user_by_username(username):
    return dbe.User.get(user_name=username)


@db_session
def insert_user(email: str, username: str, password: str,
                photo: Optional[str]):
    """
    Adds a new user to the database
    """
    if photo is None:
        photo = "https://www.kindpng.com/imgv/hJhxTix_harrypotter-dobby-sticker-harry-potter-harry-potter-dobby/"
    
    dbe.User(
        user_email=email,
        user_name=username,
        user_password=password,
        user_photo=photo, 
        user_creation_dt=datetime.now())


##############################################################################################
##############################################################################################
######################################lobby functions#########################################
##############################################################################################
##############################################################################################


@db_session
def exist_lobby_name(lobbyIn_name):
    """
    Returns true if there is a lobby with that name
    """
    return dbe.Lobby.exists(lobby_name=lobbyIn_name)


@db_session
def check_max_players(lobbyIn_max_players):
    return not (5 <= lobbyIn_max_players <=10)


@db_session
def check_min_players(lobbyIn_min_players, lobbyIn_max_players):
    return not (5 <= lobbyIn_max_players <= lobbyIn_max_players <=10)


@db_session
def get_lobby_by_id(id: int):
    """
    Returns a Lobby from ID
    """
    return dbe.Lobby.get(lobby_id=id)


@db_session
def get_lobby_by_player_id(player_id: int):
    """
    Returns [Lobby] by player_id
    """
    return dbe.Player[player_id].player_lobby
    #return dbe.Lobby.get(playerSet[player_id=player_id]))


@db_session
def is_player_lobby_owner(player_id : int, lobby_id : int):
    """
    Returns "True" if the player_id is a owner of lobby_id
    """
    current_player = dbe.Player[player_id]
    return current_player.player_lobby.lobby_id == lobby_id


@db_session
def get_players_lobby(lobby_id : int):
    """
    Get [PLAYERS] of the lobby from id
    """
    players = dbe.Lobby[lobby_id].lobby_players
    return [p for p in players]  # list(players) :D


@db_session
def create_lobby(
                 lobbyIn_name: str,
                 lobbyIn_creator: int, #str,
                 lobbyIn_max_players: int, 
                 lobbyIn_min_players: int):
    lobby1= dbe.Lobby(
                    lobby_name = lobbyIn_name, 
                    lobby_creator = dbe.User[lobbyIn_creator].user_id, #lobbyIn_creator,
                    lobby_max_players = lobbyIn_max_players, 
                    lobby_min_players = lobbyIn_min_players)
    dbe.Lobby.select().show()
    return lobby1


@db_session
def join_lobby(current_user: int, lobby_id: int): # Review
    """
    Adds a user to a lobby. Creates (and returns) a player
    PRE : This does not check or return an error if user is 
    """
    player1 = dbe.Player(
                    player_user = dbe.User[current_user],
                    player_lobby = dbe.Lobby[lobby_id],
                    player_nick = dbe.User[current_user].user_name,
                    player_role = -1,
                    player_is_alive = True,
                    player_chat_blocked = False,
                    player_director = False,
                    player_minister = False
    )
    return  dbe.Lobby[lobby_id].lobby_name


@db_session
def is_user_in_lobby(user_id : int, lobby_id: int): # Final, its ok
    """
    Return True is the user_id is on lobby_id
    """
    user = dbe.User[user_id]
    lobby = dbe.Lobby[lobby_id]
    return (user in lobby.lobby_players.player_user)


## Terminar
@db_session
def leave_lobby(player_id: int): # Final, its ok
    """
    Removes current_user from a Lobby by id
    """
    print(f"Player {dbe.Player[player_id].player_nick} is leaving...")
    dbe.Player[player_id].delete()
    

# Pasar jugadores al Game
@db_session
def join_game(current_player: int, game_id : int): # ¿Final?
    """
    Add current_player from a Game
    """
    g = dbe.Game[game_id] # Game
    dbe.Player[current_player].player_game = g


@db_session
def get_number_of_players(lobby_id : int): # Final, its ok
    """
    Returns total player of the Lobby from id
    """
    total_players= 0 # Esta línea no tiene sentido
    l= dbe.Lobby[lobby_id] # Lobby
    total_players= l.lobby_players
    return len(total_players)


@db_session
def get_player_id_from_lobby(user_id: int, lobby_id: int):
    """
    Returns a player_id from  lobby_id
    
    Returns 0 if the user_id doesn't have a player in the lobby_id
    """
    # REVISAR print(dbf.get_player_id(2,1)) 2: user, lobby:1
    user_try = dbe.User[user_id].user_player
    print(user_try) # PlayerSet([Player[3]])
    for players in user_try:
        print((players.player_lobby.lobby_id == lobby_id))
        if (players.player_lobby.lobby_id == lobby_id):
            return players.player_id
    return 0

##############################################################################################
##############################################################################################
#####################################player functions#########################################
##############################################################################################
##############################################################################################


@db_session
def createPlayer(playerModelObj: md.PlayerOut): # Final, its ok
    """
    Creates a new Player
    """
    print(" Adding all players on the lobby")
    # p= 
    dbe.Player(player_game= 1,
    #player_lobby= Optional(Lobby)    # Depends on Lobby
    #player_id= Required(User)    # Depends on User
    #player_number= checkNumber(p), # Change checkNumber(p) from
    player_nick= playerModelObj.player_nick, 
    player_role= playerModelObj.player_role, 
    player_is_alive= playerModelObj.player_is_alive, 
    player_chat_blocked= playerModelObj.player_chat_blocked, 
    player_director= playerModelObj.player_director,
    player_minister= playerModelObj.player_minister)
    print("-> Player Added! ≧◉ᴥ◉≦\n")

##############################################################################################
##############################################################################################
#######################################game functions#########################################
##############################################################################################
##############################################################################################


## Esto lo hacemos para ver como construir a partir de modelos, no necesariamente va a ser asi...
@db_session
def insert_game(gameModelObj: md.ViewGame, lobby_id: id): # Final, its ok
    """
    Creates a new Game
    """
    print(" Creating a new game from ViewGame...")
    g= dbe.Game(game_is_started= False, 
    game_total_players= gameModelObj.game_total_players,
    game_next_minister= gameModelObj.game_next_minister, 
    game_failed_elections= gameModelObj.game_failed_elections, 
    game_step_turn= gameModelObj.game_step_turn, 
    game_last_director= gameModelObj.game_last_director, 
    game_last_minister= gameModelObj.game_last_minister)
    createBoardFromGame(g)
    print("-> Game Added! ≧◉ᴥ◉≦\n")
    
    ############################################################################################
    ####################################### REVIEW #############################################
    ############################################################################################
    
    # Pass players to al Game
    players = get_players_lobby(lobby_id)
    for p in players:
        p.player_game = g
    # Delete Lobby
    dbe.Lobby[lobby_id].delete()
    flush() ##
    game_p = dbe.Game[g.game_id].game_players #???
    print(len (game_p))
    
    # Select roles of the players
    print("\n ------")
    select_roles(g.game_total_players, game_p) ## select_roles(game_total_players, game_p)
    
    # Select orders of the players
    select_orders(game_p) ## select_orders(game_total_players, game_p)
    #list_players.append(player) # ["Player[0],: Pepe, 0, False, True, False...", "Lola", "Marta", "Jorge", "Lucas"]
    # Creo lobby A id= 1--> Creo Lobby B id=2--> Inicio Game B id=--> Inicio Game A
    print(" Starting a new game...")
    g.game_is_started = True
    print("-> Game Started! ≧◉ᴥ◉≦")
    
@db_session
def delete_lobby(lobby_id:int):
    """
    Deletes a Lobby from lobby_id
    """
    dbe.Lobby[lobby_id].delete()


@db_session # Review
def select_roles(game_total_players: int, game_p: set): # game_total_players: int, [PLAYERS]
    """
    Selectes role of player
    role: 0 Phoenix, 1 DeathEater, 2 Voldemort
    """
    print("\n select_roles()")
    if (game_total_players == 5): # 5 players: three phoenix(0), one death eater(1) and voldemort(2)
        print("\n Game total players: 5")
        roles = [0, 0, 0, 1, 2]
    elif (game_total_players == 6): # 6 players: four phoenix(0), one death eater(1) and volvemort(2)
        print("\n Game total players: 6")
        roles = [0, 0, 0, 0, 1, 2]
    elif (game_total_players == 7): # 7 players: four phoenix(0), two death eater(1) and voldemort(2)
        print("\n Game total players: 7")
        roles = [0, 0, 0, 0, 1, 1, 2]
    elif (game_total_players == 8): # 8 players: five phoenix(0), two death eater(1) and voldemort(2)
        print("\n Game total players: 8")
        roles = [0, 0, 0, 0, 0, 1, 1, 2]
    elif (game_total_players == 9): # 9 players: five phoenix(0), three death eater(1) and voldemort(2)
        print("\n Game total players: 9")
        roles = [0, 0, 0, 0, 0, 1, 1, 1, 2]
    elif (game_total_players == 10): # 10 players: six phoenix(0), three death eater(1) and voldemort(2)
        print("\n Game total players: 10")
        roles = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
    else: # Debuger
        raise ValueError("Error: Bad call. List of players should be between 5 and 10 >:C")
        
    random.shuffle(roles) # Asigned random order
    index = 0
    for player in game_p: # player[0] ... player[4]
        player.player_role = roles[index]
        index = index + 1

    print("\n select_roles() OK")
    

@db_session
def select_orders(game_p: set): # Review
    """
    Selectes order of players on game
    """
    print("\n Game total players: 5")
    #order = range(len(game_p) + 1)
    #random.shuffle(order)
    #random.shuffle(range(1, len(game_p) + 1)) ####### ERROR TypeError: 'range' object does not support item assignment
    #index = 0
    #for p in game_p:
    #    p.player_number = (range(1, len(game_p) + 1))[index]
    #    index = index + 1

    list_players=[0,1,2,3,4] # 5 players
    random.shuffle(list_players)
    for p in game_p:
        p.player_number= list_players[0]
        list_players.pop(0)
    print("\n select_orders()")


@db_session
def player_is_director():
    """
    Returns True if the player is the director
    """
    return dbe.Player[current_user].player_director


@db_session
def add_proclamation_card_on_board(is_phoenix: bool, game_id: int): # Final, its ok
    """
    Add card proclamation a Board from game_id 
    """
    print("Adding a new proclamation card o board...\n")
    b = dbe.Game[game_id].game_board_game
    # is_fenix: True
    if is_phoenix:
        print("Adding fenix ploclamation...")
        b.board_promulged_fenix = b.board_promulged_fenix + 1
        return (b.board_promulged_fenix)
    # is_fenix: False
    else:
        print("Adding death eater ploclamation...")
        b.board_promulged_death_eater = b.board_promulged_death_eater + 1
        return (b.board_promulged_death_eater)
    print("-> Proclamation card added on board ≧◉ᴥ◉≦\n")
    #return b
    #return (b.board_promulged_fenix, b.board_promulged_death_eater)


##############################################################################################
##############################################################################################
######################################board functions#########################################
##############################################################################################
##############################################################################################

@db_session
def createBoardFromGame(vGame: md.ViewGame): # Final, its ok
    """
    Creates a Board from Game
    """
    print(" Creating a new board from game...")
    dbe.Board(board_game= vGame, 
    board_promulged_fenix= 0, 
    board_promulged_death_eater= 0, 
    board_deck_codification= hf.generate_new_deck(),
    board_is_spell_active= 0)
    print("-> Board Added ≧◉ᴥ◉≦")


#@db_session
#def deck_order(proclamed_fenix: int = 0, proclamed_death_eater: int = 0): # board_id: in    

@db_session
def get_board_information(): # For endpoint
    """
    
    """
    return True


@db_session
def getFirstCardFromDeck(deckTry: list): # Final, its ok
    """
    Returns the first card of the deck
    """
    card = deckTry[0]
    # Remove the card
    removeCard(deckTry)
    # Proclamar
    return card


@db_session
def removeCard(deck_try: list): # Fianl, its ok
    """
    Return a list of deck without first card
    """
    print(" Removing a card...")
    # [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
    # Add the card at discardedCards
    # discardedCards(deck_try[0])
    # Remove the card
    deck_try.pop(0)
    print("-> Card removed OK ≧◉ᴥ◉≦\n")
    return deck_try


"""@db_session
def discardedCards(card: int):
    #print(" Adding a card to descartes deck...")
    deck_descartes: list
    # Add a card to the end of the list
    deck_descartes.append()   
    #print("-> Discarded Cards OK ≧◉ᴥ◉≦\n")
    #return ... (devuelve las cartas descartadas)"""


##############################################################################################
##############################################################################################
######################################log functions#########################################
##############################################################################################
##############################################################################################

#@db_sesion
#def add():

##############################################################################################
##############################################################################################
######################################data functions#########################################
##############################################################################################
##############################################################################################
@db_session
def testFunc():
    print(dbe.Game[1])


@db_session
def showDatabase(): # NO TOCAR
    """
    Shows database
    """
    print("---|Users|---(user_id, user_email, user_name, user_password, user_photo, user_creation_dt, #user_lobby, user_player, user_log, user_defau)")
    dbe.User.select().show()
    print("\n---|Lobbies|---(lobby_id, lobby_name, lobby_max_players, lobby_min_players, lobby_creator, lobby_user, lobby_players)")
    dbe.Lobby.select().show()
    print("\n---|Games|---(id, game_board_game, game_is_started, game_total_players, game_next_minister, game_failed_elections, game_step_turn, game_last_director, game_last_minister)")
    dbe.Game.select().show()
    print("\n---|Boards|---(id, board_game, board_promulged_fenix, board_promulged_death_eater, board_deck_codification, board_is_spell_active)")
    dbe.Board.select().show()
    print("\n---|Players|---(player_id, player_number, player_nick, player_role, player_is_alive, player_chat_blocked, player_director, player_minister, player_game, player_lobby, player_user)")
    #print("\n---|Players|---(id, player_game, player_lobby, player_number, player_nick, player_role, player_is_alive, player_chat_blocked, player_director, player_minister)")
    dbe.Player.select().show()
    #dbe.Log.select().show()