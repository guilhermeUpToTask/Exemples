
export type fakeDataType = {
    id: number;
    name: string;
}

const fakeData: fakeDataType[] = [
    { id: 1, name: 'Example Data' },
    { id: 2, name: 'Example 2 Data' },
    { id: 3, name: 'Another Exemple' },
    { id: 4, name: 'ThirdExemple' }
]


export const fakeFetchData = async (): Promise<fakeDataType[]> => {
    return new Promise((resolve) => {
        setTimeout(() => {
            const data = fakeData;
            resolve(data);
        }, 2000);
    })
}

export const fakeFetchDataById = async (id: number): Promise<fakeDataType> => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = fakeData.find((item) => item.id === id);
            if (!data) {
                reject(new Error('Data not found'));
            } else {
                resolve(data);
            }
        }, 2000);
    })
}
