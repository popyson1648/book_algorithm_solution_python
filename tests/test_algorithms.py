"""小規模総当たり・独立した標準実装・不変条件を用いる検証。"""
import itertools
import math
import random
import unittest
from types import SimpleNamespace

from support import capture, load, run_main


class AlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(20261030)

    def test_complexity_examples_and_search(self):
        for n in (0, 1, 9):
            self.assertEqual(load('codes/2/1').count_operations(n), n)
            self.assertEqual(load('codes/2/2').count_operations(n), n * n)
        self.assertEqual(run_main('codes/2/3', '8\n'), '2\n4\n6\n8\n')
        cp = load('codes/2/4')
        self.assertEqual(cp.closest_pair([(0, 0), (3, 4)]), 5)
        self.assertEqual(cp.closest_pair([(0, 0), (0, 0)]), 0)
        self.assertEqual(cp.closest_pair([(0, 0), (10**10, 0)]), 10**10)
        for _ in range(40):
            a = [self.rng.randint(-10, 10) for _ in range(self.rng.randint(1, 20))]
            value = self.rng.randint(-10, 10)
            self.assertEqual(load('codes/3/1').contains(a, value), value in a)
            self.assertEqual(load('codes/3/2').find_index(a, value), a.index(value) if value in a else -1)
            self.assertEqual(load('codes/3/3').minimum(a), min(a))
            self.assertEqual(load('solutions/3/1').count_matches(a, value), a.count(value))
            self.assertEqual(load('solutions/3/3').spread(a), max(a) - min(a))
            if len(a) >= 2:
                self.assertEqual(load('solutions/3/2').second_smallest(a), sorted(a)[1])
        self.assertEqual(load('codes/3/3').minimum([10**30, 10**40]), 10**30)

    def test_pair_sum(self):
        slow, fast = load('codes/3/4'), load('codes/6/4')
        for _ in range(80):
            a = [self.rng.randint(-20, 30) for _ in range(6)]
            b = [self.rng.randint(-20, 30) for _ in range(6)]
            k = self.rng.randint(-30, 50)
            expected = min((x + y for x in a for y in b if x + y >= k), default=math.inf)
            self.assertEqual(slow.minimum_pair_sum(a, b, k), expected)
            self.assertEqual(fast.minimum_pair_sum(a, b, k), expected)
        self.assertEqual(fast.minimum_pair_sum([10**30], [10**30], 1), 2 * 10**30)
        # b末尾へのlower_boundで誤って末尾要素を参照しない。
        self.assertEqual(fast.minimum_pair_sum([0, 100], [1, 2], 50), 101)

    def test_recurrences(self):
        self.assertEqual(load('codes/4/1').func(20), 210)
        value, output = capture(load('codes/4/2').func, 2)
        self.assertEqual(value, 3)
        self.assertEqual(output, 'func(2) を呼び出しました\nfunc(1) を呼び出しました\nfunc(0) を呼び出しました\n1 までの和 = 1\n2 までの和 = 3\n')
        gcd = load('codes/4/4').gcd
        for a, b in [(51, 15), (15, 51), (7, 0), (0, 7), (81, 81)]:
            self.assertEqual(gcd(a, b), math.gcd(a, b))
        f = [0, 1]
        for _ in range(48):
            f.append(f[-1] + f[-2])
        for n in range(12):
            self.assertEqual(load('codes/4/5').fibo(n), f[n])
            self.assertEqual(capture(load('codes/4/6').fibo, n)[0], f[n])
        memo = [-1] * 50
        self.assertEqual(load('codes/4/8').fibo(49, memo), f[49])
        expected = ''.join(f'{n} 項目: {f[n]}\n' for n in range(2, 50))
        self.assertEqual(run_main('codes/4/7'), expected)
        self.assertEqual(run_main('codes/4/8'), expected)
        trib = [0, 0, 1]
        for _ in range(15):
            trib.append(sum(trib[-3:]))
        for n in range(14):
            self.assertEqual(load('solutions/4/1').func(n), trib[n])
            self.assertEqual(load('solutions/4/2').func(n, [-1] * (n + 1)), trib[n])
        for n in (0, 356, 357, 575, 10000):
            expected = sum(set(str(x)) == set('357') for x in range(1, n + 1))
            self.assertEqual(load('solutions/4/3').count_753(n), expected)

    def test_subset_sum_variants(self):
        for _ in range(60):
            a = [self.rng.randint(0, 9) for _ in range(self.rng.randint(0, 8))]
            target = self.rng.randint(0, 25)
            possibilities = [(sum(a[i] for i in range(len(a)) if mask >> i & 1), mask.bit_count())
                             for mask in range(1 << len(a))]
            expected = any(total == target for total, _ in possibilities)
            self.assertEqual(load('codes/3/6').subset_sum(a, target), expected)
            self.assertEqual(load('codes/4/9').func(len(a), target, a), expected)
            self.assertEqual(load('solutions/4/4').subset_sum(a, target), expected)
            self.assertEqual(load('solutions/5/3').subset_sum(a, target), expected)
            limit = self.rng.randint(0, 5)
            limited = any(total == target and count <= limit for total, count in possibilities)
            for key in ('solutions/5/4', 'solutions/5/6'):
                self.assertEqual(load(key).subset_sum_at_most_k(a, target, limit), limited)
        # 原文は途中で負のwを参照する。この回帰ケースを明示。
        self.assertFalse(load('solutions/4/4').subset_sum([10, 20, 30], 1))
        for _ in range(35):
            a = [self.rng.randint(1, 8) for _ in range(3)]
            target = self.rng.randint(0, 20)
            expected = any(sum(x * y for x, y in zip(a, counts)) == target
                           for counts in itertools.product(*(range(target // x + 1) for x in a)))
            self.assertEqual(load('solutions/5/9').subset_sum(a, target), expected)
            items = [(x, self.rng.randint(0, 3)) for x in a]
            expected = any(sum(x * c for (x, _), c in zip(items, counts)) == target
                           for counts in itertools.product(*(range(limit + 1) for _, limit in items)))
            self.assertEqual(load('solutions/5/10').bounded_subset_sum(items, target), expected)

    def test_transition_fragments(self):
        for key in ('solutions/5/2', 'solutions/5/7', 'solutions/5/8'):
            m = load(key)
            dp = [[True, False, False, False, False], [False] * 5]
            for j in range(5):
                m.transition(dp, [2], 0, j)
            self.assertEqual(dp[1], [True, False, True, False, key.endswith('/8')])
        dp = [[0, math.inf, 1, math.inf, math.inf], [math.inf] * 5]
        for j in range(5):
            load('solutions/5/5').transition(dp, [2], 0, j)
        self.assertEqual(dp[1], [0, math.inf, 1, math.inf, 2])
        dp = [[math.inf] * 4 for _ in range(4)]
        dp[0][1], dp[1][2], dp[2][3] = 0, 0, 0
        dp[0][2], dp[1][3] = 3, 5
        load('solutions/5/12').relax_interval(dp, [0, 1, 3, 6], 0, 3)
        self.assertEqual(dp[0][3], 9)
        self.assertEqual(load('codes/5/2').chmin(7, 3), 3)
        self.assertEqual(load('codes/5/2').chmin(3, 7), 3)
        self.assertEqual(load('codes/14/1').chmin(7, 3), (3, True))
        self.assertEqual(load('codes/14/1').chmin(3, 3), (3, False))

    def test_frog_and_knapsack(self):
        def frog_oracle(h, i=0):
            if i == len(h) - 1:
                return 0
            return min(abs(h[i] - h[j]) + frog_oracle(h, j)
                       for j in (i + 1, i + 2) if j < len(h))
        for _ in range(35):
            h = [self.rng.randint(-20, 20) for _ in range(self.rng.randint(1, 9))]
            for num in (1, 3, 4, 6):
                self.assertEqual(load(f'codes/5/{num}').frog(h), frog_oracle(h))
            items = [(self.rng.randint(1, 8), self.rng.randint(0, 30)) for _ in range(6)]
            capacity = self.rng.randint(0, 20)
            expected = max(sum(items[i][1] for i in range(6) if mask >> i & 1)
                           for mask in range(64)
                           if sum(items[i][0] for i in range(6) if mask >> i & 1) <= capacity)
            self.assertEqual(load('codes/5/7').knapsack(items, capacity), expected)

    def test_strings_and_intervals(self):
        ed = load('codes/5/8').edit_distance
        for s, t, expected in [('', '', 0), ('', 'abc', 3), ('kitten', 'sitting', 3), ('abc', 'abc', 0), ('あいう', 'あう', 1)]:
            self.assertEqual(ed(s, t), expected)
            self.assertEqual(ed(t, s), expected)
        lcs = load('solutions/5/11').lcs_length
        for _ in range(35):
            s = ''.join(self.rng.choice('abc') for _ in range(6))
            t = ''.join(self.rng.choice('abc') for _ in range(5))
            subsequences = {''.join(s[i] for i in range(len(s)) if mask >> i & 1)
                            for mask in range(1 << len(s))}
            other = {''.join(t[i] for i in range(len(t)) if mask >> i & 1)
                     for mask in range(1 << len(t))}
            self.assertEqual(lcs(s, t), max(map(len, subsequences & other)))
        for _ in range(25):
            n = 5
            c = [[self.rng.randint(-5, 15) for _ in range(n + 1)] for _ in range(n + 1)]
            expected = math.inf
            for mask in range(1 << (n - 1)):
                boundaries = [0] + [i for i in range(1, n) if mask >> (i - 1) & 1] + [n]
                expected = min(expected, sum(c[x][y] for x, y in zip(boundaries, boundaries[1:])))
            self.assertEqual(load('codes/5/9').partition_cost(c), expected)
        def merge_oracle(a):
            if len(a) == 1:
                return 0
            return min(a[i] + a[i + 1] + merge_oracle(a[:i] + [a[i] + a[i + 1]] + a[i + 2:])
                       for i in range(len(a) - 1))
        for _ in range(20):
            a = [self.rng.randint(1, 12) for _ in range(self.rng.randint(1, 6))]
            self.assertEqual(load('solutions/5/13').slime_cost(a), merge_oracle(a))

    def test_binary_search_and_greedy(self):
        for value in range(-2, 42):
            m = load('codes/6/1')
            self.assertEqual(m.binary_search(value), m.A.index(value) if value in m.A else -1)
        for threshold in range(-10, 11):
            self.assertEqual(load('codes/6/2').binary_search(lambda x: x >= threshold, -11, 11), threshold)
        for age in range(20, 36):
            lo, hi, answers = 20, 36, []
            while hi - lo > 1:
                mid = (lo + hi) // 2
                answers.append('yes' if age < mid else 'no')
                if age < mid:
                    hi = mid
                else:
                    lo = mid
            self.assertTrue(run_main('codes/6/3', '\n'.join(answers) + '\n').endswith(f'The age is {age}!\n'))
        for _ in range(25):
            balloons = [(self.rng.randint(0, 10), self.rng.randint(1, 5)) for _ in range(5)]
            expected = min(max(h + s * i for i, (h, s) in enumerate(order))
                           for order in itertools.permutations(balloons))
            self.assertEqual(load('codes/6/5').shooting_king(balloons), expected)
            a = self.rng.sample(range(30), 7)
            count = self.rng.randint(2, 7)
            expected = max(min(y - x for x, y in zip(sorted(xs), sorted(xs)[1:]))
                           for xs in itertools.combinations(a, count))
            self.assertEqual(load('solutions/6/3').maximum_spacing(a, count), expected)
        self.assertEqual(load('codes/7/1').coin_count(620, [1, 2, 2, 3, 0, 0]), 4)
        for _ in range(25):
            intervals = [(start, start + self.rng.randint(1, 8)) for start in self.rng.sample(range(15), 7)]
            best = 0
            for mask in range(1 << len(intervals)):
                chosen = sorted(intervals[i] for i in range(len(intervals)) if mask >> i & 1)
                if all(x[1] <= y[0] for x, y in zip(chosen, chosen[1:])):
                    best = max(best, len(chosen))
            self.assertEqual(load('codes/7/2').schedule(intervals), best)
        self.assertEqual(load('codes/7/3').multiple_array([(3, 5), (2, 7), (9, 4)]), 7)
        self.assertEqual(load('codes/7/3').multiple_array([(10, 5)]), 0)
        for _ in range(25):
            a = [self.rng.randint(0, 9) for _ in range(4)]
            b = [self.rng.randint(0, 9) for _ in range(4)]
            expected = max(sum(x < y for x, y in zip(a, p)) for p in itertools.permutations(b))
            self.assertEqual(load('solutions/7/1').match_count(a, b), expected)

    def test_small_enumerations(self):
        for k in range(6):
            for n in range(3 * k + 2):
                expected = sum(sum(values) == n for values in itertools.product(range(k + 1), repeat=3))
                for key in ('solutions/3/5', 'solutions/3/6'):
                    self.assertEqual(load(key).count_triples(k, n), expected)
        shift = load('solutions/3/4')
        self.assertEqual(shift.shift_only([8, 12, 40]), 2)
        with self.assertRaises(ValueError):
            shift.how_many_times(0)
        for s in ('0', '9', '125', '1001', '99999'):
            expected = 0
            for mask in range(1 << (len(s) - 1)):
                parts, last = [], 0
                for i in range(len(s) - 1):
                    if mask >> i & 1:
                        parts.append(int(s[last:i + 1]))
                        last = i + 1
                expected += sum(parts) + int(s[last:])
            self.assertEqual(load('solutions/3/7').expression_sum(s), expected)
        for _ in range(20):
            a = [[self.rng.randrange(20) for _ in range(3)] for _ in range(5)]
            expected = max(sum(a[i][k] for i, k in enumerate(schedule))
                           for schedule in itertools.product(range(3), repeat=5)
                           if all(x != y for x, y in zip(schedule, schedule[1:])))
            self.assertEqual(load('solutions/5/1').vacation(a), expected)

    def test_linked_lists(self):
        for key in ('codes/8/2', 'codes/8/5'):
            node = load(key).Node('a')
            self.assertEqual(node.name, 'a')
            self.assertIsNone(node.next)
            if key.endswith('/5'):
                self.assertIsNone(node.prev)
        a, b, c = (SimpleNamespace(name=x, next=None) for x in 'abc')
        a.next = c
        load('codes/8/3').insert(b, a)
        self.assertIs(a.next, b)
        self.assertIs(b.next, c)
        for key in ('codes/8/4', 'codes/8/6'):
            m = load(key)
            m.init()
            nodes = [m.Node(x) for x in 'abc']
            for node in nodes:
                m.insert(node)
            self.assertEqual(capture(m.print_list)[1], 'c -> b -> a -> \n')
            self.assertEqual(capture(load('solutions/8/1').print_list, m.nil)[1], 'c -> b -> a -> \n')
            if key.endswith('/6'):
                m.erase(nodes[1])
                m.erase(m.nil)
                self.assertIs(nodes[2].next, nodes[0])
                self.assertIs(nodes[0].prev, nodes[2])
                m.erase(nodes[0])
                m.erase(nodes[2])
                self.assertIs(m.nil.next, m.nil)
                self.assertIs(m.nil.prev, m.nil)
            else:
                load('solutions/8/3').erase(nodes[1], nodes[2], m.nil)
                self.assertIs(nodes[2].next, nodes[0])
                load('solutions/8/3').erase(m.nil, nodes[0], m.nil)
                self.assertIs(nodes[0].next, m.nil)
        visits = []
        def get(i):
            cur = a
            for _ in range(i):
                cur = cur.next
            visits.append(i + 1)
            return cur.name
        self.assertEqual(capture(load('solutions/8/2').print_by_index, 3, get)[1], 'a\nb\nc\n')
        self.assertEqual(sum(visits), 6)
        self.assertEqual(run_main('codes/8/1'), '4\n12\n5\n')

    def test_stack_queue_heap(self):
        st = load('codes/9/1')
        st.MAX, st.st = 3, [0] * 3
        st.init()
        for x in (1, 2, 3):
            st.push(x)
        self.assertTrue(st.is_full())
        self.assertEqual(capture(st.push, 4)[1], 'error: stack is full.\n')
        self.assertEqual([st.pop(), st.pop(), st.pop()], [3, 2, 1])
        self.assertEqual(capture(st.pop), (-1, 'error: stack is empty.\n'))
        q = load('codes/9/2')
        q.MAX, q.qu = 4, [0] * 4
        q.init()
        for x in (1, 2, 3):
            q.enqueue(x)
        self.assertTrue(q.is_full())
        self.assertEqual(capture(q.enqueue, 4)[1], 'error: queue is full.\n')
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(4)  # tailが0へ折り返す。
        self.assertEqual([q.dequeue(), q.dequeue(), q.dequeue()], [2, 3, 4])
        self.assertEqual(capture(q.dequeue), (-1, 'error: queue is empty.\n'))
        q.init()
        for i in range(50):
            q.enqueue(i)
            self.assertEqual(q.dequeue(), i)
        h = load('codes/10/5').Heap()
        model = []
        for _ in range(300):
            if not model or self.rng.random() < .6:
                value = self.rng.randrange(-100, 100)
                h.push(value)
                model.append(value)
            else:
                self.assertEqual(h.top(), max(model))
                h.pop()
                model.remove(max(model))
            self.assertTrue(all(h.heap[(i - 1) // 2] >= h.heap[i] for i in range(1, len(h.heap))))
        while model:
            self.assertEqual(h.top(), max(model))
            h.pop()
            model.remove(max(model))
        h.pop()
        self.assertEqual(h.top(), -1)

    def test_union_find_and_graph_construction(self):
        for key in ('codes/11/1', 'codes/11/2'):
            par = [-1, 0, 1, 2]
            self.assertEqual(load(key).root(par, 3), 0)
            self.assertEqual(par, [-1, 0, 0, 0] if key.endswith('/2') else [-1, 0, 1, 2])
        for key in ('codes/11/3', 'codes/11/4', 'codes/15/1', 'solutions/15/1', 'solutions/15/2'):
            uf = load(key).UnionFind(12)
            if key.startswith('solutions/'):
                uf.merge(0, 1)
                uf.init(12)
                self.assertFalse(uf.is_same(0, 1))
            labels = list(range(12))
            merge = getattr(uf, 'unite', None) or uf.merge
            for _ in range(60):
                a, b = self.rng.randrange(12), self.rng.randrange(12)
                expected = labels[a] != labels[b]
                self.assertEqual(merge(a, b), expected)
                old, new = labels[b], labels[a]
                labels = [new if x == old else x for x in labels]
                for i in range(12):
                    self.assertEqual(uf.size(i), labels.count(labels[i]))
                    self.assertEqual(uf.is_same(a, i), labels[a] == labels[i])
        graph = load('codes/10/3').build_graph(3, [(0, 1), (0, 1), (2, 2)])
        self.assertEqual(graph, [[1, 1], [], [2]])
        graph = load('codes/10/4').build_graph(3, [(0, 1, -7), (1, 2, 2)])
        self.assertEqual([[(e.to, e.w) for e in row] for row in graph], [[(1, -7)], [(2, 2)], []])

    def test_sorting_selection_and_ranks(self):
        for _ in range(35):
            a = [self.rng.randrange(100) for _ in range(self.rng.randrange(35))]
            expected = sorted(a)
            for num, name in [(1, 'insertion_sort'), (2, 'merge_sort'), (3, 'quick_sort'), (4, 'heap_sort'), (5, 'bucket_sort')]:
                b = a.copy()
                m = load(f'codes/12/{num}')
                if num == 5:
                    m.MAX = 100
                args = (b, 0, len(b)) if num in (2, 3) else (b,)
                getattr(m, name)(*args)
                self.assertEqual(b, expected)
            for key in ('solutions/6/2', 'solutions/12/1'):
                self.assertEqual(load(key).coordinate_ranks(a), [expected.index(x) for x in a])
            for value in (0, 50, 99, 100):
                self.assertEqual(load('solutions/6/1').rank_in_sorted(expected, value), sum(x < value for x in a))
        # 再帰分割の分岐と、元の疑似コードの0始まり境界を通す。
        select = load('solutions/12/2').select
        for a in [list(range(101)), list(reversed(range(127))), [7] * 251,
                  [self.rng.randrange(20) for _ in range(503)]]:
            expected = sorted(a)
            for k in range(len(a)):
                self.assertEqual(select(a, k), expected[k])
        with self.assertRaises(ValueError):
            select([], 0)
        with self.assertRaises(ValueError):
            load('codes/12/5').bucket_sort([-1])

    def test_rpn_and_parentheses(self):
        calc = load('solutions/9/1').calc
        for expression, value in [('34+12-*', -7), ('82/', 4), ('28-', -6), ('23*4+', 10), ('12/', .5)]:
            self.assertEqual(calc(expression), value)
        check = load('solutions/9/2').check
        self.assertEqual(capture(check, '()()'), (True, '(0, 1), (2, 3)\n'))
        self.assertEqual(capture(check, ')('), (False, 'error\n'))
        self.assertEqual(capture(check, '('), (False, 'too many (\n'))
        self.assertEqual(capture(check, ''), (True, '\n'))

    def test_graph_traversals(self):
        for _ in range(35):
            n = 7
            edges = [(u, v) for u in range(n) for v in range(u + 1, n) if self.rng.random() < .2]
            graph = [[] for _ in range(n)]
            reach = [[i == j for j in range(n)] for i in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                reach[u][v] = reach[v][u] = True
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        reach[i][j] |= reach[i][k] and reach[k][j]
            representatives = {min(i for i in range(n) if reach[v][i]) for v in range(n)}
            for key in ('solutions/13/1', 'solutions/13/2'):
                self.assertEqual(load(key).count_components(graph), len(representatives))
            self.assertEqual(load('codes/11/4').count_components(n, edges), len(representatives))
            for start in range(n):
                for key in ('codes/13/2', 'codes/13/4'):
                    seen = [False] * n
                    load(key).dfs(graph, start, seen)
                    self.assertEqual(seen, reach[start])
                # 距離の独立な反復緩和オラクル。
                expected = [math.inf] * n
                expected[start] = 0
                for _ in range(n):
                    for u, v in edges:
                        expected[u] = min(expected[u], expected[v] + 1)
                        expected[v] = min(expected[v], expected[u] + 1)
                expected = [-1 if d == math.inf else d for d in expected]
                for key in ('codes/13/3', 'solutions/13/3'):
                    self.assertEqual(load(key).bfs(graph, start), expected)
            bipartite = any(all((mask >> u & 1) != (mask >> v & 1) for u, v in edges)
                            for mask in range(1 << n))
            for key in ('codes/13/5', 'solutions/13/4'):
                self.assertEqual(load(key).is_bipartite(graph), bipartite)
                self.assertFalse(load(key).is_bipartite([[0]]))
            dag = [[] for _ in range(n)]
            for u, v in edges:
                dag[u].append(v)
            order = load('codes/13/6').topological_sort(dag)
            self.assertEqual(sorted(order), list(range(n)))
            position = {v: i for i, v in enumerate(order)}
            self.assertTrue(all(position[u] < position[v] for u, v in edges))
        maze = load('solutions/13/5').maze_distance
        self.assertEqual(maze(['S..', '##.', '..G']), 4)
        self.assertEqual(maze(['S#G']), -1)
        self.assertEqual(maze(['SG']), 1)
        with self.assertRaises(ValueError):
            maze(['...'])
        # dequeを使う探索は深いグラフでも再帰深度に依存しない。
        chain = [[i + 1] if i < 4999 else [] for i in range(5000)]
        self.assertEqual(load('codes/13/3').bfs(chain, 0)[-1], 4999)

    def test_shortest_paths(self):
        for _ in range(40):
            n = 6
            # 負の辺を持つDAGでは負閉路なし。パスの全列挙と比較。
            edges = [(u, v, self.rng.randint(-5, 15)) for u in range(n) for v in range(u + 1, n)
                     if self.rng.random() < .4]
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                graph[u].append((v, w))
            expected = [[math.inf] * n for _ in range(n)]
            def enumerate_paths(start, v, distance):
                expected[start][v] = min(expected[start][v], distance)
                for to, weight in graph[v]:
                    enumerate_paths(start, to, distance + weight)
            for start in range(n):
                enumerate_paths(start, start, 0)
                dist, negative = load('codes/14/2').bellman_ford(graph, start)
                self.assertFalse(negative)
                self.assertEqual(dist, expected[start])
            matrix, negative = load('codes/14/5').floyd_warshall(n, edges)
            self.assertFalse(negative)
            self.assertEqual(matrix, expected)
            # 非負グラフ。全単純パスを列挙してDijkstraを比較。
            graph = [[(to, abs(w)) for to, w in row] for row in graph]
            for start in range(n):
                expected[start] = [math.inf] * n
                enumerate_paths(start, start, 0)
                for key in ('codes/14/3', 'codes/14/4'):
                    self.assertEqual(load(key).dijkstra(graph, start), expected[start])
        graph = [[(1, 1)], [(2, -2)], [(1, 1)]]
        self.assertTrue(load('codes/14/2').bellman_ford(graph, 0)[1])
        self.assertFalse(load('codes/14/2').bellman_ford([[], [(2, -2)], [(1, 1)]], 0)[1])
        fw = load('codes/14/5').floyd_warshall
        self.assertTrue(fw(1, [(0, 0, -1)])[1])
        self.assertEqual(fw(2, [(0, 1, 2), (0, 1, 9)])[0][0][1], 2)
        self.assertEqual(fw(3, [(1, 2, -10)])[0][0][2], math.inf)
        large = 10**30
        self.assertEqual(fw(2, [(0, 1, large)])[0][0][1], large)
        for key in ('codes/14/2', 'codes/14/3', 'codes/14/4'):
            m = load(key)
            result = m.bellman_ford([[(1, large)], []], 0)[0] if key.endswith('/2') else m.dijkstra([[(1, large)], []], 0)
            self.assertEqual(result, [0, large])

    def test_spanning_trees(self):
        def all_trees(n, edges):
            trees = []
            for ids in itertools.combinations(range(len(edges)), n - 1):
                seen = {0}
                for _ in range(n):
                    for i in ids:
                        _, u, v = edges[i]
                        if u in seen or v in seen:
                            seen.update((u, v))
                if len(seen) == n:
                    trees.append((sum(edges[i][0] for i in ids), set(ids)))
            return trees
        for _ in range(40):
            n = self.rng.randint(2, 5)
            edges = [(self.rng.randint(1, 9), i, i + 1) for i in range(n - 1)]
            edges += [(self.rng.randint(1, 9), u, v) for u in range(n) for v in range(u + 2, n)
                      if self.rng.random() < .4]
            trees = all_trees(n, edges)
            minimum = min(cost for cost, _ in trees)
            self.assertEqual(load('codes/15/1').kruskal(n, edges), minimum)
            minimum_trees = [ids for cost, ids in trees if cost == minimum]
            necessary = set.intersection(*minimum_trees)
            self.assertEqual(load('solutions/15/2').necessary_edges(n, edges),
                             (len(necessary), sum(edges[i][0] for i in necessary)))
            # 原文は(N+1)//2本目を採用する（N=偶数の問題設定では中央値）。
            expected = min(sorted(edges[i][0] for i in ids)[(n + 1) // 2 - 1]
                           for _, ids in trees)
            self.assertEqual(load('solutions/15/1').median_tree(n, edges), expected)
        self.assertEqual(load('codes/15/1').kruskal(4, [(3, 0, 1)]), 3)

    def test_flow_against_all_cuts(self):
        module = load('codes/16/1')
        for _ in range(70):
            n = self.rng.randint(2, 6)
            edges = [(u, v, self.rng.randrange(6)) for u in range(n) for v in range(n)
                     if self.rng.random() < .2]
            # 多重辺も含める。
            edges += [(0, n - 1, self.rng.randrange(6))]
            graph = module.Graph(n)
            for u, v, cap in edges:
                graph.add_edge(u, v, cap)
            for row in graph:
                for edge in row:
                    self.assertIs(graph.reverse_edge(graph.reverse_edge(edge)), edge)
            expected = min(sum(c for u, v, c in edges if mask >> u & 1 and not (mask >> v & 1))
                           for mask in range(1 << n) if mask & 1 and not (mask >> (n - 1) & 1))
            self.assertEqual(module.FordFulkerson().solve(graph, 0, n - 1), expected)
            for v, row in enumerate(graph):
                for edge in row:
                    self.assertGreaterEqual(edge.cap, 0)
                    self.assertEqual(edge.source, v)
                    self.assertEqual(graph.reverse_edge(edge).to, v)
            self.assertEqual(module.FordFulkerson().solve(graph, 0, n - 1), 0)
        graph = module.Graph(2)
        graph.add_edge(0, 1, 10**30)
        self.assertEqual(module.FordFulkerson().solve(graph, 0, 1), 10**30)
        with self.assertRaises(ValueError):
            module.FordFulkerson().solve(module.Graph(1), 0, 0)

    def test_tree_algorithms(self):
        for _ in range(45):
            n = self.rng.randint(1, 9)
            parents = [-1] + [self.rng.randrange(v) for v in range(1, n)]
            edges = [(v, parents[v]) for v in range(1, n)]
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            depth, sizes = load('codes/13/9').tree_info(graph)
            expected_depth = [0] * n
            expected_size = [0] * n
            for v in range(n):
                current = v
                while current != -1:
                    expected_size[current] += 1
                    if current != v:
                        expected_depth[v] += 1
                    current = parents[current]
            self.assertEqual(depth, expected_depth)
            self.assertEqual(sizes, expected_size)
            sets = [mask for mask in range(1 << n)
                    if all(not (mask >> u & 1 and mask >> v & 1) for u, v in edges)]
            weights = [self.rng.randint(-5, 20) for _ in range(n)]
            expected = max(sum(weights[v] for v in range(n) if mask >> v & 1) for mask in sets)
            self.assertEqual(load('codes/18/1').maximum_weight_independent_set(graph, weights), expected)
            self.assertEqual(load('solutions/18/1').maximum_independent_set(graph), max(mask.bit_count() for mask in sets))
            self.assertEqual(load('solutions/18/2').count_independent_sets(graph), len(sets))
        self.assertEqual(load('codes/18/1').maximum_weight_independent_set([[1], [0]], [10**30, 1]), 10**30)
