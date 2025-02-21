class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        left, right = 2 * node + 1, 2 * node + 2
        self.build(arr, left, l, mid)
        self.build(arr, right, mid + 1, r)
        self.tree[node] = self.tree[left] + self.tree[right]

    def update(self, idx, val, node, l, r):
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        left, right = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self.update(idx, val, left, l, mid)
        else:
            self.update(idx, val, right, mid + 1, r)
        self.tree[node] = self.tree[left] + self.tree[right]

    def query(self, ql, qr, node, l, r):
        if ql > r or qr < l:
            return 0
        if ql <= l and qr >= r:
            return self.tree[node]
        mid = (l + r) // 2
        return self.query(ql, qr, 2 * node + 1, l, mid) + self.query(ql, qr, 2 * node + 2, mid + 1, r)

# Example Usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print(seg_tree.query(1, 3, 0, 0, len(arr) - 1))  # Sum from index 1 to 3
seg_tree.update(2, 6, 0, 0, len(arr) - 1)       # Update index 2 to value 6
print(seg_tree.query(1, 3, 0, 0, len(arr) - 1))  # Updated sum from index 1 to 3
