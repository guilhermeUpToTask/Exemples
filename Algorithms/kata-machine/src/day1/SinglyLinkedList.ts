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
                    this.head = currentNode?.next;
                    if (this.length === 1) {
                        this.tail = undefined;
                    }
                } else if (previousNode) {
                    if (i === this.length - 1) {
                        this.tail = previousNode;
                        previousNode.next = undefined;
                    } else {
                        previousNode.next = currentNode?.next;
                    }
                }

                this.length--;

                //clear node
                currentNode = undefined;
                
                return item;
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
        let item: T | undefined = undefined;


        if (idx === 0) {
            if (this.length === 1) {
                this.tail = undefined;
            }
            item = this.head?.item;
            this.head = this.head?.next;

            //clear node
            currentNode = undefined;

            this.length--;
            return item;
        }


        for (let i = 0; i < this.length; i++) {

            if (i === idx) {
                if (previousNode) {
                    if (idx === this.length - 1) {
                        this.tail = previousNode;
                        previousNode.next = undefined;
                    } else {
                        previousNode.next = currentNode?.next;
                    }
                    item = currentNode?.item;

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

}