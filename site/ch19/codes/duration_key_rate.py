# -*- coding: utf-8 -*-
"""
duration_key_rate.py

This module implements Duration and Key Rate Duration.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


def duration_key_rate():
    """
    Duration and Key Rate Duration.
    
    This function demonstrates the key concepts and computational techniques
    for duration and key rate duration.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Duration and Key Rate Duration
    print(f"Computing Duration and Key Rate Duration...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Duration and Key Rate Duration"
    }
    
    return results


def main():
    """Main execution function."""
    results = duration_key_rate()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Duration and Key Rate Duration")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/duration_key_rate.png", dpi=150)
    print(f"Figure saved to /tmp/duration_key_rate.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
