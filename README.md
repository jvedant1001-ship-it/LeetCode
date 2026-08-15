# LeetCode Solutions

A personal collection of accepted [LeetCode](https://leetcode.com/) solutions, organized by problem number and title.

This repository is maintained as part of my ongoing preparation in **Data Structures & Algorithms**, with a focus on writing clear, efficient, and maintainable solutions.

## Repository Structure

Each problem is stored in its own directory:

```text
LeetCode/
│
├── 0001-two-sum/
│   ├── solution.py
│   └── README.md
│
├── 0020-valid-parenthesis/
│   ├── solution.py
│   └── README.md
│
├── 0021-merge-two-sorted-lists/
│   ├── solution.py
│   └── README.md
│
└── ...
```

Each problem directory may contain:

* `solution.*` — the submitted solution.
* `README.md` — problem-specific information, including difficulty, language, complexity, and the original LeetCode link.

## Languages

Solutions may be written in different programming languages depending on the problem and learning goals.

Currently supported by the automation workflow:

* Python
* C
* C++
* Java
* JavaScript
* TypeScript

Python is currently my primary language for solving problems.

## Solution Format

A typical problem README contains:

```text
# Problem Title

- Problem: #
- Difficulty: Easy / Medium / Hard
- Language: Python
- Solved: YYYY-MM-DD
- Link: LeetCode problem URL

## Complexity

Time: O(...)
Space: O(...)
```

Complexity information is included only when it is known and can be stated accurately.

## Automation

This repository is connected to a personal **LeetCode → GitHub automation system**.

The intended workflow is:

```text
Solve a LeetCode problem
        ↓
Submit solution
        ↓
LeetCode reports Accepted
        ↓
Local browser extension detects the acceptance
        ↓
Problem metadata and submitted solution are collected
        ↓
Local Python server receives the data
        ↓
Solution is organized in this repository
        ↓
Git commit
        ↓
Git push
        ↓
GitHub repository updated
```

The automation runs locally and is designed specifically for my own LeetCode submissions.

### Security

Security and least-privilege access are important design requirements for the automation system.

The system:

* Does not require LeetCode passwords to be stored.
* Does not require GitHub passwords to be stored.
* Does not intentionally read or transmit browser cookies.
* Does not place credentials or tokens in source code.
* Uses a local Python server bound to `127.0.0.1`.
* Does not expose the local synchronization server publicly.
* Targets only this LeetCode repository.
* Avoids unnecessary third-party automation services.

The browser extension and local server communicate through the local machine rather than sending credentials or session information to a separate cloud service.

## Goals

This repository serves several purposes:

1. **DSA Practice**
   Build consistency through regular problem solving.

2. **Problem-Solving Skills**
   Improve algorithmic thinking and recognize common patterns.

3. **Code Quality**
   Practice writing readable and maintainable solutions.

4. **Progress Tracking**
   Maintain a permanent record of solved problems.

5. **Automation & Engineering**
   Build practical software engineering skills by automating the process of archiving accepted solutions.

## Disclaimer

These solutions represent my own learning and problem-solving process.

They are intended primarily for educational and reference purposes. If you are currently solving a LeetCode problem yourself, try solving it independently before looking at an existing solution.

---

**Author:** Vedant Joshi
**Repository:** [jvedant1001-ship-it/LeetCode](https://github.com/jvedant1001-ship-it/LeetCode)
