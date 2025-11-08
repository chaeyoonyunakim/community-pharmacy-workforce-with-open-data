"""
Utility functions for project setup and file paths.

Provides helper functions for managing data directories and project paths,
and financial year conversions.
"""

from pathlib import Path


def get_data_dir(data_dir=None):
    """
    Get the data directory path.
    
    If data_dir is None, automatically determines the data directory
    relative to the project root (assumes src/ is a subdirectory of project root).
    
    Args:
        data_dir: Optional custom data directory path. If None, uses default project structure.
    
    Returns:
        Path: Path object pointing to the data directory.
    """
    if data_dir is None:
        # Get the project root directory (parent of src/)
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        data_dir = project_root / 'data'
    else:
        data_dir = Path(data_dir)
    
    return data_dir


def get_project_root():
    """
    Get the project root directory path.
    
    Assumes src/ is a subdirectory of the project root.
    
    Returns:
        Path: Path object pointing to the project root directory.
    """
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    return project_root


def calendar_to_financial_year(calendar_year):
    """
    Convert calendar year to UK financial year format (e.g., 2025 -> '2025/26').
    
    UK financial year runs from April to March.
    Financial year 2025/26 = April 2025 to March 2026.
    
    Args:
        calendar_year: Calendar year (int)
    
    Returns:
        str: Financial year in format 'YYYY/YY'
    """
    next_year_short = str(calendar_year + 1)[-2:]
    return f"{calendar_year}/{next_year_short}"


def add_financial_year_column(df):
    """
    Add financial year column to dataframe based on calendar year.
    
    Args:
        df: DataFrame with 'year' column
    
    Returns:
        DataFrame: DataFrame with added 'financial_year' column
    """
    df = df.copy()
    df['financial_year'] = df['year'].apply(calendar_to_financial_year)
    return df

