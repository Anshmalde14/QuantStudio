
# Assets
ASSETS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "GLD",
    "BTC-USD",
    "SPY"
]

# Assets to train during development
TRAIN_ASSETS = [
    "AAPL"
]

# Data
START_DATE = "2015-01-01"
END_DATE = None

# Target
VOLATILITY_WINDOW = 20

# Sequence
SEQUENCE_LENGTH = 60

# Train/Test
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Paths
RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"
MODEL_PATH = "models"