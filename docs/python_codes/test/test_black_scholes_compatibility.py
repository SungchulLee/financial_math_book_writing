#!/usr/bin/env python3
# ============================================================================
# test_black_scholes_compatibility.py
# ============================================================================
"""
Comprehensive compatibility test runner for the updated Black-Scholes package.

This script automatically finds and runs all Python files starting with 
"black_scholes" to verify backward compatibility of the updated package.
"""

import os
import sys
import subprocess
import glob
import time
from pathlib import Path
import traceback

# Add parent directory to Python path to find black_scholes module
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

def find_black_scholes_scripts(directory=None):
    """
    Find all Python scripts starting with 'black_scholes' in the given directory.
    
    Parameters:
    -----------
    directory : str
        Directory to search in (default: parent directory of test script)
    
    Returns:
    --------
    list
        List of found Python script paths
    """
    if directory is None:
        # Default to parent directory (one level up from test folder)
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    pattern = os.path.join(directory, "black_scholes*.py")
    scripts = glob.glob(pattern)
    
    # Sort for consistent execution order
    scripts.sort()
    
    # Filter out __pycache__ and other non-script files
    valid_scripts = []
    for script in scripts:
        # Skip files in __pycache__ or other directories
        if "__pycache__" not in script and os.path.isfile(script):
            valid_scripts.append(script)
    
    return valid_scripts

def run_script(script_path, timeout=60):
    """
    Run a single Python script and capture its output.
    
    Parameters:
    -----------
    script_path : str
        Path to the Python script
    timeout : int
        Timeout in seconds (default: 60)
    
    Returns:
    --------
    dict
        Results dictionary with success status, output, and timing
    """
    script_name = os.path.basename(script_path)
    script_dir = os.path.dirname(script_path)
    
    print(f"  Running: {script_name}")
    
    start_time = time.time()
    
    try:
        # Set up environment to ensure the script can find the black_scholes module
        env = os.environ.copy()
        current_pythonpath = env.get('PYTHONPATH', '')
        
        # Add the script's directory and parent directory to PYTHONPATH
        additional_paths = [script_dir]
        if script_dir != parent_dir:
            additional_paths.append(parent_dir)
        
        if current_pythonpath:
            env['PYTHONPATH'] = os.pathsep.join(additional_paths + [current_pythonpath])
        else:
            env['PYTHONPATH'] = os.pathsep.join(additional_paths)
        
        # Run the script with timeout
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=script_dir,
            env=env
        )
        
        execution_time = time.time() - start_time
        
        return {
            'script': script_name,
            'success': result.returncode == 0,
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'execution_time': execution_time,
            'timeout': False
        }
        
    except subprocess.TimeoutExpired:
        execution_time = time.time() - start_time
        return {
            'script': script_name,
            'success': False,
            'returncode': -1,
            'stdout': '',
            'stderr': f'Script timed out after {timeout} seconds',
            'execution_time': execution_time,
            'timeout': True
        }
        
    except Exception as e:
        execution_time = time.time() - start_time
        return {
            'script': script_name,
            'success': False,
            'returncode': -1,
            'stdout': '',
            'stderr': f'Exception running script: {str(e)}',
            'execution_time': execution_time,
            'timeout': False
        }

def print_separator(title, char="=", width=80):
    """Print a formatted separator with title"""
    padding = (width - len(title) - 2) // 2
    print(char * padding + f" {title} " + char * padding)

def print_results_summary(results):
    """
    Print a comprehensive summary of test results.
    
    Parameters:
    -----------
    results : list
        List of result dictionaries from run_script
    """
    total_scripts = len(results)
    successful_scripts = sum(1 for r in results if r['success'])
    failed_scripts = total_scripts - successful_scripts
    total_time = sum(r['execution_time'] for r in results)
    
    print_separator("COMPATIBILITY TEST RESULTS SUMMARY")
    print(f"Total Scripts Found:    {total_scripts}")
    print(f"Successful Runs:        {successful_scripts}")
    print(f"Failed Runs:            {failed_scripts}")
    print(f"Success Rate:           {successful_scripts/total_scripts*100:.1f}%")
    print(f"Total Execution Time:   {total_time:.2f} seconds")
    print()
    
    # Detailed results
    if successful_scripts > 0:
        print_separator("✅ SUCCESSFUL SCRIPTS", "=", 60)
        for result in results:
            if result['success']:
                print(f"  ✅ {result['script']:<35} ({result['execution_time']:.2f}s)")
        print()
    
    if failed_scripts > 0:
        print_separator("❌ FAILED SCRIPTS", "=", 60)
        for result in results:
            if not result['success']:
                status = "TIMEOUT" if result['timeout'] else f"EXIT CODE {result['returncode']}"
                print(f"  ❌ {result['script']:<35} ({status}) ({result['execution_time']:.2f}s)")
        print()
    
    # Performance summary
    if results:
        print_separator("⏱️ PERFORMANCE SUMMARY", "=", 60)
        fastest = min(results, key=lambda x: x['execution_time'])
        slowest = max(results, key=lambda x: x['execution_time'])
        avg_time = total_time / total_scripts
        
        print(f"  Fastest: {fastest['script']:<25} {fastest['execution_time']:.2f}s")
        print(f"  Slowest: {slowest['script']:<25} {slowest['execution_time']:.2f}s")
        print(f"  Average: {avg_time:.2f}s")
        print()

def print_error_details(results):
    """
    Print detailed error information for failed scripts.
    
    Parameters:
    -----------
    results : list
        List of result dictionaries from run_script
    """
    failed_results = [r for r in results if not r['success']]
    
    if not failed_results:
        return
    
    print_separator("🔍 DETAILED ERROR ANALYSIS")
    
    for result in failed_results:
        print(f"\n📄 SCRIPT: {result['script']}")
        print(f"   Return Code: {result['returncode']}")
        print(f"   Execution Time: {result['execution_time']:.2f}s")
        
        if result['stderr']:
            print("   STDERR:")
            # Print first few lines of stderr to avoid too much output
            stderr_lines = result['stderr'].strip().split('\n')
            for line in stderr_lines[:10]:  # Show first 10 lines
                print(f"     {line}")
            if len(stderr_lines) > 10:
                print(f"     ... ({len(stderr_lines) - 10} more lines)")
        
        if result['stdout']:
            print("   STDOUT (last few lines):")
            stdout_lines = result['stdout'].strip().split('\n')
            for line in stdout_lines[-5:]:  # Show last 5 lines
                print(f"     {line}")
        
        print("-" * 60)

def check_package_import():
    """
    Test if the black_scholes package can be imported successfully.
    
    Returns:
    --------
    bool
        True if package imports successfully, False otherwise
    """
    try:
        # Try to import the black_scholes module
        import black_scholes as bs
        
        print("✅ Package import test: SUCCESS")
        print(f"   Package version: {getattr(bs, '__version__', 'Unknown')}")
        print(f"   Package location: {bs.__file__}")
        
        # Test basic imports - be more flexible about what's available
        success_count = 0
        total_imports = 0
        
        # Try individual imports and count successes
        import_tests = [
            ('BlackScholes', 'from black_scholes import BlackScholes'),
            ('BlackScholesFormula', 'from black_scholes import BlackScholesFormula'),
            ('BlackScholesGreeks', 'from black_scholes import BlackScholesGreeks'),
            ('BlackScholesMonteCarlo', 'from black_scholes import BlackScholesMonteCarlo'),
            ('BlackScholesNumericalSolver', 'from black_scholes import BlackScholesNumericalSolver'),
            ('BlackScholesImpliedVol', 'from black_scholes import BlackScholesImpliedVol'),
            ('bs_call_price', 'from black_scholes import bs_call_price'),
            ('bs_put_price', 'from black_scholes import bs_put_price'),
            ('delta', 'from black_scholes import delta'),
            ('gamma', 'from black_scholes import gamma'),
            ('vega', 'from black_scholes import vega')
        ]
        
        available_classes = []
        for name, import_stmt in import_tests:
            total_imports += 1
            try:
                exec(import_stmt)
                success_count += 1
                available_classes.append(name)
            except ImportError:
                pass
        
        print(f"   Available imports: {success_count}/{total_imports}")
        print(f"   Available classes: {', '.join(available_classes[:5])}{'...' if len(available_classes) > 5 else ''}")
        
        # Try to test basic functionality if BlackScholes is available
        if 'BlackScholes' in available_classes:
            try:
                from black_scholes import BlackScholes
                test_bs = BlackScholes(S0=100, K=105, T=0.25, r=0.05, sigma=0.2)
                call_price, put_price = test_bs.price_analytical()
                print(f"   Basic functionality test: SUCCESS")
                print(f"   Sample call price: {call_price:.4f}")
            except Exception as e:
                print(f"   Basic functionality test: FAILED ({e})")
        
        return True
        
    except Exception as e:
        print("❌ Package import test: FAILED")
        print(f"   Error: {str(e)}")
        print(f"   Python path includes: {parent_dir}")
        
        # Check if there are any .py files that might be the module
        possible_files = glob.glob(os.path.join(parent_dir, "black_scholes*.py"))
        if possible_files:
            print(f"   Found potential module files:")
            for f in possible_files[:3]:  # Show first 3
                print(f"     {os.path.basename(f)}")
        
        return False

def main():
    """Main test runner function"""
    print_separator("BLACK-SCHOLES PACKAGE COMPATIBILITY TEST RUNNER")
    
    # Show directory information
    current_dir = os.getcwd()
    test_script_dir = os.path.dirname(os.path.abspath(__file__))
    search_dir = parent_dir
    
    print(f"Test script location: {test_script_dir}")
    print(f"Searching for scripts in: {search_dir}")
    print(f"Python path includes: {parent_dir}")
    
    # Test package import first
    print_separator("📦 PACKAGE IMPORT TEST")
    if not check_package_import():
        print("\n❌ Package import failed. Cannot proceed with script testing.")
        print("Please ensure the black_scholes package is properly installed/available.")
        print(f"Expected location: {parent_dir}")
        return False
    
    print()
    
    # Find all black_scholes scripts
    print_separator("🔍 SCRIPT DISCOVERY")
    scripts = find_black_scholes_scripts(search_dir)
    
    if not scripts:
        print(f"❌ No Python scripts starting with 'black_scholes' found in {search_dir}")
        print("Please ensure you're running this script from the correct directory.")
        
        # Show what files are available for debugging
        all_py_files = glob.glob(os.path.join(search_dir, "*.py"))
        if all_py_files:
            print(f"\nAvailable .py files in {search_dir}:")
            for f in all_py_files[:10]:  # Show first 10
                print(f"  {os.path.basename(f)}")
            if len(all_py_files) > 10:
                print(f"  ... and {len(all_py_files) - 10} more")
        
        return False
    
    print(f"Found {len(scripts)} script(s):")
    for i, script in enumerate(scripts, 1):
        print(f"  {i}. {os.path.basename(script)}")
    
    print()
    
    # Run all scripts
    print_separator("🚀 RUNNING COMPATIBILITY TESTS")
    results = []
    
    for i, script in enumerate(scripts, 1):
        print(f"[{i}/{len(scripts)}] Testing: {os.path.basename(script)}")
        result = run_script(script, timeout=120)  # 2 minute timeout
        results.append(result)
        
        if result['success']:
            print(f"  ✅ SUCCESS ({result['execution_time']:.2f}s)")
        else:
            status = "TIMEOUT" if result['timeout'] else f"FAILED (code {result['returncode']})"
            print(f"  ❌ {status} ({result['execution_time']:.2f}s)")
        print()
    
    # Print comprehensive results
    print_results_summary(results)
    
    # Print error details if any failures
    failed_count = sum(1 for r in results if not r['success'])
    if failed_count > 0:
        print_error_details(results)
        
        print_separator("🔧 TROUBLESHOOTING SUGGESTIONS")
        print("If scripts are failing, check for:")
        print("  • Import errors - ensure all required packages are installed")
        print("  • API changes - verify method signatures match expectations")
        print("  • Path issues - ensure scripts can find the black_scholes package")
        print("  • Missing dependencies - matplotlib, numpy, scipy, pandas")
        print("  • File permissions - ensure scripts are readable/executable")
        print("  • Interactive input - some scripts may require user input")
        print()
    
    # Final verdict
    success_rate = (len(scripts) - failed_count) / len(scripts) * 100
    
    print_separator("🏁 FINAL COMPATIBILITY VERDICT")
    if success_rate == 100:
        print("🎉 PERFECT COMPATIBILITY: All scripts ran successfully!")
        print("The updated black_scholes package is fully backward compatible.")
    elif success_rate >= 90:
        print("✅ EXCELLENT COMPATIBILITY: Most scripts ran successfully!")
        print(f"Success rate: {success_rate:.1f}% - Minor issues may need attention.")
    elif success_rate >= 75:
        print("⚠️  GOOD COMPATIBILITY: Majority of scripts ran successfully.")
        print(f"Success rate: {success_rate:.1f}% - Some compatibility issues exist.")
    elif success_rate >= 50:
        print("🔶 MODERATE COMPATIBILITY: Significant compatibility issues detected.")
        print(f"Success rate: {success_rate:.1f}% - Review and fix needed.")
    else:
        print("❌ POOR COMPATIBILITY: Major compatibility issues detected.")
        print(f"Success rate: {success_rate:.1f}% - Substantial changes needed.")
    
    print("="*80)
    
    return success_rate == 100

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user (Ctrl+C)")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ Unexpected error in test runner: {str(e)}")
        traceback.print_exc()
        sys.exit(1)

# ============================================================================
# ADDITIONAL UTILITY FUNCTIONS
# ============================================================================

def run_single_script_test(script_name):
    """
    Run a single script test (utility function for debugging).
    
    Parameters:
    -----------
    script_name : str
        Name of the script to test
    
    Usage:
    ------
    python test_black_scholes_compatibility.py --single black_scholes_EXAMPLE.py
    """
    # Look for script in parent directory if not found in current
    if not os.path.exists(script_name):
        parent_script = os.path.join(parent_dir, script_name)
        if os.path.exists(parent_script):
            script_name = parent_script
        else:
            print(f"❌ Script not found: {script_name}")
            print(f"Also checked: {parent_script}")
            return False
    
    print(f"Testing single script: {script_name}")
    result = run_script(script_name)
    
    if result['success']:
        print(f"✅ SUCCESS: {script_name}")
        if result['stdout']:
            print("Output:")
            print(result['stdout'])
    else:
        print(f"❌ FAILED: {script_name}")
        if result['stderr']:
            print("Error output:")
            print(result['stderr'])
    
    return result['success']

# Command line interface for single script testing
if __name__ == "__main__" and len(sys.argv) > 1:
    if sys.argv[1] == "--single" and len(sys.argv) > 2:
        script_name = sys.argv[2]
        success = run_single_script_test(script_name)
        sys.exit(0 if success else 1)