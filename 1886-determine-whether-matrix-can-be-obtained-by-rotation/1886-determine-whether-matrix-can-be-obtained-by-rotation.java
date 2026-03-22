class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n= mat.length;
        for(int r=0; r<4; r++){
            if(Arrays.deepEquals(mat,target)){
                return true;
            }
        
        for(int i=0; i<n;i++){
            for(int j=i+1;j<n;j++){
                int temp = mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]=temp;
                
            }
        }
        for(int i=0;i<n;i++){
            int left = 0;
            int right = n-1;
            while(left<right){
                int temp = mat[i][left];
                mat[i][left]=mat[i][right];
                mat[i][right]=temp;
                left++;
                right--;
            }
        }
        }
        return false;
    }
}