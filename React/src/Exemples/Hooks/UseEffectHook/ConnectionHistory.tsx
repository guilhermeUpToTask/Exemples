import React, { useEffect, useState } from 'react';
import { createConnection } from './externalSystem';

interface IConnectionHistoryProps {
    connectionName: string;
    connectionValue: number;
}


export default function ConnectionHistory(props: IConnectionHistoryProps): React.ReactElement {
    const [connectHistory, setConnectHistory] = useState<string[]>([]);


    useEffect(() => {

        const connection = createConnection(props.connectionName, props.connectionValue);
        setConnectHistory(prevConnectHistory => [...prevConnectHistory, connection.connect()]);

        return () => {
            setConnectHistory(prevConnectHistory => [...prevConnectHistory, connection.disconnect()]);
        }
    }
        , [props.connectionName, props.connectionValue]);

    const displayHistory = () => {
        return connectHistory.map((returnValue, index) => {
            return <p key={index}>{returnValue}</p>
        });
    }
    return (
        <section>
            <h3>Connection History</h3>

            <article style={{ border: '1px solid black', padding: '10px' }}>
                {displayHistory()}
            </article>

        </section>
    )
}