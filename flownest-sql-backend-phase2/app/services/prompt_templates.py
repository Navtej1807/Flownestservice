def get_tune_prompt(query: str) -> str:
    return f"Optimize this SQL query and explain the changes:\n\n{query}"

def get_plan_analysis_prompt(query: str) -> str:
    return f"Analyze the following SQL execution plan and provide detailed performance insights:\n\n{query}"

def get_schema_optimization_prompt(schema: str, query: str) -> str:
    return (
        f"Given this database schema:\n\n{schema}\n\n"
        f"Optimize the following query considering indexes, joins, and best practices:\n\n{query}"
    )
