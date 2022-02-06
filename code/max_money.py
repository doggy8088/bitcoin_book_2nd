# 最初的區塊挖掘獎勵是50比特幣
start_block_reward = 50
# 平均每10分鐘挖掘一塊，每4年挖掘 210000 塊
reward_interval = 210000


def max_money():
    # 50 BTC = 50 0000 0000 Satoshis
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total

print("Total BTC to ever be created:", max_money(), "Satoshis")
