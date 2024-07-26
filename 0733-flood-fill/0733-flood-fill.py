class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:  # Check if the image is empty
            return image
        
        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        
        def dfs(r, c):
            # Check if the current position is within bounds and matches the original color
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != originalColor:
                return
            
            # Change the color of the current pixel
            image[r][c] = color
            
            # Perform DFS in all four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Start DFS from the initial position
        dfs(sr, sc)
        return image
