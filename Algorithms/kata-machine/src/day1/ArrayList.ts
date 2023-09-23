import { NewLineKind } from "typescript";



export default class ArrayList<T> {
    public length: number;
    private capacity: number;
    private arr: Array<T>;


    constructor(size:number) {
        this.capacity = size*2;
        this.length = size;
        this.arr = new Array<T>(this.capacity);
    }


    private grow(): void {
        const newCapacity = this.capacity * 2;
        const newArr: Array<T> = new Array<T>(newCapacity);

        for (let i = 0; i < this.length; i++) {
            newArr[i] = this.arr[i];
        }

        this.arr = newArr;
        this.capacity = newCapacity;
    }

    prepend(item: T): void { // this need a shifting
        if (this.length === this.capacity) {
            this.capacity *= 2;
        }

        const newArr = new Array<T>(this.capacity);
        newArr[0] = item;

        for (let i = 1; i <= this.length; i++) {
            newArr[i] = this.arr[i-1];
        }
        this.arr = newArr;
        this.length++;
    }

    insertAt(item: T, idx: number): void {
        if (idx > this.length){
            this.capacity*= 2;
        }

        const temp =  this.arr[idx];
        const newArr = new Array<T>(this.capacity);

        for(let i = 0; i < idx; i++){
            newArr[i] = this.arr[i];
        
        }
        newArr[idx] = item;
        for (let i = idx; i < this.length; i++) {
            newArr[i+1] = this.arr[i];
        }
        this.arr = newArr;
        this.length++;
    }

    append(item: T): void {
        if (this.length === this.capacity) {
            this.grow();
        }
        this.arr[this.length] = item;
        this.length++;
    }

    remove(item: T): T | undefined {
        const newArr = new Array<T>(this.capacity);
        let itemFound = undefined;
        for (let i = 0; i < this.length; i++) {
            if (this.arr[i] !== item) {
                newArr[i] = this.arr[i];
            } else {
                itemFound = this.arr[i];
            }
        }
        this.arr = newArr;
        this.length--;
        return itemFound;
    }

    get(idx: number): T | undefined {
        if (idx < 0 || idx >= this.length) {
            return undefined;
        } else {
            return this.arr[idx];
        }
    }

    removeAt(idx: number): T | undefined {
        if (idx < 0 || idx >= this.length) {
            return undefined;
        }
        const item = this.arr[idx];

        for (let i = idx; i < this.length; i++) {
            this.arr[i] = this.arr[i + 1];
        }

        this.length--;
        return item;

    }
}