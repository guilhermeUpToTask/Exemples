import React from 'react';
import useIsOnline from './Hooks/useIsOnline';
export default function IsOnlineExemple(): React.ReactElement {
    const isOnline = useIsOnline();


    return (
        <article>
            <h3>This is a custom hooks example.</h3>
            <p>Its shows if User have internet connection or not.</p>
            <p>  Is User online? <strong>{isOnline ? 'Yes' : 'No'}</strong></p>
        </article>
    )
}