from beem import Steem
stm = Steem()
print(stm.get_config(1)["STEEMIT_MAX_PERMLINK_LENGTH"])

print(stm.get_config()["STEEMIT_MIN_PERMLINK_LENGTH"])
