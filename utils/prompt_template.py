def generate_review_prompt(code, language):
    return f"""
You are a senior software engineer.

Review the following {language} code and provide:

1. Bugs or logical errors
2. Code improvement suggestions
3. Optimization tips
4. Time and space complexity
5. Refactored version
6. Code quality score out of 10

Code:
{code}

Provide output in clean markdown format.
"""
