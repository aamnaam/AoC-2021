def count_increasing(nums):
    prev_num = nums[0]
    count = 0
    for num in nums[1:]:
        if num > prev_num:
            count += 1
        prev_num = num

    return count


def count_window_increasing(nums):
    prev_sum = nums[0] + nums[1] + nums[2]
    count = i = 0
    j = 3

    while j < len(nums):
        curr_sum = prev_sum - nums[i] + nums[j]
        if curr_sum > prev_sum:
            count += 1
        i += 1
        j += 1
        prev_sum = curr_sum

    return count


def main():
    with open("01-SonarSweep/input.txt") as f:
        depths = [int(x) for x in f.read().split("\n")]

    print(f"Part 1: {count_increasing(depths)}")
    print(f"Part 2: {count_window_increasing(depths)}")


if __name__ == '__main__':
    main()
