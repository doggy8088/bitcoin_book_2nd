#include <random>
#include <bitcoin/bitcoin.hpp>

// 要搜尋的字串
const std::string search = "1kid";

// 隨機產生金鑰
bc::ec_secret random_secret(std::default_random_engine& engine);
// 從EC金鑰中產生比特幣地址
std::string bitcoin_address(const bc::ec_secret& secret);
// 與要搜尋的字串進行比較（大小寫敏感）
bool match_found(const std::string& address);

int main()
{
    // Linux上的 random_device 使用 "/dev/urandom"
    // 注意: 根據具體實現，隨機源可能不是足夠安全的!
    // 不要在生產環境中使用本例產生的虛榮地址
    std::random_device random;
    std::default_random_engine engine(random());

    // 連續迴圈...
    while (true)
    {
        // 產生隨機私鑰.
        bc::ec_secret secret = random_secret(engine);
        // 產生地址
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
    // 不可能執行到這裡
    return 0;
}

bc::ec_secret random_secret(std::default_random_engine& engine)
{
    // 產生新的金鑰...
    bc::ec_secret secret;
    // 遍歷每個位元組設定隨機值...
    for (uint8_t& byte: secret)
        byte = engine() % std::numeric_limits<uint8_t>::max();
    // 返回結果.
    return secret;
}

std::string bitcoin_address(const bc::ec_secret& secret)
{
    // 將金鑰轉換為付款地址
    bc::wallet::ec_private private_key(secret);
    bc::wallet::payment_address payaddr(private_key);
    // 返回加密的形式.
    return payaddr.encoded();
}

bool match_found(const std::string& address)
{
    auto addr_it = address.begin();
    // 比較字串字首
    for (auto it = search.begin(); it != search.end(); ++it, ++addr_it)
        if (*it != std::tolower(*addr_it))
            return false;
    // 匹配
    return true;
}
