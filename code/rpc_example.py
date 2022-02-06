from bitcoin.rpc import RawProxy

# 與本地Bitcoin Core節點創建連接
p = RawProxy()

# 運行 getblockchaininfo 命令, 將返回數據保存到info中
info = p.getblockchaininfo()

# 印出info中的blocks内容
print(info['blocks'])
