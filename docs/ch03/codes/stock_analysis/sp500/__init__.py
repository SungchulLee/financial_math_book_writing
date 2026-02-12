# ============================================================================
# stock_analysis/sp500/__init__.py
# ============================================================================
from .historical_data import get_comprehensive_sp500_changes, get_major_sp500_events_by_year
from .composition import (
    get_sp500_tickers_by_year, 
    get_sp500_changes_in_year,
    get_sp500_survivors,
    compare_sp500_compositions,
    get_sp500_composition_on_date
)
from .analysis import (
    validate_sp500_year_data, 
    analyze_sp500_changes_by_decade,
    generate_sp500_analysis_report,
    identify_crisis_impact_years,
    get_most_stable_periods
)

# Import new simplified functions
from .data_downloader import (
    download_sp500,
    load_data_from_csv,
    create_returns_matrix,
    get_summary,
    save_data,
    load_data,
    quick_test
)

# Import deprecated functions for backwards compatibility
from .data_downloader import (
    download_sp500_csv_bulletproof,
    download_sp500_simple,
    download_sp500_data_simple,
    download_sp500_sample,
    quick_test_download,
    download_sp500_batch,
    create_sp500_returns_matrix,
    save_sp500_data,
    load_sp500_data,
    get_sp500_data_summary,
    download_sp500_data  # Main backwards compatibility alias
)

__all__ = [
    # Core functions
    "get_sp500_tickers_by_year",
    "get_sp500_changes_in_year", 
    "validate_sp500_year_data",
    
    # Comparison functions
    "get_sp500_survivors",
    "compare_sp500_compositions",
    "get_sp500_composition_on_date",
    
    # Analysis functions
    "analyze_sp500_changes_by_decade",
    "generate_sp500_analysis_report",
    "identify_crisis_impact_years",
    "get_most_stable_periods",
    
    # NEW SIMPLIFIED DATA DOWNLOAD FUNCTIONS (RECOMMENDED)
    "download_sp500",           # Main download function
    "load_data_from_csv",
    "create_returns_matrix",    # Create returns matrix
    "get_summary",             # Get data summary
    "save_data",               # Save data to pickle
    "load_data",               # Load data from pickle
    "quick_test",              # Quick test download
    
    # DEPRECATED DATA DOWNLOAD FUNCTIONS (use new ones above instead)
    "download_sp500_csv_bulletproof",  # DEPRECATED: use download_sp500(save_csv=True)
    "download_sp500_simple",           # DEPRECATED: use download_sp500()
    "download_sp500_data",             # DEPRECATED: use download_sp500()
    "download_sp500_data_simple",      # DEPRECATED: use download_sp500()
    "download_sp500_sample",           # DEPRECATED: use download_sp500(sample_size=N)
    "quick_test_download",             # DEPRECATED: use quick_test()
    "download_sp500_batch",            # DEPRECATED: use download_sp500()
    "create_sp500_returns_matrix",     # DEPRECATED: use create_returns_matrix()
    "save_sp500_data",                 # DEPRECATED: use save_data()
    "load_sp500_data",                 # DEPRECATED: use load_data()
    "get_sp500_data_summary",          # DEPRECATED: use get_summary()
    
    # Historical data functions
    "get_comprehensive_sp500_changes",
    "get_major_sp500_events_by_year"
]