import math
from collections import Counter
import matplotlib.pyplot as plt

# ---------------- READ DATA ----------------
with open("random_bytes.txt", "r") as f:
    data = [int(line.strip()) for line in f if line.strip()]

# ---------------- HISTOGRAM ----------------
plt.hist(data, bins=256)
plt.title("QRNG Byte Distribution")
plt.xlabel("Byte Value")
plt.ylabel("Frequency")
plt.show()

# ---------------- BIT BALANCE ----------------
zeros = 0
ones = 0

for byte in data:
    bits = format(byte, "08b")
    zeros += bits.count("0")
    ones += bits.count("1")

print("Total bits:", zeros + ones)
print("0s:", zeros)
print("1s:", ones)
print("Zero-One Balance:", zeros / (zeros + ones), ones / (zeros + ones))

# ---------------- ENTROPY ----------------
counts = Counter(data)
total = len(data)

entropy = -sum((count/total) * math.log2(count/total)
               for count in counts.values())

print("Entropy:", entropy, "/ 8")
