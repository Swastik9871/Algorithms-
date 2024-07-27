def rabin_karp_search(pattern, text):
    d = 256  # Size of the alphabet
    q = 101  # A prime number for the hash function
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1, q)  
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    # Slide the pattern over the text
    for i in range(n - m + 1):
        if p == t and pattern == text[i:i+m]:
            return i  
        # Update hash for the next window in the text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q
            t = (t + q) % q  
    return -1  # No match found

# Example usage:
text = "GOOGLE"
pattern = "OG"
result = rabin_karp_search(pattern, text)
print("Pattern found at index:", result)