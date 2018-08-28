# LOGGING CONSTANTS
LOG_DIRECTORY = "log/"
DATE_FORMAT = "%d %b %H:%M:%S"

# WALLET CONSTANTS
WALLET_STORAGE_FILE = "wallets.log"

# DNS SEED CONSTANTS
ENTRY_DURATION = 60 * 60 * 24 * 1  # duration in seconds
SEED_SERVER_URL = "http://localhost:8080"
SEED_SERVER_PORT = 8080

# MINER CONSTANTS
MINER_SERVER_PORT = 9000
MINER_VERSION = "0.1"

# DB CONSTANTS
BLOCK_DB_LOC = "db/block.db"

# BLOCKCHAIN CONSTANTS
TRANSACTION_ID_LENGTH_HEX = 64  # 256 bit string is 64 hexa_dec string

MAX_BLOCK_SIZE_KB = 4096
MAX_SATOSHIS_POSSIBLE = 21_000_000 * 100_000_000

# A block cannot have timestamp greater than this time in the future
BLOCK_MAX_TIME_FUTURE_SECS = 2 * 60 * 60

BLOCK_DIFFICULTY_UPDATE_INTERVAL = 1024  # number of blocks
AVERAGE_BLOCK_MINE_INTERVAL = 10 * 60  # seconds
MAXIMUM_TARGET_DIFFICULTY = 255
