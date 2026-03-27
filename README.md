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
| 3 | [Problem 3](https://projecteuler.net/problem=3) | [solutions/problem_0003.py](solutions/problem_0003.py) | 2026-03-11 | Unsolved |
| 4 | [Problem 4](https://projecteuler.net/problem=4) | [solutions/problem_0004.py](solutions/problem_0004.py) | 2026-03-12 | Unsolved |
| 5 | [Problem 5](https://projecteuler.net/problem=5) | [solutions/problem_0005.py](solutions/problem_0005.py) | 2026-03-13 | Unsolved |
| 6 | [Problem 6](https://projecteuler.net/problem=6) | [solutions/problem_0006.py](solutions/problem_0006.py) | 2026-03-14 | Unsolved |
| 7 | [Problem 7](https://projecteuler.net/problem=7) | [solutions/problem_0007.py](solutions/problem_0007.py) | 2026-03-15 | Unsolved |
| 8 | [Problem 8](https://projecteuler.net/problem=8) | [solutions/problem_0008.py](solutions/problem_0008.py) | 2026-03-16 | Unsolved |
| 9 | [Problem 9](https://projecteuler.net/problem=9) | [solutions/problem_0009.py](solutions/problem_0009.py) | 2026-03-16 | Unsolved |
| 10 | [Problem 10](https://projecteuler.net/problem=10) | [solutions/problem_0010.py](solutions/problem_0010.py) | 2026-03-17 | Unsolved |
| 11 | [Problem 11](https://projecteuler.net/problem=11) | [solutions/problem_0011.py](solutions/problem_0011.py) | 2026-03-18 | Unsolved |
| 12 | [Problem 12](https://projecteuler.net/problem=12) | [solutions/problem_0012.py](solutions/problem_0012.py) | 2026-03-19 | Unsolved |
| 13 | [Problem 13](https://projecteuler.net/problem=13) | [solutions/problem_0013.py](solutions/problem_0013.py) | 2026-03-20 | Unsolved |
| 14 | [Problem 14](https://projecteuler.net/problem=14) | [solutions/problem_0014.py](solutions/problem_0014.py) | 2026-03-21 | Unsolved |
| 15 | [Problem 15](https://projecteuler.net/problem=15) | [solutions/problem_0015.py](solutions/problem_0015.py) | 2026-03-22 | Unsolved |
| 16 | [Problem 16](https://projecteuler.net/problem=16) | [solutions/problem_0016.py](solutions/problem_0016.py) | 2026-03-23 | Unsolved |
| 17 | [Problem 17](https://projecteuler.net/problem=17) | [solutions/problem_0017.py](solutions/problem_0017.py) | 2026-03-24 | Unsolved |
| 18 | [Problem 18](https://projecteuler.net/problem=18) | [solutions/problem_0018.py](solutions/problem_0018.py) | 2026-03-25 | Unsolved |
| 19 | [Problem 19](https://projecteuler.net/problem=19) | [solutions/problem_0019.py](solutions/problem_0019.py) | 2026-03-26 | Unsolved |
| 20 | [Problem 20](https://projecteuler.net/problem=20) | [solutions/problem_0020.py](solutions/problem_0020.py) | 2026-03-27 | Unsolved |
