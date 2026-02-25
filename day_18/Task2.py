# installing modules that are not part of python's standard library
import heroes
import villains

hero_name = heroes.gen()
villain_name = villains.gen()
print(f"hero = {hero_name}, villain = {villain_name}")


marvel_team = heroes.genarr(5)
villain_team = villains.genarr(5)
print(f"marvel's team {marvel_team} VS. {villain_team}")