import sys, re, matplotlib.pyplot as plt
from collections import Counter

ip_regex = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ips = []

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f:
        match = ip_regex.match(line)
        if match:
            ips.append(match.group(1))

# 集計して上位10件をグラフ化
counts = Counter(ips).most_common(10)
labels, values = zip(*counts)

plt.bar(labels, values)
plt.xticks(rotation=45) # IPが重ならないよう斜めに
plt.tight_layout()
plt.show()