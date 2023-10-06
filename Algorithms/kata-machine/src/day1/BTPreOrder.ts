
function traversal (curr: BinaryNode<number> | null, path: number[]) : number[]{
    //basecase
    if (!curr){
        return path;
    }

    //recursive steps

    //pre
    path.push(curr.value);

    //recurse
    traversal(curr.left, path);
    traversal(curr.right, path);

    //post
    return path;

}

export default function pre_order_search(head: BinaryNode<number>): number[] {
    return traversal(head, []);
}