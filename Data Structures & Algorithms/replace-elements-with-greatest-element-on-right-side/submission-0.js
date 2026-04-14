class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {

        let largestNum = -1

        for (let i = arr.length -1; i >= 0; i--) {
            let temp = arr[i]
            arr[i] = largestNum
            largestNum = Math.max(largestNum, temp)
        }

        return arr

    }
}
