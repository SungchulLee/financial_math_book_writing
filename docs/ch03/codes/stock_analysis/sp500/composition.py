# ============================================================================
# stock_analysis/sp500/composition.py
# ============================================================================
import pandas as pd
import requests
from typing import List, Dict, Optional
from datetime import datetime
from .historical_data import get_comprehensive_sp500_changes


def get_sp500_tickers_by_year(year: str, include_index: bool = True) -> List[str]:
    """
    Get S&P 500 ticker symbols for a specific year.
    
    Args:
        year: Year as string (e.g., '2023', '2020')
        include_index: Whether to include ^GSPC (S&P 500 index) in results
        
    Returns:
        List of ticker symbols that were in S&P 500 during that year
        
    Example:
        >>> tickers_2023 = get_sp500_tickers_by_year('2023')
        >>> tickers_2020 = get_sp500_tickers_by_year('2020', include_index=False)
    """
    year_int = int(year)
    current_year = datetime.now().year
    
    # Validate year
    if year_int < 1957:  # S&P 500 started in 1957
        raise ValueError("S&P 500 index started in 1957")
    if year_int > current_year:
        raise ValueError(f"Cannot get future data. Current year is {current_year}")
    
    # For recent years (current and last year), use current composition
    if year_int >= current_year - 1:
        tickers = _get_current_sp500_composition()
        if not include_index:
            tickers = [t for t in tickers if t != '^GSPC']
        return tickers
    
    # For historical years, apply known changes
    tickers = _get_historical_sp500_composition(year_int)
    
    if include_index and '^GSPC' not in tickers:
        tickers.append('^GSPC')
    elif not include_index and '^GSPC' in tickers:
        tickers.remove('^GSPC')
    
    return tickers


def _get_current_sp500_composition() -> List[str]:
    """Helper function to get current S&P 500 composition."""
    source_url = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv'
    
    try:
        sp500_df = pd.read_csv(source_url)
        
        # Fix Yahoo Finance incompatible symbols
        sp500_df['Symbol'] = sp500_df['Symbol'].str.replace('.', '-', regex=False)
        
        # Additional known fixes
        symbol_fixes = {
            'BF.B': 'BF-B', 
            'BRK.B': 'BRK-B',
            'BF-B': 'BF-B',  # Already fixed, but ensure consistency
            'BRK-B': 'BRK-B'  # Already fixed, but ensure consistency
        }
        sp500_df['Symbol'] = sp500_df['Symbol'].replace(symbol_fixes)
        
        ticker_list = sp500_df['Symbol'].tolist()
        ticker_list.append('^GSPC')
        
        return ticker_list
        
    except Exception as e:
        raise ConnectionError(f"Failed to fetch current S&P 500 data: {e}")


def _get_historical_sp500_composition(year: int) -> List[str]:
    """
    Helper function to reconstruct historical S&P 500 composition.
    
    This uses comprehensive historical changes to work backwards from current composition.
    """
    
    # Start with current composition
    current_tickers = _get_current_sp500_composition()
    
    # Get comprehensive historical changes
    historical_changes = get_comprehensive_sp500_changes()
    
    # Work backwards from current composition
    reconstructed_tickers = current_tickers.copy()
    target_year_start = f'{year}-01-01'
    
    # Apply changes chronologically backwards
    for change_date in sorted(historical_changes.keys(), reverse=True):
        change_year = int(change_date[:4])
        
        # If this change happened after our target year, reverse it
        if change_year > year:
            change = historical_changes[change_date]
            
            # Remove tickers that were added after target year
            if 'added' in change:
                for ticker in change['added']:
                    if ticker in reconstructed_tickers:
                        reconstructed_tickers.remove(ticker)
            
            # Add back tickers that were removed after target year
            if 'removed' in change:
                for ticker in change['removed']:
                    if ticker not in reconstructed_tickers:
                        reconstructed_tickers.append(ticker)
    
    return reconstructed_tickers


def get_sp500_changes_in_year(year: str) -> Dict[str, List[str]]:
    """
    Get the specific changes that happened to S&P 500 in a given year.
    
    Args:
        year: Year as string (e.g., '2023')
        
    Returns:
        Dictionary with 'added' and 'removed' ticker lists
    """
    year_int = int(year)
    
    # Get composition at start and end of year
    start_tickers = set(get_sp500_tickers_by_year(str(year_int), include_index=False))
    
    if year_int == datetime.now().year:
        # For current year, use current composition
        end_tickers = set(_get_current_sp500_composition())
        end_tickers.discard('^GSPC')  # Remove index
    else:
        # For past years, get next year's composition
        end_tickers = set(get_sp500_tickers_by_year(str(year_int + 1), include_index=False))
    
    added = list(end_tickers - start_tickers)
    removed = list(start_tickers - end_tickers)
    
    return {
        'year': year,
        'added': added,
        'removed': removed,
        'total_changes': len(added) + len(removed)
    }


def get_sp500_composition_on_date(date: str) -> List[str]:
    """
    Get S&P 500 composition as of a specific date.
    
    Args:
        date: Date in YYYY-MM-DD format
        
    Returns:
        List of ticker symbols
    """
    # Extract year from date and use yearly composition
    # This is a simplification - for exact date accuracy, you'd need daily change data
    year = date[:4]
    return get_sp500_tickers_by_year(year, include_index=True)


def compare_sp500_compositions(year1: str, year2: str) -> Dict[str, List[str]]:
    """
    Compare S&P 500 compositions between two years.
    
    Args:
        year1: First year to compare
        year2: Second year to compare
        
    Returns:
        Dictionary with comparison results
    """
    tickers1 = set(get_sp500_tickers_by_year(year1, include_index=False))
    tickers2 = set(get_sp500_tickers_by_year(year2, include_index=False))
    
    added = list(tickers2 - tickers1)
    removed = list(tickers1 - tickers2)
    unchanged = list(tickers1 & tickers2)
    
    return {
        'year1': year1,
        'year2': year2,
        'year1_count': len(tickers1),
        'year2_count': len(tickers2),
        'added_in_year2': added,
        'removed_from_year1': removed,
        'unchanged': unchanged,
        'total_changes': len(added) + len(removed),
        'stability_rate': len(unchanged) / len(tickers1) if tickers1 else 0
    }


def get_sp500_survivors(start_year: str, end_year: str) -> Dict[str, List[str]]:
    """
    Get companies that survived in S&P 500 throughout a period.
    
    Args:
        start_year: Starting year
        end_year: Ending year
        
    Returns:
        Dictionary with survivors and dropouts
    """
    start_tickers = set(get_sp500_tickers_by_year(start_year, include_index=False))
    end_tickers = set(get_sp500_tickers_by_year(end_year, include_index=False))
    
    survivors = list(start_tickers & end_tickers)
    dropouts = list(start_tickers - end_tickers)
    new_additions = list(end_tickers - start_tickers)
    
    return {
        'period': f'{start_year}-{end_year}',
        'survivors': survivors,
        'dropouts': dropouts,
        'new_additions': new_additions,
        'survival_rate': len(survivors) / len(start_tickers) if start_tickers else 0,
        'turnover_rate': (len(dropouts) + len(new_additions)) / len(start_tickers) if start_tickers else 0
    }