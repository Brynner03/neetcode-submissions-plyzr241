class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Map counting frequencies string_count
        # where key = sorted string
        # values = array of original strings
        # Loop through array
        # sort the string, and hold in another variable
        # if in map, push original string
        # if not, push original string

        # loop through map frequencies
        # push values into an grouped_strings array

        # Return grouped_strings array

        string_count = {}
        grouped_strings = []

        for string in strs:
            sorted_string = sorted(string)
            conjoined_string = "".join(sorted_string)
            if conjoined_string in string_count:
                string_count[conjoined_string].append(string)
            else:
                string_count[conjoined_string] = [string]

        return list(string_count.values())