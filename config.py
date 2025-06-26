"""
Configuration file for trading instruments and parameters
"""

# Market Configuration
MARKET_CONFIG = {
    "timezone": "Asia/Kolkata",
    "market_open": "09:15",
    "market_close": "15:30",
    "trading_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
}

# Primary Trading Instruments
INSTRUMENTS = {
    "indices": {
        "NIFTY50": {
            "symbol": "^NSEI",
            "name": "Nifty 50",
            "exchange": "NSE",
            "description": "NSE Nifty 50 Index"
        },
        "BANKNIFTY": {
            "symbol": "^NSEBANK",
            "name": "Bank Nifty",
            "exchange": "NSE", 
            "description": "NSE Bank Nifty Index"
        },
        "SENSEX": {
            "symbol": "^BSESN",
            "name": "Sensex",
            "exchange": "BSE",
            "description": "BSE Sensex Index"
        }
    },
    
    "stocks": {
        "RELIANCE": {
            "symbol": "RELIANCE.NS",
            "name": "Reliance Industries",
            "exchange": "NSE",
            "sector": "Oil & Gas"
        },
        "TCS": {
            "symbol": "TCS.NS", 
            "name": "Tata Consultancy Services",
            "exchange": "NSE",
            "sector": "IT"
        },
        "HDFCBANK": {
            "symbol": "HDFCBANK.NS",
            "name": "HDFC Bank",
            "exchange": "NSE", 
            "sector": "Banking"
        },
        "INFY": {
            "symbol": "INFY.NS",
            "name": "Infosys",
            "exchange": "NSE",
            "sector": "IT"
        },
        "ICICIBANK": {
            "symbol": "ICICIBANK.NS",
            "name": "ICICI Bank",
            "exchange": "NSE",
            "sector": "Banking"
        }
    },
    
    "etfs": {
        "NIFTYBEES": {
            "symbol": "NIFTYBEES.NS",
            "name": "Nippon India ETF Nifty BeES",
            "exchange": "NSE",
            "tracks": "NIFTY50"
        },
        "BANKBEES": {
            "symbol": "BANKBEES.NS", 
            "name": "Nippon India ETF Bank BeES",
            "exchange": "NSE",
            "tracks": "BANKNIFTY"
        }
    }
}

# Default Trading Parameters
TRADING_PARAMS = {
    "default_period": "1d",
    "default_interval": "5m",
    "available_intervals": ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"],
    "available_periods": ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
}

# SuperTrend Indicator Settings
SUPERTREND_CONFIG = {
    "default_period": 10,
    "default_multiplier": 3.0,
    "periods": [7, 10, 14, 21],
    "multipliers": [2.0, 2.5, 3.0, 3.5, 4.0]
}

# Data Sources Configuration
DATA_SOURCES = {
    "primary": "yfinance",
    "backup": None,  # Can be configured for other data sources
    "rate_limit": {
        "requests_per_second": 2,
        "requests_per_minute": 100
    }
}

# Utility Functions
def get_instrument_symbol(instrument_type: str, instrument_name: str) -> str:
    """
    Get the symbol for a specific instrument
    
    Args:
        instrument_type: Type of instrument ('indices', 'stocks', 'etfs')
        instrument_name: Name/key of the instrument
        
    Returns:
        str: Symbol for the instrument or None if not found
    """
    try:
        return INSTRUMENTS[instrument_type][instrument_name]["symbol"]
    except KeyError:
        return None

def get_all_symbols(instrument_type: str = None) -> list:
    """
    Get all symbols for a specific instrument type or all symbols
    
    Args:
        instrument_type: Optional instrument type filter
        
    Returns:
        list: List of symbols
    """
    symbols = []
    
    if instrument_type:
        if instrument_type in INSTRUMENTS:
            symbols = [data["symbol"] for data in INSTRUMENTS[instrument_type].values()]
    else:
        for inst_type in INSTRUMENTS.values():
            symbols.extend([data["symbol"] for data in inst_type.values()])
    
    return symbols

def get_instrument_info(symbol: str) -> dict:
    """
    Get instrument information by symbol
    
    Args:
        symbol: The symbol to search for
        
    Returns:
        dict: Instrument information or None if not found
    """
    for inst_type, instruments in INSTRUMENTS.items():
        for inst_name, inst_data in instruments.items():
            if inst_data["symbol"] == symbol:
                return {
                    "type": inst_type,
                    "name": inst_name,
                    **inst_data
                }
    return None

def validate_trading_params(period: str, interval: str) -> bool:
    """
    Validate if the given period and interval are supported
    
    Args:
        period: Trading period
        interval: Trading interval
        
    Returns:
        bool: True if valid, False otherwise
    """
    return (period in TRADING_PARAMS["available_periods"] and 
            interval in TRADING_PARAMS["available_intervals"])

# Default instrument for quick access
DEFAULT_INSTRUMENT = get_instrument_symbol("indices", "NIFTY50")

# Print configuration summary
def print_config_summary():
    """Print a summary of the configuration"""
    print("=" * 50)
    print("TRADING CONFIGURATION SUMMARY")
    print("=" * 50)
    print(f"Default Instrument: {DEFAULT_INSTRUMENT}")
    print(f"Default Period: {TRADING_PARAMS['default_period']}")
    print(f"Default Interval: {TRADING_PARAMS['default_interval']}")
    print(f"SuperTrend Period: {SUPERTREND_CONFIG['default_period']}")
    print(f"SuperTrend Multiplier: {SUPERTREND_CONFIG['default_multiplier']}")
    
    print(f"\nAvailable Instruments:")
    for inst_type, instruments in INSTRUMENTS.items():
        print(f"  {inst_type.upper()}: {len(instruments)} instruments")
        for name, data in instruments.items():
            print(f"    {name}: {data['symbol']}")
    
    print("=" * 50)

if __name__ == "__main__":
    print_config_summary()
