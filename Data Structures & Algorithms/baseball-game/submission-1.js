class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        let stack = []
        let score = 0

        for (let i = 0; i < operations.length; i ++) {
            let op = operations[i]

            if (op == "+") {
                let prevScore = stack.pop()
                let prevSecScore = stack.pop()
                let newScore = prevScore + prevSecScore
                stack.push(prevSecScore)
                stack.push(prevScore)
                stack.push(newScore)
                score += newScore
            } else if (op == "D") {
                let lastScore = stack[stack.length - 1]
                let newScore = lastScore * 2
                stack.push(newScore)
                score += newScore
            } else if (op == "C") {
                let removedScore = stack.pop()
                score -= removedScore
            } else {
                let val = Number(op)
                stack.push(val)
                score += val
            }
        }
        return score
    }
}
