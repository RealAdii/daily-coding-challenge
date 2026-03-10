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
