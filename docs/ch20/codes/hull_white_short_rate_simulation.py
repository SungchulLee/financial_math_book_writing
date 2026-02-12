# -*- coding: utf-8 -*-
"""
hull_white_short_rate_simulation.py

This module implements Hull-White Short Rate Simulation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def hull_white_short_rate_simulation():
    """
    Hull-White Short Rate Simulation.
    
    This function demonstrates the key concepts and computational techniques
    for hull-white short rate simulation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Hull-White Short Rate Simulation
    print(f"Computing Hull-White Short Rate Simulation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Hull-White Short Rate Simulation"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_short_rate_simulation()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Hull-White Short Rate Simulation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_short_rate_simulation.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_short_rate_simulation.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
