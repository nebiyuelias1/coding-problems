def solution(message, K):
    # write your code in Python 3.6
    if K == 0:
        return ''
    
    s = []
    total_len = 0
    words = message.split(' ')

    for word in words:
        if len(word) + total_len <= K:
            s.append(word)
            total_len += len(word) + 1
        else:
            break

    return ' '.join(s).rstrip()

print(solution('The quick brown fox jumps over the lazy dog', 39))