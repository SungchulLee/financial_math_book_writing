# ============================================================================
# stock_analysis/sp500/analysis.py
# ============================================================================
import pandas as pd
from typing import Dict, List
from datetime import datetime
from .composition import get_sp500_tickers_by_year
from .historical_data import get_comprehensive_sp500_changes, get_major_sp500_events_by_year


def validate_sp500_year_data(year: str) -> Dict[str, any]:
    """
    Validate and provide information about S&P 500 data quality for a given year.
    
    Args:
        year: Year as string
        
    Returns:
        Dictionary with validation information
    """
    year_int = int(year)
    current_year = datetime.now().year
    
    # Determine data quality based on how far back the year is
    if year_int >= current_year - 1:
        quality = 'Excellent'
        confidence = 0.99
        note = 'Current/recent data from official source'
    elif year_int >= 2020:
        quality = 'Very Good'
        confidence = 0.95
        note = 'Recent historical data with comprehensive changes applied'
    elif year_int >= 2010:
        quality = 'Good'
        confidence = 0.85
        note = 'Historical reconstruction with major changes captured'
    elif year_int >= 2005:
        quality = 'Fair'
        confidence = 0.75
        note = 'Historical reconstruction - some minor changes may be missing'
    elif year_int >= 2000:
        quality = 'Limited'
        confidence = 0.65
        note = 'Long-term historical - major events captured, recommend verification'
    else:
        quality = 'Poor'
        confidence = 0.40
        note = 'Insufficient historical data - use professional database'
    
    tickers = get_sp500_tickers_by_year(year, include_index=False)
    
    return {
        'year': year,
        'data_quality': quality,
        'confidence_level': confidence,
        'note': note,
        'ticker_count': len(tickers),
        'expected_range': '500-505 companies',
        'within_expected_range': 495 <= len(tickers) <= 510,
        'recommendation': 'Use with confidence' if confidence >= 0.80 else 'Consider verification for critical analysis',
        'coverage_note': 'Comprehensive changes from 2000-2024 included'
    }


def analyze_sp500_changes_by_decade() -> Dict[str, Dict]:
    """
    Analyze S&P 500 changes by decade for insights.
    
    Returns:
        Dictionary with decade analysis
    """
    
    changes = get_comprehensive_sp500_changes()
    events = get_major_sp500_events_by_year()
    
    # Group by decade
    decades = {
        '2020s': {'years': range(2020, 2025), 'changes': 0, 'themes': []},
        '2010s': {'years': range(2010, 2020), 'changes': 0, 'themes': []},
        '2000s': {'years': range(2000, 2010), 'changes': 0, 'themes': []}
    }
    
    # Count changes per decade
    for date_str in changes.keys():
        year = int(date_str[:4])
        
        if 2020 <= year < 2025:
            decades['2020s']['changes'] += 1
        elif 2010 <= year < 2020:
            decades['2010s']['changes'] += 1
        elif 2000 <= year < 2010:
            decades['2000s']['changes'] += 1
    
    # Add themes
    decades['2020s']['themes'] = ['AI/Tech boom', 'Pandemic impact', 'EV revolution', 'Bank consolidation']
    decades['2010s']['themes'] = ['Post-crisis recovery', 'Tech maturation', 'Social media', 'Healthcare consolidation']
    decades['2000s']['themes'] = ['Dot-com crash', 'Financial crisis', 'Corporate scandals', 'Energy volatility']
    
    # Add statistics
    for decade, info in decades.items():
        info['avg_changes_per_year'] = info['changes'] / len(info['years'])
        info['total_years'] = len(info['years'])
    
    return decades


def get_sp500_composition_quality_by_year(year: int) -> str:
    """
    Assess the quality of historical S&P 500 composition data for a given year.
    
    Args:
        year: Year to assess
        
    Returns:
        Quality assessment string
    """
    
    current_year = datetime.now().year
    
    if year >= current_year - 1:
        return "Excellent - Official current data"
    elif year >= 2020:
        return "Very Good - Major changes well documented"
    elif year >= 2010:
        return "Good - Most significant changes captured"
    elif year >= 2005:
        return "Fair - Major events captured, some gaps possible"
    elif year >= 2000:
        return "Limited - Key changes captured, recommend verification"
    else:
        return "Poor - Insufficient data, use professional database"


def analyze_sp500_volatility_by_year() -> pd.DataFrame:
    """
    Analyze S&P 500 composition volatility by year.
    
    Returns:
        DataFrame with yearly volatility metrics
    """
    
    changes = get_comprehensive_sp500_changes()
    
    # Group changes by year
    yearly_changes = {}
    for date_str, change in changes.items():
        year = int(date_str[:4])
        if year not in yearly_changes:
            yearly_changes[year] = {'added': 0, 'removed': 0}
        
        yearly_changes[year]['added'] += len(change.get('added', []))
        yearly_changes[year]['removed'] += len(change.get('removed', []))
    
    # Create DataFrame
    volatility_data = []
    for year in range(2000, 2025):
        changes_data = yearly_changes.get(year, {'added': 0, 'removed': 0})
        total_changes = changes_data['added'] + changes_data['removed']
        
        volatility_data.append({
            'year': year,
            'companies_added': changes_data['added'],
            'companies_removed': changes_data['removed'],
            'total_changes': total_changes,
            'volatility_score': total_changes / 500.0  # Normalize by typical S&P 500 size
        })
    
    df = pd.DataFrame(volatility_data)
    
    # Add rolling averages
    df['volatility_3yr_avg'] = df['volatility_score'].rolling(window=3).mean()
    df['volatility_5yr_avg'] = df['volatility_score'].rolling(window=5).mean()
    
    return df


def identify_crisis_impact_years() -> Dict[str, Dict]:
    """
    Identify years with unusually high S&P 500 composition changes (crisis periods).
    
    Returns:
        Dictionary with crisis years and their impacts
    """
    
    volatility_df = analyze_sp500_volatility_by_year()
    events = get_major_sp500_events_by_year()
    
    # Define high volatility threshold (above 75th percentile)
    high_volatility_threshold = volatility_df['total_changes'].quantile(0.75)
    
    crisis_years = {}
    for _, row in volatility_df.iterrows():
        year = int(row['year'])
        if row['total_changes'] >= high_volatility_threshold:
            crisis_years[str(year)] = {
                'total_changes': int(row['total_changes']),
                'companies_added': int(row['companies_added']),
                'companies_removed': int(row['companies_removed']),
                'volatility_score': round(row['volatility_score'], 4),
                'context': events.get(str(year), 'Unknown'),
                'severity': 'High' if row['total_changes'] >= 15 else 'Moderate'
            }
    
    return crisis_years


def get_most_stable_periods() -> Dict[str, Dict]:
    """
    Identify the most stable periods in S&P 500 composition.
    
    Returns:
        Dictionary with stable periods and their characteristics
    """
    
    volatility_df = analyze_sp500_volatility_by_year()
    
    # Find periods with low volatility
    low_volatility_threshold = volatility_df['total_changes'].quantile(0.25)
    
    stable_periods = {}
    current_period = []
    
    for _, row in volatility_df.iterrows():
        year = int(row['year'])
        if row['total_changes'] <= low_volatility_threshold:
            current_period.append(year)
        else:
            if len(current_period) >= 2:  # At least 2 consecutive years
                period_name = f"{current_period[0]}-{current_period[-1]}"
                stable_periods[period_name] = {
                    'years': current_period.copy(),
                    'duration': len(current_period),
                    'avg_changes_per_year': volatility_df[volatility_df['year'].isin(current_period)]['total_changes'].mean(),
                    'stability_score': 1 - volatility_df[volatility_df['year'].isin(current_period)]['volatility_score'].mean()
                }
            current_period = []
    
    # Handle the last period if it's stable
    if len(current_period) >= 2:
        period_name = f"{current_period[0]}-{current_period[-1]}"
        stable_periods[period_name] = {
            'years': current_period,
            'duration': len(current_period),
            'avg_changes_per_year': volatility_df[volatility_df['year'].isin(current_period)]['total_changes'].mean(),
            'stability_score': 1 - volatility_df[volatility_df['year'].isin(current_period)]['volatility_score'].mean()
        }
    
    return stable_periods


def generate_sp500_analysis_report(start_year: str, end_year: str) -> Dict[str, any]:
    """
    Generate a comprehensive analysis report for a given period.
    
    Args:
        start_year: Starting year for analysis
        end_year: Ending year for analysis
        
    Returns:
        Dictionary with comprehensive analysis
    """
    
    start_year_int = int(start_year)
    end_year_int = int(end_year)
    
    # Basic composition data
    start_tickers = get_sp500_tickers_by_year(start_year, include_index=False)
    end_tickers = get_sp500_tickers_by_year(end_year, include_index=False)
    
    # Calculate changes
    added = list(set(end_tickers) - set(start_tickers))
    removed = list(set(start_tickers) - set(end_tickers))
    survivors = list(set(start_tickers) & set(end_tickers))
    
    # Get volatility data for the period
    volatility_df = analyze_sp500_volatility_by_year()
    period_volatility = volatility_df[
        (volatility_df['year'] >= start_year_int) & 
        (volatility_df['year'] <= end_year_int)
    ]
    
    # Data quality assessment
    start_quality = validate_sp500_year_data(start_year)
    end_quality = validate_sp500_year_data(end_year)
    
    # Crisis years in period
    crisis_years = identify_crisis_impact_years()
    period_crisis_years = {k: v for k, v in crisis_years.items() 
                          if start_year_int <= int(k) <= end_year_int}
    
    return {
        'analysis_period': f'{start_year} to {end_year}',
        'period_length': end_year_int - start_year_int + 1,
        
        'composition_changes': {
            'start_companies': len(start_tickers),
            'end_companies': len(end_tickers),
            'companies_added': len(added),
            'companies_removed': len(removed),
            'companies_survived': len(survivors),
            'survival_rate': len(survivors) / len(start_tickers) if start_tickers else 0,
            'turnover_rate': (len(added) + len(removed)) / len(start_tickers) if start_tickers else 0
        },
        
        'notable_additions': added[:10],  # Top 10 additions
        'notable_removals': removed[:10],  # Top 10 removals
        
        'volatility_metrics': {
            'avg_changes_per_year': period_volatility['total_changes'].mean(),
            'max_changes_in_year': period_volatility['total_changes'].max(),
            'min_changes_in_year': period_volatility['total_changes'].min(),
            'most_volatile_year': int(period_volatility.loc[period_volatility['total_changes'].idxmax(), 'year']),
            'most_stable_year': int(period_volatility.loc[period_volatility['total_changes'].idxmin(), 'year'])
        },
        
        'crisis_years_in_period': period_crisis_years,
        
        'data_quality': {
            'start_year_quality': start_quality['data_quality'],
            'end_year_quality': end_quality['data_quality'],
            'overall_confidence': min(start_quality['confidence_level'], end_quality['confidence_level']),
            'recommendation': 'Reliable for analysis' if min(start_quality['confidence_level'], end_quality['confidence_level']) >= 0.8 else 'Use with caution'
        }
    }


def demo_sp500_analysis():
    """Demonstrate the S&P 500 analysis functions."""
    
    print("=== S&P 500 Historical Analysis Demo ===\n")
    
    # 1. Decade analysis
    print("1. Changes by decade:")
    decades = analyze_sp500_changes_by_decade()
    for decade, info in decades.items():
        print(f"   {decade}: {info['changes']} total changes ({info['avg_changes_per_year']:.1f}/year)")
        print(f"      Themes: {', '.join(info['themes'])}")
    
    # 2. Crisis years
    print("\n2. High volatility (crisis) years:")
    crisis_years = identify_crisis_impact_years()
    for year, info in list(crisis_years.items())[:5]:  # Show top 5
        print(f"   {year}: {info['total_changes']} changes - {info['context']}")
    
    # 3. Stable periods
    print("\n3. Most stable periods:")
    stable_periods = get_most_stable_periods()
    for period, info in stable_periods.items():
        print(f"   {period}: {info['duration']} years, {info['avg_changes_per_year']:.1f} avg changes/year")
    
    # 4. Sample period analysis
    print("\n4. Sample period analysis (2020-2024):")
    report = generate_sp500_analysis_report('2020', '2024')
    print(f"   Survival rate: {report['composition_changes']['survival_rate']:.1%}")
    print(f"   Average changes/year: {report['volatility_metrics']['avg_changes_per_year']:.1f}")
    print(f"   Data quality: {report['data_quality']['recommendation']}")


if __name__ == "__main__":
    demo_sp500_analysis()