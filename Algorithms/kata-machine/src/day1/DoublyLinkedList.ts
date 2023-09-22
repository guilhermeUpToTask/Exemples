type Node<T> = {
    prev: Node<T> | undefined;
    next: Node<T> | undefined;
    item: T;
}


export default class DoublyLinkedList<T> {
    public length: number;
    public head: Node<T> | undefined;
    public tail: Node<T> | undefined;


    constructor() {
        this.length = 0;
        this.head = this.tail = undefined;
    }

    prepend(item: T): void {
        if (this.length === 0) {
            this.append(item);
        } else if (this.head) {
            const newNode: Node<T> = { item, prev: undefined, next: undefined }
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode;
            this.length++;
        }
    }

    insertAt(item: T, idx: number): void {
        const newNode: Node<T> = { item, prev: undefined, next: undefined }

        if (idx === 0) {
            this.prepend(item);
        } else if (idx === this.length - 1) {
            this.append(item);
        } else {

            if (this.head) {
                const currentNode: Node<T> = this.head;
                for (let i = 0; i < this.length; i++) {
                    if (i === idx) {
                        if (currentNode.prev) {
                            currentNode.prev.next = newNode; // set the prev node next to new node
                            newNode.prev = currentNode.prev;
                            currentNode.prev = newNode;
                            newNode.next = currentNode;
                            this.length++;
                        }
                    }
                }
            }

        }

    }

    append(item: T): void {
        const newNode: Node<T> = { item, prev: undefined, next: undefined }

        if (!this.tail && !this.head) {
            this.head = this.tail = newNode;
        } else if (this.tail) {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }

        this.length++;
        console.log(this.length);
        console.log('2', this.get(2));
    }


    remove(item: T): T | undefined {
        let currentNode = this.head;
        for (let i = 0; i < this.length; i++) {
            if (currentNode?.item === item) {
                if (i === 0) {
                    if (this.length === 1) {
                        this.tail = undefined;
                    }
                    this.head = currentNode?.next;
                    if (this.head) {
                        this.head.prev = undefined;
                    }
                } else if (i === this.length - 1) {
                    if (currentNode.prev) {
                        this.tail = currentNode.prev;
                        this.tail.next = undefined;
                    }

                } else if (currentNode.prev && currentNode.next) {
                    const prevNode = currentNode.prev;
                    prevNode.next = currentNode.next;
                    currentNode.next.prev = prevNode;
                }

                currentNode = undefined;
                this.length--;
                return item;

            }
            currentNode = currentNode?.next;
        }

        return undefined;
    }




    get(idx: number): T | undefined {
        let currentNode = this.head;

        for (let i = 0; i < this.length; i++) {
            if (i === idx) {
                return currentNode?.item;
            }

            currentNode = currentNode?.next;
        }

        return undefined;
    }


    removeAt(idx: number): T | undefined {

        let currentNode = this.head;
        let item: T | undefined = undefined;

        if (idx === 0 && this.head) {
            return this.remove(this.head.item);
        } else if (idx === this.length - 1 && this.tail) {
            return this.remove(this.tail.item);
        } else {

            for (let i = 0; i < this.length; i++) {
                if (i === idx && currentNode) {
                    if (currentNode.prev && currentNode.next) {
                        const prevNode = currentNode.prev;
                        prevNode.next = currentNode.next;
                        currentNode.next.prev = prevNode;
                    }
                    item = currentNode.item;
                    currentNode = undefined;
                    this.length--;
                    return item;
                }
                currentNode = currentNode?.next;
            }

            return undefined;
        }
    }

}