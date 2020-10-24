from pony.orm import Database, PrimaryKey, Required, Optional, Set

db = Database()

#user entity


#lobby entity

class Lobby(db.Entity):
    match_id            = PrimaryKey(int, auto = True)
    lobby_creator       = Required(str)     # User.username
    lobby_name          = Required(str, unique=True)
    max_amount_players  = Required(int)
    min_amount_players  = Required(int)
    match_started       = Required(bool)
    players             = Set('Player')     # 1-* relation with Lobby-Player, we use '' because Player is declarated after this call 
 
#game entity


#player entity

class Player(db.Entity):
    player_lobby            = Required(Lobby)
    #player_id               = Required(User) #Depends on User
    player_number           = Required(int, unique = True)
    player_nick             = Required(str) 
    player_role             = Required(bool)
    player_is_alive         = Required(bool)
    player_chat_blocked     = Required(bool)
    player_director         = Required(bool)
    player_minister         = Required(bool)



#board entity


#history entity


# connect the object 'db' with data base
db.bind('sqlite', 'data_base.sqlite', create_db=True)
# generate the data base
db.generate_mapping(create_tables=True)