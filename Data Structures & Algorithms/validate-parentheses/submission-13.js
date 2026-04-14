class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {

        let myStack = []
        let closedParens = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for (let i = 0; i < s.length; i++) {
            if (myStack.length > 0 && closedParens[s[i]] === myStack[myStack.length - 1]) {
                myStack.pop()
            } else {
                myStack.push(s[i])
            }
        }

        return myStack.length === 0
    }
}