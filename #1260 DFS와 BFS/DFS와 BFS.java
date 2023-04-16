import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int N, M, V;
	public static int[][] graph;
	// public static boolean[] visit;

	public static void dfs(boolean[] visit, int v) {
		visit[v] = true;
		System.out.print(v + " ");
		for (int i = 1; i <= N; i++) {
			if (!visit[i] && graph[v][i] == 1) {
				dfs(visit, i);
			}
		}

	}

	public static void bfs(boolean[] visit) {
		Queue<Integer> myQue = new LinkedList<>();
		visit = new boolean[N + 1];
		myQue.add(V);

		while (!myQue.isEmpty()) {
			int curr = myQue.poll();

			if (visit[curr]) {
				continue;
			}

			visit[curr] = true;
			System.out.print(curr + " ");

			for (int i = 1; i <= N; i++) {
				if (graph[curr][i] == 1 && !visit[i]) {
					myQue.add(i);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); // 정점의 개수
		M = Integer.parseInt(st.nextToken()); // 간선의 개수
		V = Integer.parseInt(st.nextToken()); // 탐색을 시작할 노드 번호

		graph = new int[N + 1][N + 1];
		boolean[] visit = new boolean[N + 1];

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int v1 = Integer.parseInt(st.nextToken());
			int v2 = Integer.parseInt(st.nextToken());

			graph[v1][v2] = 1;
			graph[v2][v1] = 1;
		}

		dfs(visit, V);
		System.out.println();
		bfs(visit);

	}
}