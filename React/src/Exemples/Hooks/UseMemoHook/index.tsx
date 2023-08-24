import React from 'react';




export default function UseMemoHook(): React.ReactElement {
    return (
        <section>
            <h2>UseMemoHook</h2>
            <p>useMemo is a React Hook that lets you cache the result of a calculation between re-renders.</p>
            <section>
            <h2>List of Trees</h2>
            <button>Change Theme</button>
            <h3>Was re-render:</h3>
            <article> 
                <h3>Filter List</h3>
                <button>All</button>
                <button>Only Fruit trees</button>
                <button>Only Deciduous Trees</button>
                <button>Only Conifer Trees</button>
            </article>
            <article>
                <ul>
                </ul>
            
            </article>
            </section>
        </section>
    )
}