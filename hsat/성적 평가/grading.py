N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]

def get_rank(score):
    sorted_score = sorted(score, reverse=True)

    rank_dict = {}

    for i, s in enumerate(sorted_score):
        if s not in rank_dict:
            rank_dict[s] = i + 1

    result = []

    for s in score:
        result.append(rank_dict[s])

    return result


# 3번 경기 각각 순위
for score in scores:
    ranks = get_rank(score)
    print(*ranks)


# 사람별 총점
total_scores = []

for i in range(N):
    total = 0

    for j in range(3):
        total += scores[j][i]

    total_scores.append(total)


# 총점 기준 순위
total_ranks = get_rank(total_scores)

print(*total_ranks)