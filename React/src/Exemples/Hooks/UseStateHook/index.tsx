import React, { useState } from 'react';

export default function UseStateHook(): React.ReactElement {
    const [inputValue, setInputValue] = useState<string>('');


    return (
        <section>
            <h2>UseState Hook</h2>
            <p>
                This is a simple example of the use of the useState hook.
            </p>
            <section>
                <label htmlFor={'inputText'}>
                    <p>
                        The input value is: <strong>{inputValue}</strong>
                    </p>
                </label>

                <input
                    type="text"
                    id='inputText'
                    value={inputValue}
                    placeholder='write here'
                    onChange={(e) => setInputValue(e.target.value)}
                >
                </input>

            </section>
        </section>
    )
}