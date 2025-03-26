def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{s[i-1]}")
            else:
                encoded.append(s[i-1])
            count = 1
    encoded.append(f"{count}{s[-1]}" if count > 1 else s[-1])
    return ''.join(encoded)