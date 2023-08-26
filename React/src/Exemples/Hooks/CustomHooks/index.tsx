import React from 'react';
import IsOnlineExemple from './IsOnlineExemple';
import Challanges from './Challanges';

export default function CustomHooks(): React.ReactElement {

    return (
        <section>
            <h2>Custom Hooks</h2>
            <IsOnlineExemple />
            <Challanges/>
        </section >
    )
}