brute-force (back tracking, state-space tree & cut edge) - dfs basic

DFS : 깊이 우선 탐색
- 전위 순회(pre-order traversal) : p -> c1 -> c2
- 중위 순회(in-order traversal) : c1 -> p -> c2
- 후위 순회(post-order traversal) : c1 -> c2 -> p 

** 이진트리의 루트 노드의 인덱스를 1이라고 할 때,
(왼쪽 자식 노드의 인덱스) = (부모 노드의 인덱스)*2
(오른쪽 자식 노드의 인덱스) = (부모 노드의 인덱스)*2+1

BFS : 넓이 우선 탐색 (level 탐색)