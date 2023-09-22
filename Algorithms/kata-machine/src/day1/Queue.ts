type Node<T> = {
    next: Node<T> | undefined;
    item: T;
}

export default class Queue<T> {
    public length: number;
    public tail: Node<T> | undefined;
    public head: Node<T> | undefined;

    constructor() {
        this.length = 0;
        this.tail = undefined;
    }

    enqueue(item: T): void {
        const newNode: Node<T> = { item, next: undefined }

        if (!this.head && !this.tail) {
            this.head = this.tail = newNode;

        } else if (this.tail) {
            this.tail.next = newNode;
            this.tail = newNode;
        }

        this.length++;

    }

    deque(): T | undefined {
        const item = this.head?.item;
        if (this.head) {
            this.length--;
        }
        this.head = this.head?.next;
        return item;


    }
    peek(): T | undefined {
        return this.tail?.item;
    }
}