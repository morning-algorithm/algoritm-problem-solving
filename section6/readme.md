brute-force (back tracking, state-space tree & cut edge) - dfs basic

## Learned
* 재귀함수
  * 자기자신을 호출하는 함수
  * stack 이용해서 운영됨 
  * 반복문의 대체제(3,4중 for문의 코드 유연성을 대체)
  
  * ex) 3을 입력 -> 1~3을 출력하는 프로그램
    ``` 
    def dfs(x):
      if x>0: # 무한루프 방지
        dfs(x-1) #1,2,3 순서로 출력되기 위해 print 전에 재귀함수 호출. 
        print(x, end = ' ')
    ```
      * print 후에 dfs호출하면 3,2,1순으로 출력 => stack을 이용하기 때문.
      * 
      <image src="https://user-images.githubusercontent.com/60434971/126507094-730ee442-75e9-4d13-8cda-18406d3e5b7f.jpg" width="500"/>
    
