import React from 'react';
import { useContext } from 'react';
import { ValueContext } from '../..';

export default function NestedChild () : React.ReactElement {
    const value: number = useContext(ValueContext);
    
    return (
        <section style={{border: '1px solid green'}}>
            <h2>Nested Child</h2>
            <p>
                Value That was get using the useContext hook: <strong>{value}</strong>
            </p>
        </section>
    )
}