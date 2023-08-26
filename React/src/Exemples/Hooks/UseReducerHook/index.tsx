import React, { useReducer } from 'react';
import counterReducer from './counterReducer';


export default function UseReducerHook(): React.ReactElement {
    const [state, dispatch] = useReducer(counterReducer, 0);

    const handleIncrement = () => {
        dispatch({ type: 'increment', value: 1 });
    }
    const handleDecrement = () => {
        dispatch({ type: 'decrement', value: 1 });
    }
    const handleReset = () => {
        dispatch({ type: 'reset', value: 0 });
    }
    const handleEdit = (value: number) => {
        dispatch({ type: 'edit', value });
    }

    return (
        <section>
            <h2>UseReducerHook</h2>
            <article>
                <h3>Simple Counter:</h3>
                <section>
                    <button onClick={handleDecrement}>Decrement (-)</button>
                    <button onClick={handleReset}>Reset</button>
                    <button onClick={handleIncrement}>Increment (+)</button>
                </section>
                <section>
                    <label htmlFor='edit-input'>Edit</label>
                    <input
                        type="number"
                        id='edit-input'
                        value={state}
                        onChange={(e) => handleEdit(Number(e.target.value))} />
                </section>
                <h3>Counter with useReducer:{state}</h3>
            </article>
        </section>
    )
}