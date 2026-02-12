# ============================================================================
# binomial_model/binomial_model_plotter.py
# ============================================================================
import matplotlib.pyplot as plt
from .binomial_model_parameter import BinomialParameter


class BinomialPlotter:
    
    def __init__(self, S0, params: BinomialParameter):
        self.S0 = S0
        self.params = params
    
    def plot_tree(self, figsize=(12, 8), title=None, save_path=None, show=True):
        """
        Visualize the binomial tree - FIXED VERSION.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        title : str, optional
            Custom title for the plot
        show : bool
            Whether to display the plot (default True)
        save_path : str, optional
            Path to save the figure
        """
        # Clear any existing figures to prevent jam
        plt.close('all')
        
        M, U, D = self.params.M, self.params.U, self.params.D
        S0 = self.S0
        tree = []
        
        # Build the tree structure
        for i in range(M + 1):
            nodes = [(S0 * (U ** j) * (D ** (i - j))) for j in range(i + 1)]
            tree.append(nodes)
        
        # Create new figure
        fig, ax = plt.subplots(figsize=figsize)
        
        # Draw branches between nodes
        for i in range(M):
            for j in range(i + 1):
                x, y = i, tree[i][j]
                ax.plot([x, x + 1], [y, tree[i + 1][j + 1]], color='black', lw=1)
                ax.plot([x, x + 1], [y, tree[i + 1][j]], color='black', lw=1)
        
        # Plot nodes and annotate with price
        for i in range(M + 1):
            for j in range(i + 1):
                x, y = i, tree[i][j]
                ax.scatter(x, y, color='blue', s=50, zorder=5)
                ax.text(x, y, f'{y:.2f}', fontsize=9, ha='right', va='bottom')
        
        # Beautify plot
        plot_title = title or 'Binomial Tree for Stock Price Evolution'
        ax.set_title(plot_title, fontsize=16)
        ax.set_xlabel('Time Step', fontsize=12)
        ax.set_ylabel('Stock Price', fontsize=12)
        for spine in ["top", "right", "left"]:
            ax.spines[spine].set_visible(False)
        ax.set_yticks([])
        ax.set_yticklabels([])
        
        # Handle saving
        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Figure saved to: {save_path}")
        
        # Handle display
        if show:
            plt.tight_layout()
            plt.show()
        
        # Return the result (fig, ax) if show=False, otherwise None
        return (fig, ax) if not show else None