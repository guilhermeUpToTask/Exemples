import React, { useState, useMemo } from 'react';
import type { Tree } from './treesList';
import treeList from './treesList';
import TreeListDisplay from './TreeListDisplay';

type Theme = "white" | "black";

type Filter = "all" | "fruit" | "deciduous" | "conifer";

export default function UseMemoHook(): React.ReactElement {
    const [theme, setTheme] = useState<Theme>("white");
    const [filter, setFilter] = useState<Filter>("all");
    const countReRender = React.useRef<number>(0);

    const changeTheme = () => {
        setTheme(theme === "white" ? "black" : "white");
    }


    const filterTreesByType = (filter: Filter, treeList: Tree[]): Tree[] => {
        countReRender.current++;
        console.log('Filter Trees is being calculed:',countReRender.current);
        if (filter === "all") {
            return treeList;
        }
        return treeList.filter(tree => {
            return tree.type === filter;
        });
    }

    const visibleTrees = useMemo(() => {
        return filterTreesByType(filter, treeList)
    }
    , [filter]);

    const listSectionStyle: React.CSSProperties = {
        border: '1px solid black',
        borderRadius: '5px',
        padding: '10px',
        boxSizing: 'border-box',
        backgroundColor: theme,
        color: theme === "white" ? "black" : "white"
    }

    return (
        <section>
            <h2>UseMemoHook</h2>
            <p>useMemo is a React Hook that lets you cache the result of a calculation between re-renders.</p>
            <section style={listSectionStyle}>
                <h2>List of Trees</h2>
                <h3>open the  Console.Log to see if a calculation of filterTreesByType happens</h3>
                <button onClick={changeTheme}>Change Theme</button>
                <article>
                    <h3>Filter List</h3>
                    <button onClick={() => setFilter("all")}>All</button>
                    <button onClick={() => setFilter("fruit")}>Only Fruit trees</button>
                    <button onClick={() => setFilter("deciduous")}>Only Deciduous Trees</button>
                    <button onClick={() => setFilter("conifer")}>Only Conifer Trees</button>
                </article>
                <article>
                    <TreeListDisplay treeList={visibleTrees} />
                </article>
            </section>
        </section>
    )
}