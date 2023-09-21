type Node<T> = {
    item: T;
    next: Node<T> | undefined;
}

export default class SinglyLinkedList<T> {
    public length: number;
    public head: Node<T> | undefined;
    public tail: Node<T> | undefined;


    constructor() {
        this.length = 0;
        this.head = undefined;
        this.tail = undefined;
    }

    prepend(item: T): void {
        if (this.length === 0) {
            this.append(item);

        } else {
            this.length++;
            const newNode: Node<T> = { item, next: this.head }
            this.head = newNode;
        }
    }

    insertAt(item: T, idx: number): void {
        let currentNode = this.head;
        let previousNode = undefined;

        for (let i = 0; i < this.length; i++) {
            if (i === idx) {
                if (i === 0) {
                    this.prepend(item);
                    break;
                } else if (i === this.length - 1) {
                    this.append(item);
                    break;
                } else if (previousNode) {
                    this.length++;

                    const newNode: Node<T> = { item, next: currentNode }
                    previousNode.next = newNode;
                    break;
                }
            }

            previousNode = currentNode;
            currentNode = currentNode?.next;

        }
    }

    append(item: T): void {

        const newNode: Node<T> = { item, next: undefined }

        if (!this.head && !this.tail) {
            this.head = this.tail = newNode;
            this.length++;
        }
        else if (this.tail) {
            this.tail.next = newNode;
            this.tail = newNode;
            this.length++;
        }
    }

    remove(item: T): T | undefined {


        let currentNode = this.head;
        let previousNode = undefined;

        for (let i = 0; i < this.length; i++) {

            if (currentNode?.item === item) {
                if (i === 0) {
                    this.head = currentNode.next;
                    //free node

                    currentNode = undefined;
                    this.length--;
                    return item;

                } else if (i === this.length - 1 && previousNode) {
                    this.tail = previousNode;
                    previousNode.next = undefined;
                    // clear node
                    currentNode = undefined;

                    this.length--;
                    return item;

                } else if (previousNode) {
                    const temp = currentNode;
                    previousNode.next = currentNode.next;

                    //clear node
                    currentNode = undefined;

                    this.length--;
                    return item;
                }
            }
            previousNode = currentNode;
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
        let previousNode = undefined;



        for (let i = 0; i < this.length; i++) {

            if (i === idx) {

                if (i == 0) {

                    this.head = currentNode?.next;
                    //free node
                    const item = currentNode?.item;

                    if (this.tail === currentNode) {
                        this.tail = undefined;
                    }
                    currentNode = undefined;

                    this.length--;
                    return item;

                } else if (i === this.length - 1 && previousNode) {
                    this.tail = previousNode;
                    previousNode.next = undefined;

                    //free node 
                    const item = currentNode?.item;
                    currentNode = undefined;

                    this.length--;
                    return item;

                } else if (previousNode) {
                    previousNode.next = currentNode?.next;

                    //free node
                    const item = currentNode?.item;
                    currentNode = undefined;

                    this.length--;
                    return item;
                }
            }
            previousNode = currentNode;
            currentNode = currentNode?.next;

        }

        return undefined;
    }

}