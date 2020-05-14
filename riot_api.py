from riotwatcher import LolWatcher
import pprint

pp = pprint.PrettyPrinter(indent=4)

api_key = 'RGAPI-a064518f-62a0-42fd-9ad3-793e608ee818'
watcher = LolWatcher(api_key)
my_region = 'eun1'

# játékos adatainak lekérdezése
me = watcher.summoner.by_name(my_region, 'BazyJoe')
# ranked adatok lekérdezése játékos ID alapján
pp.pprint(me)

# a legutolsó meccs adati account ID alapján
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
pp.pprint(my_matches)
