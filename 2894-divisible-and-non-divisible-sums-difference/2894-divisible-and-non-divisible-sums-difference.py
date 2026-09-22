class Solution(object):

  def differenceOfSums(self, n, m):
    total_sum = n * (n + 1) // 2
    k = n // m
    num2 = m * k * (k + 1) // 2

    return total_sum - 2 * num2