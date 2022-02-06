from __future__ import print_function
import bitcoin

# 隨機產生一個私鑰
valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decoded_private_key < bitcoin.N

print("Private Key (hex) is: ", private_key)
print("Private Key (decimal) is: ", decoded_private_key)

# 將私鑰轉換為WIF格式
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print("Private Key (WIF) is: ", wif_encoded_private_key)

# 新增"01"字尾，表示壓縮的私鑰
compressed_private_key = private_key + '01'
print("Private Key Compressed (hex) is: ", compressed_private_key)

# 產生 WIF-compressed
wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif_compressed')
print("Private Key (WIF-Compressed) is: ", wif_compressed_private_key)

# 乘以EC產生點G，產生公鑰
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
print("Public Key (x,y) coordinates is:", public_key)

# 編碼成十六進位制，以04開頭
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print("Public Key (hex) is:", hex_encoded_public_key)

# 壓縮公鑰，根據y是偶數還是奇數來調整字首
(public_key_x, public_key_y) = public_key
compressed_prefix = '02' if (public_key_y % 2) == 0 else '03'
hex_compressed_public_key = compressed_prefix + (bitcoin.encode(public_key_x, 16).zfill(64))
print("Compressed Public Key (hex) is:", hex_compressed_public_key)

# 從公鑰產生比特幣地址
print("Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(public_key))

# 從壓縮的公鑰產生壓縮的比特幣地址
print("Compressed Bitcoin Address (b58check) is:",
      bitcoin.pubkey_to_address(hex_compressed_public_key))
