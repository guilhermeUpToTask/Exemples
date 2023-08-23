import React, { useState } from 'react';
import ConnectionHistory from './ConnectionHistory';

//later on we can send the props to child with a trigger button

export default function UseEffectHook(): React.ReactElement {
    const [connectionName, setConnectionName] = useState<string>('');
    const [connectionValue, setConnectionValue] = useState<number>(0);

    return (
        <section>
            <h2>UseEffectHook</h2>
            <p>
                This is a simple example of the use of the useEffect hook.
            </p>

            <section>
                <label htmlFor={'connectionName'}>
                    Connection Name:
                </label>
                <input
                    type="text"
                    id='connectionName'
                    value={connectionName}
                    onChange={(e) => setConnectionName(e.target.value)}
                    placeholder='write here' />
                <label htmlFor={'connectionName'}>
                    Connection Value:
                </label>
                <input
                    type="number"
                    id='connectionValue'
                    value={connectionValue}
                    onChange={(e) => setConnectionValue(parseInt(e.target.value))}
                    placeholder='write here' />
            </section>
            <ConnectionHistory connectionName={connectionName} connectionValue={connectionValue} />
        </section>
    )
}