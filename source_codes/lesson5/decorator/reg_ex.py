import re

sample_string = "There will be a heavy rain on 27-03-2026 and 28-03-2026."

pattern = r"(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-(?:\d{4})"
pattern2 = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})"


matches = re.findall(pattern, sample_string)
matches2 = re.findall(pattern2, sample_string)

print(matches)
print(matches2)

