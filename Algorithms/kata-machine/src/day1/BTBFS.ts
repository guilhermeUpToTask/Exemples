export default function bfs(head: BinaryNode<number>, needle: number): boolean {
    const q : (BinaryNode<number> | null)[] = [head];

    while (q.length) {
        const curr = q.shift() as BinaryNode<number> | undefined | null; // pop the current node

        if (!curr){
            continue;
        }

        if (curr.value === needle) {
            return true;
        }

        q.push(curr.left);
        q.push(curr.right);
    }

    return false;  // not found

}

