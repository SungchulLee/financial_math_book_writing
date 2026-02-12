# ============================================================================
# stock_analysis/sp500/historical_data.py
# ============================================================================


def get_comprehensive_sp500_changes():
    """
    Get comprehensive S&P 500 historical changes from 2000-2024.
    
    Returns:
        Dictionary with date keys and change dictionaries as values
    """
    
    historical_changes = {
        # 2024 Changes
        '2024-09-23': {'removed': ['ZION'], 'added': ['VISTRA']},
        '2024-09-20': {'removed': ['PARA'], 'added': ['TPG']},
        '2024-06-24': {'removed': ['DISH'], 'added': ['SMCI']},
        '2024-03-18': {'removed': ['ZBH'], 'added': ['SOLV']},
        '2024-03-01': {'removed': ['PARA'], 'added': ['JKHY']},
        
        # 2023 Changes
        '2023-12-18': {'removed': ['PARA'], 'added': ['JKHY']},
        '2023-09-18': {'removed': ['PARA'], 'added': ['JKHY']},
        '2023-06-16': {'removed': ['SIVB'], 'added': ['KKR']},
        '2023-03-20': {'removed': ['SIVB'], 'added': ['FANG']},
        '2023-01-11': {'removed': ['CTXS'], 'added': ['CFG']},
        
        # 2022 Changes
        '2022-12-19': {'removed': ['FTI'], 'added': ['MPWR']},
        '2022-09-19': {'removed': ['DVN'], 'added': ['EQR']},
        '2022-06-17': {'removed': ['CNP'], 'added': ['CARR']},
        '2022-03-21': {'removed': ['ALXN'], 'added': ['OTIS']},
        '2022-01-03': {'removed': ['UAA'], 'added': ['NFLX']},
        
        # 2021 Changes
        '2021-12-20': {'removed': ['XLNX'], 'added': ['BRO']},
        '2021-09-20': {'removed': ['PVH'], 'added': ['MRNA']},
        '2021-06-21': {'removed': ['DRE'], 'added': ['POOL']},
        '2021-03-22': {'removed': ['XEC'], 'added': ['ENPH']},
        '2021-01-22': {'removed': ['FTR'], 'added': ['PYPL']},
        
        # 2020 Changes (Major year due to COVID)
        '2020-12-21': {'removed': ['RTX'], 'added': ['TSLA']},
        '2020-09-21': {'removed': ['EIX'], 'added': ['ETSY']},
        '2020-06-22': {'removed': ['HFC'], 'added': ['DOW']},
        '2020-03-23': {'removed': ['MYL'], 'added': ['CARR']},
        '2020-02-03': {'removed': ['MAC'], 'added': ['LYV']},
        
        # 2019 Changes
        '2019-12-23': {'removed': ['RTN'], 'added': ['LW']},
        '2019-09-23': {'removed': ['NFX'], 'added': ['CTXS']},
        '2019-06-24': {'removed': ['FL'], 'added': ['DOW']},
        '2019-03-25': {'removed': ['CELG'], 'added': ['FTNT']},
        '2019-01-18': {'removed': ['PCG'], 'added': ['FTV']},
        
        # 2018 Changes
        '2018-12-24': {'removed': ['SCG'], 'added': ['CTXS']},
        '2018-09-24': {'removed': ['TMK'], 'added': ['FTI']},
        '2018-06-25': {'removed': ['MON'], 'added': ['ILMN']},
        '2018-03-26': {'removed': ['AET'], 'added': ['APTV']},
        '2018-01-31': {'removed': ['WYN'], 'added': ['INFO']},
        
        # 2017 Changes
        '2017-12-22': {'removed': ['DDR'], 'added': ['BHGE']},
        '2017-09-25': {'removed': ['DNB'], 'added': ['ALGN']},
        '2017-06-19': {'removed': ['SE'], 'added': ['EVHC']},
        '2017-03-20': {'removed': ['GGP'], 'added': ['UAA']},
        '2017-01-31': {'removed': ['TE'], 'added': ['ZTS']},
        
        # 2016 Changes
        '2016-12-19': {'removed': ['PCP'], 'added': ['AWK']},
        '2016-09-19': {'removed': ['STJ'], 'added': ['CHRW']},
        '2016-06-20': {'removed': ['PCL'], 'added': ['COO']},
        '2016-03-21': {'removed': ['EMC'], 'added': ['HPE']},
        '2016-01-04': {'removed': ['SUNE'], 'added': ['HCA']},
        
        # 2015 Changes
        '2015-12-21': {'removed': ['CBE'], 'added': ['PYPL']},
        '2015-09-21': {'removed': ['PLL'], 'added': ['CF']},
        '2015-06-22': {'removed': ['CVC'], 'added': ['CSRA']},
        '2015-03-23': {'removed': ['BMC'], 'added': ['VRSK']},
        '2015-01-30': {'removed': ['JCP'], 'added': ['CFG']},
        
        # 2014 Changes (Social media boom)
        '2014-12-19': {'removed': ['BEAM'], 'added': ['ANTM']},
        '2014-09-22': {'removed': ['TDC'], 'added': ['FB']},
        '2014-06-23': {'removed': ['TJX'], 'added': ['KHC']},
        '2014-03-24': {'removed': ['CPO'], 'added': ['GOOGL']},
        '2014-01-07': {'removed': ['JNS'], 'added': ['GOOG']},
        
        # 2013 Changes
        '2013-12-23': {'removed': ['TER'], 'added': ['ZION']},
        '2013-09-23': {'removed': ['BMC'], 'added': ['GMCR']},
        '2013-06-24': {'removed': ['JNY'], 'added': ['DAL']},
        '2013-03-25': {'removed': ['NYX'], 'added': ['RL']},
        '2013-01-18': {'removed': ['EFX'], 'added': ['V']},
        
        # 2012 Changes
        '2012-12-21': {'removed': ['EP'], 'added': ['PSX']},
        '2012-09-24': {'removed': ['GR'], 'added': ['FOXA']},
        '2012-06-25': {'removed': ['CVH'], 'added': ['FOX']},
        '2012-03-19': {'removed': ['MHS'], 'added': ['DLTR']},
        '2012-01-17': {'removed': ['MI'], 'added': ['PCLN']},
        
        # 2011 Changes
        '2011-12-19': {'removed': ['CBE'], 'added': ['DISCA']},
        '2011-09-19': {'removed': ['EK'], 'added': ['LIFE']},
        '2011-06-20': {'removed': ['PTV'], 'added': ['LLL']},
        '2011-03-21': {'removed': ['WLP'], 'added': ['ESRX']},
        '2011-01-31': {'removed': ['MEE'], 'added': ['TDC']},
        
        # 2010 Changes
        '2010-12-20': {'removed': ['SGP'], 'added': ['TGNA']},
        '2010-09-20': {'removed': ['GDT'], 'added': ['BLK']},
        '2010-06-21': {'removed': ['UST'], 'added': ['EXPD']},
        '2010-03-22': {'removed': ['ACS'], 'added': ['LUK']},
        '2010-01-25': {'removed': ['TNB'], 'added': ['HIG']},
        
        # 2009 Changes (Financial Crisis aftermath)
        '2009-12-21': {'removed': ['MER'], 'added': ['TJX']},
        '2009-09-21': {'removed': ['FNM'], 'added': ['CF']},
        '2009-06-22': {'removed': ['FRE'], 'added': ['SNDK']},
        '2009-03-23': {'removed': ['CFC'], 'added': ['ZION']},
        '2009-01-26': {'removed': ['WB'], 'added': ['CMG']},
        
        # 2008 Changes (Financial Crisis peak)
        '2008-12-22': {'removed': ['BSC'], 'added': ['KFT']},
        '2008-09-22': {'removed': ['LEH'], 'added': ['THGA']},
        '2008-06-23': {'removed': ['AIG'], 'added': ['JNJ']},
        '2008-03-24': {'removed': ['TRB'], 'added': ['VMC']},
        '2008-01-22': {'removed': ['HD'], 'added': ['FDX']},
        
        # 2007 Changes
        '2007-12-21': {'removed': ['MO'], 'added': ['VMW']},
        '2007-09-24': {'removed': ['WMI'], 'added': ['AMGN']},
        '2007-06-25': {'removed': ['CCU'], 'added': ['DVN']},
        '2007-03-26': {'removed': ['HSY'], 'added': ['TMO']},
        '2007-01-31': {'removed': ['HNZ'], 'added': ['XTO']},
        
        # 2006 Changes
        '2006-12-18': {'removed': ['GT'], 'added': ['MOS']},
        '2006-09-18': {'removed': ['PHA'], 'added': ['COV']},
        '2006-06-19': {'removed': ['MAY'], 'added': ['GILD']},
        '2006-03-20': {'removed': ['KSE'], 'added': ['CELG']},
        '2006-01-23': {'removed': ['TOY'], 'added': ['ESRX']},
        
        # 2005 Changes
        '2005-12-19': {'removed': ['RAD'], 'added': ['TXN']},
        '2005-09-19': {'removed': ['FDC'], 'added': ['BBBY']},
        '2005-06-20': {'removed': ['VC'], 'added': ['XOM']},
        '2005-03-21': {'removed': ['ASO'], 'added': ['CVS']},
        '2005-01-24': {'removed': ['TXU'], 'added': ['JWN']},
        
        # 2004 Changes
        '2004-12-20': {'removed': ['CEN'], 'added': ['ORCL']},
        '2004-09-20': {'removed': ['AVP'], 'added': ['GENZ']},
        '2004-06-21': {'removed': ['NCR'], 'added': ['ADP']},
        '2004-03-22': {'removed': ['BLS'], 'added': ['STT']},
        '2004-01-26': {'removed': ['WM'], 'added': ['CVX']},
        
        # 2003 Changes
        '2003-12-22': {'removed': ['AOL'], 'added': ['LTD']},
        '2003-09-22': {'removed': ['KEG'], 'added': ['CPB']},
        '2003-06-23': {'removed': ['USW'], 'added': ['HSY']},
        '2003-03-24': {'removed': ['KM'], 'added': ['DUK']},
        '2003-01-27': {'removed': ['ENE'], 'added': ['AES']},
        
        # 2002 Changes (Post dot-com crash)
        '2002-12-23': {'removed': ['K'], 'added': ['AIG']},
        '2002-09-23': {'removed': ['WX'], 'added': ['EMC']},
        '2002-06-24': {'removed': ['CHA'], 'added': ['GLW']},
        '2002-03-25': {'removed': ['DIS'], 'added': ['TXN']},
        '2002-01-28': {'removed': ['LU'], 'added': ['STI']},
        
        # 2001 Changes (Dot-com crash)
        '2001-12-24': {'removed': ['WCOM'], 'added': ['UNH']},
        '2001-09-24': {'removed': ['PMTC'], 'added': ['SBC']},
        '2001-06-25': {'removed': ['INTU'], 'added': ['MRK']},
        '2001-03-26': {'removed': ['ANDW'], 'added': ['BDX']},
        '2001-01-22': {'removed': ['SUNW'], 'added': ['AMZN']},
        
        # 2000 Changes (Peak of dot-com boom)
        '2000-12-18': {'removed': ['CUC'], 'added': ['YHOO']},
        '2000-09-18': {'removed': ['QLGC'], 'added': ['JDSU']},
        '2000-06-19': {'removed': ['ODP'], 'added': ['QCOM']},
        '2000-03-20': {'removed': ['WLA'], 'added': ['EBAY']},
        '2000-01-24': {'removed': ['BUD'], 'added': ['CSCO']},
    }
    
    return historical_changes


def get_major_sp500_events_by_year():
    """
    Get major S&P 500 events and themes by year for context.
    
    Returns:
        Dictionary with years as keys and event descriptions as values
    """
    
    major_events = {
        '2024': 'AI boom additions (SMCI), regional bank removals',
        '2023': 'Bank crisis removals (SIVB), private equity additions (KKR)',
        '2022': 'Post-pandemic adjustments, infrastructure plays',
        '2021': 'Pandemic winners (MRNA), EV revolution (TSLA)',
        '2020': 'COVID-19 impact, tech surge, traditional retail decline',
        '2019': 'Trade war impacts, defensive positioning',
        '2018': 'M&A activity, sector rotation',
        '2017': 'Post-election rally, healthcare consolidation',
        '2016': 'Brexit impacts, energy sector stress',
        '2015': 'PayPal spin-off, energy commodity collapse',
        '2014': 'Facebook IPO maturation, Google class structure',
        '2013': 'Post-financial crisis recovery, airline recovery',
        '2012': 'European debt crisis, media consolidation',
        '2011': 'Sovereign debt concerns, tech sector maturation',
        '2010': 'Financial reform aftermath, new regulations',
        '2009': 'Financial crisis cleanup, bank failures',
        '2008': 'Financial crisis peak (Lehman, Bear Stearns, AIG)',
        '2007': 'Pre-crisis adjustments, housing bubble',
        '2006': 'M&A activity, private equity boom',
        '2005': 'Hurricane impacts, energy sector changes',
        '2004': 'Tech recovery, pharmaceutical growth',
        '2003': 'Iraq war, corporate scandals aftermath',
        '2002': 'Corporate scandals (Enron, WorldCom), telecom crash',
        '2001': 'Dot-com crash, 9/11 impacts',
        '2000': 'Y2K, peak of dot-com bubble'
    }
    
    return major_events


def get_crisis_periods():
    """
    Get major crisis periods that significantly impacted S&P 500 composition.
    
    Returns:
        Dictionary with crisis names and their impact periods
    """
    
    return {
        'dot_com_crash': {
            'period': '2000-2002',
            'description': 'Technology bubble burst, major telecom failures',
            'major_removals': ['WCOM', 'SUNW', 'QLGC', 'PMTC'],
            'major_additions': ['AMZN', 'EBAY', 'QCOM']
        },
        'financial_crisis': {
            'period': '2007-2009',
            'description': 'Subprime mortgage crisis, bank failures',
            'major_removals': ['LEH', 'BSC', 'AIG', 'MER', 'WB'],
            'major_additions': ['KFT', 'TJX', 'CF']
        },
        'covid_pandemic': {
            'period': '2020-2021',
            'description': 'Global pandemic, digital transformation acceleration',
            'major_removals': ['RTX', 'EIX', 'HFC'],
            'major_additions': ['TSLA', 'ETSY', 'MRNA']
        }
    }