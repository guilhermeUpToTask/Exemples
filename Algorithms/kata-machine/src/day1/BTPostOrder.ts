function traversal (curr: BinaryNode<number> | null, path: number[]) : number[]{
    //base case
    if (!curr){
        return path;
    }

    //recursive steps

    //pre

    //recurse
    traversal(curr.left, path);
    traversal(curr.right, path);

    //post
    path.push(curr.value);
    return path;

}

export default function post_order_search(head: BinaryNode<number>): number[] {
    return traversal(head, []);
}