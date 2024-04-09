class Solution:
    @classmethod
    def isRobotBounded(self, instructions:str)->bool:
        directions = {
            'north' : [0,1],
            'east' : [1, 0],
            'south' : [0,-1],
            'west' : [-1,0]
        }

        dir = 'north'
        option = [0,0]
        # G, L, R
        for act in instructions:
            if act == 'G':
                option[0]+= directions[dir][0]
                option[1]+= directions[dir][1]
            # change direction
            else:
                temp = list(directions)
                keyPos = temp.index(dir)
                if keyPos > 3:
                    keyPos = -1
                if act == 'L':
                    dir = temp[keyPos+1]
                if act == 'R':
                    dir = temp[keyPos-1]
            
            print("direction:", dir ,option)

        return option == [0,0]

# 
# Input: instructions = "GGLLGG"
# Output: true   
instructions = "GGLLGG"
print(Solution.isRobotBounded(instructions))


# Input: instructions = "GG"
# Output: false
instructions = "GG"
print(Solution.isRobotBounded(instructions))

# Input: instructions = "GL"
# Output: true
instructions = "GL"
print(Solution.isRobotBounded(instructions))