import sys
input = sys.stdin.readline

def ai_distance(model_name, context):
    m_len = len(model_name)
    c_len = len(context)
    min_len = min(m_len, c_len)

    mismatch = 0
    for i in range(min_len):
        if model_name[i] != context[i]:
            mismatch += 1

    mismatch += abs(m_len - c_len)
    return mismatch

modelOne, modelTow = input().strip().split()
parityOne, parityTow = input().strip().split()

parity_map = {'even': 0, 'odd': 1}
parityOne = parity_map[parityOne]
parityTow = parity_map[parityTow]

n = int(input())
context = [input().strip() for _ in range(n)]

score1 = 0
score2 = 0


q = int(input())
for _ in range(q):
    parts = input().strip().split()
    if parts[0] == 'MODIFY':
        idx = int(parts[1]) - 1
        new_str = ' '.join(parts[2:])
        context[idx] = new_str

    elif parts[0] == 'TEST':
        l = int(parts[1]) - 1
        r = int(parts[2]) - 1

        # Model 1
        valid1 = []
        for i in range(l, r + 1):
            dist = ai_distance(modelOne, context[i])
            if dist % 2 == parityOne:
                valid1.append(dist)
        max1 = max(valid1) if valid1 else 0
        score1 ^= max1

        # Model 2
        valid2 = []
        for i in range(l, r + 1):
            dist = ai_distance(modelTow, context[i])
            if dist % 2 == parityTow:
                valid2.append(dist)
        max2 = max(valid2) if valid2 else 0
        score2 ^= max2

        # Compare scores
        if score1 > score2:
            print(f"ALICE {score1 - score2}")
        elif score2 > score1:
            print(f"BOB {score2 - score1}")
        else:
            print("Draw")