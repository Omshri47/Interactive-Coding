class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 1:
            return encodedText.rstrip()
            
        n = len(encodedText)
        cols = n // rows
        result = []
        
        # Iterate through each diagonal's starting column
        for start_col in range(cols):
            # Traverse down the diagonal
            for i in range(rows):
                # Calculate current column in the diagonal
                curr_col = start_col + i
                
                # If the column exceeds the matrix width, this diagonal is done
                if curr_col >= cols:
                    break
                
                # Convert 2D coordinates (i, curr_col) to 1D index
                idx = i * cols + curr_col
                result.append(encodedText[idx])
                
        # Join the characters and remove trailing spaces
        return "".join(result).rstrip()