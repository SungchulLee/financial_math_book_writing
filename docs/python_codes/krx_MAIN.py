#!/usr/bin/env python3
"""
KRX Korean Market Analysis - Main Script

This script demonstrates Korean stock market analysis using the KRX package.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Try to import with graceful fallback
    from stock_analysis import quick_analysis, KRX_AVAILABLE
    
    if KRX_AVAILABLE:
        from stock_analysis import KOSPI200Analyzer
        print("✅ All KRX components loaded successfully")
    else:
        print("⚠️ KRX components not available")
        print("📦 Installing missing dependencies...")
        
        # Try to install missing dependency
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
        
        print("✅ Dependencies installed. Please restart the script.")
        sys.exit(0)
        
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("📦 Installing missing dependencies...")
    
    # Install required packages
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
        print("✅ Dependencies installed. Please restart the script.")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies. Please install manually:")
        print("   pip install beautifulsoup4")
    
    sys.exit(1)

def main():
    """Main analysis function."""
    print("\n🚀 Starting Korean Market Analysis")
    print("=" * 50)
    
    try:
        # KOSPI200 Analysis
        print("\n📊 KOSPI200 Analysis")
        print("-" * 30)
        
        kospi200 = KOSPI200Analyzer(refresh_data=False)
        
        # Run market overview
        overview_results = kospi200.market_overview(show_summary=True, n_display=10)
        print(f"✅ Market overview completed: {overview_results['total_companies']} companies analyzed")
        
        # Run quality analysis
        quality_results = kospi200.quality_analysis()
        print(f"✅ Quality analysis completed")
        
        # Run comprehensive screening
        screening_results = kospi200.comprehensive_screening()
        print(f"✅ Investment screening completed: {len(screening_results)} screens")
        
        # Generate report
        report = kospi200.generate_kospi200_report(save_path="kospi200_analysis_report.txt")
        print(f"✅ Report generated and saved")
        
        print("\n🎯 Analysis Summary:")
        print(f"• Total KOSPI200 companies: {overview_results.get('total_companies', 'N/A')}")
        print(f"• Blue chip opportunities: {len(screening_results.get('blue_chip_value', []))}")
        print(f"• Growth opportunities: {len(screening_results.get('growth_at_reasonable_price', []))}")
        print(f"• High dividend stocks: {len(screening_results.get('high_dividend', []))}")
        
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        print("💡 Make sure all dependencies are installed correctly")
        return False
    
    print("\n✅ Korean Market Analysis Complete!")
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n📄 Check 'kospi200_analysis_report.txt' for detailed results")
    else:
        print("\n❌ Analysis failed. Please check error messages above.")
        sys.exit(1)