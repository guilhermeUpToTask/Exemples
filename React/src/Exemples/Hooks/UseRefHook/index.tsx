import React, { useRef } from 'react';
import ChildRef from './ChildRef';

export default function UseRefHook(): React.ReactElement {
    const valueRef = useRef<number>(0);
    const elementRef = useRef<HTMLHeadingElement>(null);
    const [elName, setElName] = React.useState<string>('');

    const increaseCount = () => {
        valueRef.current++;
        window.alert(valueRef.current);

    }

    const scrollElement = () => {
        elementRef.current?.scrollIntoView({
            behavior: 'smooth',
            block: 'center',
            inline: 'center'
        });
        setElName(elementRef.current?.textContent ?? '');
    }

    return (
        <section>
            <h2>UseRefHook</h2>

            <article>
                <h3>UseRefHook to Store a Count Value</h3>
                <button onClick={increaseCount}>Click Me to increase the count</button>
            </article>
            <article>
                <h3>UseRefHook to Store a ref from a element</h3>
                <h3>Element Name: {elName}</h3>
                <button onClick={scrollElement}>Click Me to scroll to the element</button>
            </article>
            <ChildRef ref={elementRef} />
        </section>
    )
}