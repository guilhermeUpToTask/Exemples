import React from "react";
import type { Tree } from "./treesList";

interface ITreeListDisplayProps {
    treeList: Tree[];
}

export default function TreeListDisplay (props: ITreeListDisplayProps) : React.ReactElement {
    
    

    const trees = props.treeList.map((tree, index) => {
        return (
            <li key={index}>
                {tree.name}
            </li>
        )
    });

    return (
            <ul>
                {trees}
            </ul>
    )
}