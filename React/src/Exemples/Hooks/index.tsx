import React from 'react';
import UseStateHook from './UseStateHook';
import UseContextHook from './UseContextHook';
import UseEffectHook from './UseEffectHook';
import UseIdHook from './UseIdHook';
import UseRefHook from './UseRefHook';
import UseMemoHook from './UseMemoHook';
import UseCallBackHook from './UseCallBackHook';
import UseReducerHook from './UseReducerHook';
import CustomHooks from './CustomHooks';

export default function Hooks(): React.ReactElement {
    return (
        <section>
            <h1>This is the Hooks page of the repo.</h1>

            <UseStateHook />
            <UseContextHook />
            <UseEffectHook />
            <UseIdHook />
            <UseRefHook />
            <UseMemoHook/>
            <UseCallBackHook/>
            <UseReducerHook/>
            <CustomHooks/>
        </section>
    )
}