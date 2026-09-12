class Solution(object):
    def calPoints(self, operations):
        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        return sum(record)
        