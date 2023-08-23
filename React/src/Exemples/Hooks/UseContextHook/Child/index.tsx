import React from 'react';
import NestedChild from './NestedChild';

export default function ContextChild(): React.ReactElement {
    return (
        <section style={{ border: '1px solid red', padding:'1rem' }}>
            <h2>Context Child</h2>
            <NestedChild />
        </section>
    )
}