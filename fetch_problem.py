#!/usr/bin/env python3
"""Fetch a Project Euler problem and create a placeholder solution file."""

import json
import os
import urllib.request
from datetime import datetime, timezone


def get_problem_number():
    """Determine which problem to fetch based on existing solutions."""
    solutions_dir = "solutions"
    if not os.path.exists(solutions_dir):
        return 1

    existing = set()
    for f in os.listdir(solutions_dir):
        if f.startswith("problem_") and f.endswith(".py"):
            try:
                num = int(f.replace("problem_", "").replace(".py", ""))
                existing.add(num)
            except ValueError:
                pass

    # Find the next problem number not yet created
    n = 1
    while n in existing:
        n += 1
    return n


def fetch_euler_problem(number):
    """Fetch problem details from projecteuler.net via the unofficial API."""
    url = f"https://projecteuler.net/minimal={number}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "daily-challenge-bot"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception:
        return None


def create_solution_file(number, problem_text):
    """Create a placeholder Python solution file."""
    os.makedirs("solutions", exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if problem_text:
        # Clean up HTML tags minimally
        import re
        clean_text = re.sub(r"<[^>]+>", " ", problem_text)
        clean_text = re.sub(r"\s+", " ", clean_text).strip()
        # Wrap to ~80 chars for readability
        words = clean_text.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 > 76:
                lines.append(current_line)
                current_line = word
            else:
                current_line = f"{current_line} {word}".strip()
        if current_line:
            lines.append(current_line)
        description = "\n".join(f"# {line}" for line in lines)
    else:
        description = f"# Visit: https://projecteuler.net/problem={number}"

    content = f'''"""
Project Euler - Problem {number}
Date: {date_str}
Link: https://projecteuler.net/problem={number}
"""

# Problem Description:
{description}


def solve():
    """TODO: Implement solution."""
    pass


if __name__ == "__main__":
    result = solve()
    print(f"Answer: {{result}}")
'''

    filepath = f"solutions/problem_{number:04d}.py"
    with open(filepath, "w") as f:
        f.write(content)

    return filepath


def update_readme(number, filepath):
    """Update README.md with the new problem entry."""
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entry = f"| {number} | [Problem {number}](https://projecteuler.net/problem={number}) | [{filepath}]({filepath}) | {date_str} | Unsolved |"

    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()
        # Append to the table
        content = content.rstrip() + "\n" + entry + "\n"
    else:
        content = f"""# Daily Coding Challenge

Solving one [Project Euler](https://projecteuler.net/) problem every day.

## Progress

| # | Problem | Solution | Date | Status |
|---|---------|----------|------|--------|
{entry}
"""

    with open(readme_path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    number = get_problem_number()
    print(f"Fetching Project Euler Problem #{number}...")

    problem_text = fetch_euler_problem(number)
    filepath = create_solution_file(number, problem_text)
    update_readme(number, filepath)

    print(f"Created: {filepath}")
    # Output for GitHub Actions
    gh_output = os.environ.get("GITHUB_OUTPUT", "")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write(f"problem_number={number}\n")
            f.write(f"filepath={filepath}\n")
