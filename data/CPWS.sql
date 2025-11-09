sql_query = """
    SELECT ref.[Region] AS [region]
    , SUM(cpws.[All-PHARMACISTS_FTE]) AS [baseline_pharmacists]
    , SUM(cpws.[ALL-Pharmacy Technicians_FTE]) + SUM(cpws.[Accuracy-checkers_FTE]) AS [baseline_technicians]
    FROM
        [Pharmacy].[dbo].[Community_Pharmacy] AS cpws
    JOIN
        [Pharmacy].[dbo].[mapping pharmacy_ICB] AS ref ON cpws.[ICB_Name] = ref.[ICB]
    WHERE
        cpws.[Year] = 2024
    GROUP BY
        ref.[Region];
"""
