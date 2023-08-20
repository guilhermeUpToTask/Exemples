import React from 'react';
import { ListType } from '..';


interface IButtonProps {
    listName: ListType;
    click: (listName: ListType) => void;
}

export default function Button(props: IButtonProps) : React.ReactElement {
    return (
        <button onClick={() => props.click(props.listName)}>
            {props.listName}
        </button>
    )
}