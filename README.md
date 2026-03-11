# Daily Coding Challenge

Solving one [Project Euler](https://projecteuler.net/) problem every day, automatically.

A GitHub Actions workflow runs daily to fetch the next unsolved problem and create a placeholder solution file.

## How it works

1. A cron job triggers the workflow every day at ~9 AM UTC
2. The script finds the next problem number not yet in `solutions/`
3. It fetches the problem description from Project Euler
4. Creates a Python solution template in `solutions/problem_XXXX.py`
5. Commits and pushes automatically

## Progress

| # | Problem | Solution | Date | Status |
|---|---------|----------|------|--------|
| 1 | [Problem 1](https://projecteuler.net/problem=1) | [solutions/problem_0001.py](solutions/problem_0001.py) | 2026-03-10 | Unsolved |
| 2 | [Problem 2](https://projecteuler.net/problem=2) | [solutions/problem_0002.py](solutions/problem_0002.py) | 2026-03-11 | Unsolved |
