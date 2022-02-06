#include <random>
#include <bitcoin/bitcoin.hpp>

// 要搜尋的字串
const std::string search = "1kid";

// 隨機生成密鑰
bc::ec_secret random_secret(std::default_random_engine& engine);
// 從EC密鑰中生成比特幣地址
std::string bitcoin_address(const bc::ec_secret& secret);
// 與要搜尋的字串進行比较（大小寫敏感）
bool match_found(const std::string& address);

int main()
{
    // Linux上的 random_device 使用 "/dev/urandom"
    // 注意: 根據具體實作，隨機源可能不足夠安全!
    // 不要在正式環境使用本範例中生成的 vanity keys
    std::random_device random;
    std::default_random_engine engine(random());

    // 無限循環...
    while (true)
    {
        // 生成隨機私鑰.
        bc::ec_secret secret = random_secret(engine);
        // 生成地址
        std::string address = bitcoin_address(secret);
        // 是否與目標字串匹配 (1kid)
        if (match_found(address))
        {
            // 成功
            std::cout << "Found vanity address! " << address << std::endl;
            std::cout << "Secret: " << bc::encode_base16(secret) << std::endl;
            return 0;
        }
    }
    // 不可能運行到這裡!
    return 0;
}

bc::ec_secret random_secret(std::default_random_engine& engine)
{
    // 生成新的密鑰...
    bc::ec_secret secret;
    // 遍歷每個字節設置隨機值...
    for (uint8_t& byte: secret)
        byte = engine() % std::numeric_limits<uint8_t>::max();
    // 返回結果.
    return secret;
}

std::string bitcoin_address(const bc::ec_secret& secret)
{
    // 將密鑰轉換為付款地址
    bc::wallet::ec_private private_key(secret);
    bc::wallet::payment_address payaddr(private_key);
    // 返回加密的形式.
    return payaddr.encoded();
}

bool match_found(const std::string& address)
{
    auto addr_it = address.begin();
    // 比較字串前缀
    for (auto it = search.begin(); it != search.end(); ++it, ++addr_it)
        if (*it != std::tolower(*addr_it))
            return false;
    // 匹配
    return true;
}
