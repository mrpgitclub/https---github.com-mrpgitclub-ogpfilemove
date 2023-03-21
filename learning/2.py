import sqlite3

my_con = sqlite3.Connection("tables.db")
my_cursor = sqlite3.Cursor(my_con)

#my_cursor.execute("create table main.characters(num numeric,character_name text,class text)")
#my_cursor.execute("insert into characters values (?,?,?)")

my_cursor.execute("create table main.tables(Obscure_encounters text,Wilderness_hooks text,General_Story_Hooks text,City_plots text,Npc_Traits text,Encounters_b text,Dungeon_dangers text,Overheard_phrases text,inn_encounters text)")
