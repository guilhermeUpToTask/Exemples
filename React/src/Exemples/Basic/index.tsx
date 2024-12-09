import React, {useState} from 'react';
import Child from './Child';

export enum Lists {
    TREES = 'Trees', 
    ROCKS =   'Rocks', 
    FLOWERS = 'Flowers'
}

export type ListType = Lists ;

export default function Basic() : React.ReactElement {
    const [list, setList] = useState<ListType>(Lists.TREES);

    const changeList = (listName : ListType) => {
        setList(listName);
    }

    return (
        <>
            <h2>Hello!, this is a simples demonstration of the structure of REACT</h2>
            <h2>List:{list}</h2>
            <Child list={list} changeList={changeList}/>
        </>
    )
}