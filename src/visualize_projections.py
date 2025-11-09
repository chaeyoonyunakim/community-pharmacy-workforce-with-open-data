"""
Visualize Workforce Projections Module

Provides functions for creating charts for workforce projections based on annual growth rates
calculated from actual registrant data.
"""

import config
from utils import calendar_to_financial_year


def create_visualizations(projections_df, output_dir=None):
    """
    Create visualization charts for projections.
    
    Args:
        projections_df: Dictionary of DataFrames from format_projections() with projections by profession
        output_dir: Optional output directory path. If None, uses project root.
    """
    # Default to project root
    if output_dir is None:
        from pathlib import Path
        output_dir = Path(__file__).parent.parent
    else:
        from pathlib import Path
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Combine all profession dataframes into one
    # Financial year column is already included from format_projections
    df = config.pd.concat(projections_df.values(), ignore_index=True)
    
    # Get unique professions dynamically
    professions = df['profession'].unique()
    num_professions = len(professions)
    
    # Create figure with subplots (one per profession)
    end_year = config.START_PROJECTION_YEAR + config.DURATION
    start_fy = calendar_to_financial_year(config.START_PROJECTION_YEAR)
    end_fy = calendar_to_financial_year(end_year)
    fig, axes = config.plt.subplots(num_professions, 1, figsize=(12, 6 * num_professions))
    if num_professions == 1:
        axes = [axes]  # Make it iterable if only one profession
    fig.suptitle(f'{config.DURATION}-Year Workforce Projection - England ({start_fy} to {end_fy})', 
                 fontsize=16, fontweight='bold')
    
    scenarios = ['baseline', 'optimistic', 'pessimistic']
    colors = {'baseline': '#1f77b4', 'optimistic': '#2ca02c', 'pessimistic': '#d62728'}
    
    # Plot each profession
    for idx, profession in enumerate(professions):
        ax = axes[idx]
        for scenario in scenarios:
            data = df[(df['profession'] == profession) & (df['scenario'] == scenario)]
            # Use year for plotting position, but financial_year for labels
            ax.plot(data['year'], data['total_registrants'], 
                    marker='o', label=scenario.capitalize(), 
                    color=colors[scenario], linewidth=2, markersize=4)
        
        # Set x-axis labels to financial years
        ax.set_title(f'{profession} Workforce Projection - England', fontsize=12, fontweight='bold')
        ax.set_xlabel('Financial Year')
        ax.set_ylabel('Number of Registrants')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xlim(config.START_PROJECTION_YEAR - 1, end_year + 1)
        
        # Set x-axis ticks and labels to financial years
        tick_positions = range(config.START_PROJECTION_YEAR, end_year + 1)
        tick_labels = [calendar_to_financial_year(year) for year in tick_positions]
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(tick_labels, rotation=45, ha='right')
    
    config.plt.tight_layout()
    
    # Save figure
    output_path = output_dir / 'workforce_projection_chart.png'
    config.plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    config.plt.close('all')

