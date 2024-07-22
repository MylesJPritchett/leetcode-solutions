class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
# Create a list of tuples (name, height)
        people = list(zip(names, heights))
        
        # Sort the list of tuples by height in descending order
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        sorted_names = [name for name, height in people]
        
        return sorted_names