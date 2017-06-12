/* You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water
inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid 
is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16 */


class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        /*对于每个岛屿格子先默认加上四条边，然后检查其左面和上面是否有岛屿格子，
        有的话分别减去两条边，即得正确的结果*/
        
        if (grid.empty()) return 0;
        int count = 0;
        for (int i=0; i<grid.size(); i++){
            for (int j=0; j<grid[0].size(); j++){
                if (grid[i][j]){
                    count += 4;
                    if (i>0 && grid[i-1][j]) count -= 2;
                    if (j>0 && grid[i][j-1]) count -= 2;
                }
            }
        }
        return count;
    }
};





