from pony.orm import Database, PrimaryKey, Required, Optional, Set

db = Database()

#user entity


#lobby entity


#game entity


#player entity
class Player(db.entity):
    player_lobby            = Required(Lobby)
    #player_id              = Required(User) # Depends on User
    player_number           = Required(int, unique = True)    # Definied order
    player_nick             = Required(str)    # = userName Depends on User
    player_role             = Required(bool)
    player_is_alive         = Required(bool)    # = True
    player_chat_blocked     = Required(bool)    # = False
    player_director         = Required(bool)
    player_minister         = Required(bool)

#board entity
class Board(db.entity):
    proclamation_promulged_fenix: Required(int)    # = 0
    proclamation_promulged_death_eater: Required(int)    # = 0
    deck_codification: Required(int)    # binarie
    is_spell_active: Required(bool)    # = False

#end match
class End_Match():
    is_end : Required(bool) # = True Depends on "Game"     
      
#history entity


# connect the object 'db' with data base
db.bind('sqlite', 'data_base.sqlite', create_db=True)
# generate the data base
db.generate_mapping(create_tables=True)

