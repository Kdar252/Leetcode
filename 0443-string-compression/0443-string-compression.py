class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer to write the compressed characters
        start = 0  # Pointer to the start of the current group

        while start < len(chars):
            end = start  # Pointer to find the end of the current group

            # Find the end of the current group of the same character
            while end < len(chars) and chars[start] == chars[end]:
                end += 1

            # Write the character
            chars[write] = chars[start]
            write += 1

            # Write the count if greater than 1
            if end - start > 1:
                count_str = str(end - start)
                for char in count_str:
                    chars[write] = char
                    write += 1

            # Move to the next group
            start = end

        return write

 