from functools import reduce
import random

# Two groups of size 10
# Rest will be whatever left remains
GROUP_SIZES = [10, 10, 10]


def to_groups(seq, group_sizes):
    groups = {}
    seq_index = 0
    group_index = 1

    total_sizes = reduce(lambda x, y: x + y, group_sizes)

    if total_sizes < len(seq):
        group_sizes.append(len(seq) - total_sizes)

    for size in group_sizes:
        elements_taken = 0
        group_name = "Group {}".format(group_index)
        groups[group_name] = []
        while elements_taken < size and seq_index < len(seq):
            groups[group_name].append(seq[seq_index])
            seq_index += 1
            elements_taken += 1
        group_index += 1

    return groups


def get_stats(teams):
    teams_count = len(teams)
    total_minutes = teams_count * 6
    total_hours = total_minutes / 60

    stats = {"teams_count": teams_count,
             "total_minutes": total_minutes,
             "total_hours": total_hours}

    return stats


teams = open("teams").read().split("\n")

teams = [team.strip() for team in teams if team.strip() != ""]
random.shuffle(teams)
print(teams)

groups = to_groups(teams, GROUP_SIZES)

print(sum([len(groups[group]) for group in groups]))

stats = get_stats(teams)

result = []

result.append("Total number of teams: {}\n".format(stats["teams_count"]))
result.append("Total minutes of presenting: {}\n".format(stats["total_minutes"]))
result.append("Total hours of presenting: {}\n".format(stats["total_hours"]))

groups_order = sorted(groups.keys())

for key in groups_order:
    result.append("## " + key)
    result.append("\n" + "\n".join(list(map(lambda x: "* " + x, groups[key]))))
    result.append("\n")

handler = open("schedule.md", "w")
handler.write("\n".join(result))
handler.close()
