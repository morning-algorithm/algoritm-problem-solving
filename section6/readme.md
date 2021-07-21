brute-force (back tracking, state-space tree & cut edge) - dfs basic

## Learned

### ⛽ 재귀함수 
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
      <image src="https://user-images.githubusercontent.com/60434971/126507094-730ee442-75e9-4d13-8cda-18406d3e5b7f.jpg" width="500"/><br/><br/>
    

### 🌲 깊이 우선 탐색  
* 트리의 구조 <br/>
<image src="https://user-images.githubusercontent.com/60434971/126518908-43966f53-6ef8-4197-aac6-884ace572291.png" width="500"/><br/>

* 트리탐색
  * DFS: 깊이우선탐색
  * BFS: 넓이우선탐색 <br/><br/>

* 깊이우선탐색
  * 기본적으로 왼쪽 자식 먼저 탐색 <br/>
   <image src="https://user-images.githubusercontent.com/60434971/126519226-98205c22-a73e-409e-a304-425f96185aae.png" width="500"/><br/>

  * 전위, 중위, 후위 탐색 모두 파고 들어가다가 막히면 back하는 메커니즘은 똑같다.<br/><br/><br/>
  * **전위 순회**
    * 부모 -> 왼쪽 -> 오른쪽 순으로 출력.
    * 자기 본연의 것을 먼저 수행하고 ( 여기서는 자신을 출력 ) 왼쪽자식, 오른쪽 자식을 탐색<br/>
    
      ```
      def dfs(v):
          if x > n: 
              return
          print(v)
          dfs(v*2)
          dfs(v*2+1) 
       ```
    
    <image src="https://user-images.githubusercontent.com/60434971/126519453-74112cfc-731b-4efb-b41b-4d6d941f5766.png" width="350"/><br/>
  
  * **중위 순회**
    * 왼 -> 부 -> 오 순으로 출력.
    * 왼쪽 자식 탐색, 자신 출력, 오른쪽 자식 탐색<br/>
       ```
          dfs(v*2)
          print(v)
          dfs(v*2+1) 
       ```
    <image src="https://user-images.githubusercontent.com/60434971/126520197-0335e9ac-1bbc-4517-b8fd-e9cc92b46ca2.png" width="350"/><br/>
  
  * **후위 순회**
    * 왼 -> 오 -> 부 순으로 출력.
    * 왼쪽 자식 탐색, 자신 출력, 오른쪽 자식 탐색<br/>
        ```
          dfs(v*2)
          dfs(v*2+1) 
          print(v)
        ```
    <image src="https://user-images.githubusercontent.com/60434971/126520235-24b50815-cee8-4f1c-a9fe-9b2e6a903f47.png" width="350"/><br/>
  
    => 모두 스택에 어떻게 쌓이는지 생각해보기!
