import React from 'react';
import type { ListType } from '..';
import { Lists } from '..';
import Button from './Button';
import ListsDisplay from './ListsDisplay';
import '../basic.css';




interface IChildProps {
    list: ListType;
    changeList: (listName: ListType) => void;
}

export default function Child(props: IChildProps): React.ReactElement {
    return (
        <section className='BasicSection'>
            <ListsDisplay list={props.list} />
            <article className='BasicArticle'>
                <h2>Click on the button to change the list to display</h2>
                <Button listName={Lists.FLOWERS} click={props.changeList} />
                <Button listName={Lists.ROCKS} click={props.changeList} />
                <Button listName={Lists.TREES} click={props.changeList} />
            </article>
        </section>
    )
}