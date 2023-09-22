type Node<T> = {
    prev: Node<T> | undefined;
    item: T;
}

export default class Stack<T> {
    public length: number;
    head: Node<T> | undefined;
    tail: Node<T> | undefined;


    constructor() {
        this.length = 0;
        this.head = this.tail = undefined;

    }

    push(item: T): void {
        const newNode: Node<T> = { item, prev: undefined }
        if (this.tail) {
            newNode.prev = this.tail;
            this.tail = newNode;
        } else {
            this.head = this.tail = newNode;
        }
        this.length++;
    }

    pop(): T | undefined {
        if (this.length == 1) {
            const item = this.tail?.item;
            this.head = this.tail = undefined;
            this.length--;
            return item;
        }else if (this.tail) {
            const item = this.tail?.item;
            this.tail = this.tail.prev;
            this.length--;
            return item;
        }else{
            return undefined;
        
        }
    }

    
    peek(): T | undefined {
        return this.head?.item;
    }
}