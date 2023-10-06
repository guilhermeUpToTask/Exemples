function traversal (curr: BinaryNode<number> | null, path: number[]) : number[]{
    //basecase
    if (!curr){
        return path;
    }

    //recursive steps

    //pre

    //recurse
    traversal(curr.left, path);
    path.push(curr.value);
    traversal(curr.right, path);

    //post
    return path;

}


export default function in_order_search(head: BinaryNode<number>): number[] {
    return traversal(head, []);
}