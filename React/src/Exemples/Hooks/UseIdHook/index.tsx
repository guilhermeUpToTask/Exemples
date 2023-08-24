import React, { useId } from 'react';

export default function UseIdHook() : React.ReactElement {

return (
    <section>
        <h2>UseIdHook</h2>
        <p>
            UseIdHook Generate a unique Id for usage
        </p>
        <ul>
            <li>Id: <strong>{useId()}</strong></li>
            <li>Id: <strong>{useId()}</strong></li>
            <li>Id: <strong>{useId()}</strong></li>
        </ul>
    </section>
)
}