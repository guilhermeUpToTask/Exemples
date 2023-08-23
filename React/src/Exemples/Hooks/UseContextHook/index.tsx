import React, { createContext } from 'react';
import ContextChild from './Child';

export const ValueContext = createContext<number>(0);


export default function UseContextHook(): React.ReactElement {
    const value : number = 256;

    return (
        <section>
            <h2>UseContextHook</h2>
            <p>
                This is a simple example of the use of the useContext hook.
            </p>
            <p>
                Value That Is Passed down using the useContext hook: <strong>{value}</strong>
            </p>
            <ValueContext.Provider value={value}>
            <ContextChild/>
            </ValueContext.Provider>
        </section>
    )
}