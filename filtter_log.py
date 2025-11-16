import re

INPUT_FILE = "./full_logs.txt"
OUTPUT_FILE = "./filtered_logs.txt"


ERROR_PATTERNS = [
    r"\berror\b",
    r"\bfail(?:ed|ure|s)?\b",
    r"exit code",
    r"\bexception\b",
    r"\btraceback\b",
    r"^E\d{3}",  # flake8 errors
    r"^F\d{3}",  # flake8 fatal errors
    r"AssertionError",  # unittest errors
    r"FAILED",  # pytest-style summary
    r"not found",  # missing files
]


# Read all lines
with open(INPUT_FILE, "r", errors="ignore") as f:
    lines = f.readlines()


def matches(line):
    return any(re.search(p, line, re.IGNORECASE) for p in ERROR_PATTERNS)


filtered = []
context_range = 2  # number of surrounding lines to include

for i, line in enumerate(lines):
    if matches(line):
        start = max(0, i - context_range)
        end = min(len(lines), i + context_range + 1)
        filtered.extend(lines[start:end])
        filtered.append("\n" + "-" * 80 + "\n")  # separator

# Remove duplicates while preserving order
seen = set()
final_output = []
for line in filtered:
    if line not in seen:
        seen.add(line)
        final_output.append(line)

# Save result
with open(OUTPUT_FILE, "w") as f:
    f.writelines(final_output)

print(f"Filtered error log saved to {OUTPUT_FILE}")
