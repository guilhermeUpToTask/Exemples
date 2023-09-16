
export default function memorySize() {

    const arr = new ArrayBuffer(6);

    console.log('buffer of 6 units of memory', arr);

    const arr8 = new Uint8Array(arr);

    console.log('Array of 6 elements with lenght of 8 bytes each', arr8);

    arr8[0] = 45;
    console.log('element 0', arr8[0]);

    console.log('memory:', arr);
    console.log('array:', arr8);

    arr8[2] = 45;
    console.log('element 2', arr8[2]);

    console.log('memory:', arr);
    console.log('array:', arr8);


    console.log('Now lets change to 16byte');

    const arr16 = new Uint16Array(arr);
    console.log('Array of 3 elements with lenght of 16 bytes each, using same space', arr16);

    arr16[2] = 0X4545;
    console.log('element 2', arr16[2]);

    console.log('memory:', arr);
    console.log('array:', arr16);
}

memorySize();
