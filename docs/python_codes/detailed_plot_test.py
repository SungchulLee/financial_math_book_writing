#!/usr/bin/env python3
"""
Test what the plotting methods actually return
"""

print("🔍 DETAILED PLOTTING TEST")
print("=" * 50)

import black_scholes_v_1_1_0 as bs
import pandas as pd
import numpy as np

# Create model and add some data
model = bs.BlackScholesImpliedVol(S0=17.6639, K=18.0, T=0.25, r=0.01, sigma=0.2, tol=0.5)

# Create minimal test data
print("📊 Creating test data...")
model.options_data = pd.DataFrame({
    'STRIKE': [15, 16, 17, 18, 19, 20],
    'TTM': [0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
    'MATURITY': [pd.Timestamp('2024-04-01')] * 6,
    'PRICE': [3.5, 2.8, 2.2, 1.8, 1.5, 1.3],
    'DATE': [pd.Timestamp('2024-01-01')] * 6,
    'IMP_VOL': [0.8, 0.75, 0.7, 0.72, 0.76, 0.8]
})

model.futures_data = pd.DataFrame({
    'MATURITY': [pd.Timestamp('2024-04-01')],
    'PRICE': [17.6639],
    'DATE': [pd.Timestamp('2024-01-01')]
})

print("✅ Test data created")

# Test each plotting method
print("\n🎨 Testing plotting methods...")

# Test 1: plot_volatility_smiles
print("\n1️⃣ Testing plot_volatility_smiles:")
try:
    result = model.plot_volatility_smiles()
    print(f"   Result type: {type(result)}")
    print(f"   Result value: {result}")
    
    if result == (None, None):
        print("   ❌ Method returned (None, None) - this is a stub!")
    elif result[0] is not None:
        print("   ✅ Method returned actual figure!")
        print(f"   Figure type: {type(result[0])}")
    else:
        print("   ⚠️  Method returned something unexpected")
        
except Exception as e:
    print(f"   ❌ Method failed: {e}")

# Test 2: plot_3d_surface
print("\n2️⃣ Testing plot_3d_surface:")
try:
    result = model.plot_3d_surface()
    print(f"   Result type: {type(result)}")
    print(f"   Result value: {result}")
    
    if result == (None, None):
        print("   ❌ Method returned (None, None) - this is a stub!")
    elif result[0] is not None:
        print("   ✅ Method returned actual figure!")
        print(f"   Figure type: {type(result[0])}")
    else:
        print("   ⚠️  Method returned something unexpected")
        
except Exception as e:
    print(f"   ❌ Method failed: {e}")

# Test 3: plot_3d_smiles
print("\n3️⃣ Testing plot_3d_smiles:")
try:
    result = model.plot_3d_smiles()
    print(f"   Result type: {type(result)}")
    print(f"   Result value: {result}")
    
    if result == (None, None):
        print("   ❌ Method returned (None, None) - this is a stub!")
    elif result[0] is not None:
        print("   ✅ Method returned actual figure!")
        print(f"   Figure type: {type(result[0])}")
    else:
        print("   ⚠️  Method returned something unexpected")
        
except Exception as e:
    print(f"   ❌ Method failed: {e}")

# Test 4: Check method source
print("\n🔍 Checking method implementation:")
import inspect

try:
    source = inspect.getsource(model.plot_volatility_smiles)
    if "preserved for compatibility" in source or "returns empty" in source:
        print("   ❌ plot_volatility_smiles is a compatibility stub")
    elif "return None, None" in source:
        print("   ❌ plot_volatility_smiles explicitly returns None")
    else:
        print("   ✅ plot_volatility_smiles has real implementation")
        
    # Show first few lines
    lines = source.split('\n')[:5]
    print("   Method starts with:")
    for line in lines:
        print(f"     {line}")
        
except Exception as e:
    print(f"   ❌ Could not inspect source: {e}")

print("\n" + "=" * 50)
print("🏁 DETAILED TEST COMPLETED")

# Recommendation
print("\n💡 RECOMMENDATION:")
print("If methods return (None, None), your v1.1.0 still has stub implementations.")
print("Use the quick fix approach:")
print("1. Save the working code as 'black_scholes_v_1_1_0_FIXED.py'")
print("2. Change import to: import black_scholes_v_1_1_0_FIXED as bs")
print("3. Run your script again")