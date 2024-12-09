import { message } from 'antd';
import { ArgsProps } from 'antd/es/message';
import React, { useEffect } from 'react';

type MessageStatus = 'loading' | 'success' | 'error' | 'idle';
type MessageMapType = { [key: string]: ArgsProps };


interface IMessageFeedBackProps {
    status: MessageStatus,
    messagekey: string
}

export default function MessageFeedBack(props: IMessageFeedBackProps): React.ReactElement {
    const [messageApi, contextHolder] = message.useMessage();


    useEffect(() => {
        const messageMap: MessageMapType = {
            ['loading']: {
                key: props.messagekey,
                type: 'loading',
                content: 'Loading...'
            },
            ['success']: {
                key: props.messagekey,
                type: 'success',
                content: 'Sucessfuly fetched the data'
            },
            ['error']: {
                key: props.messagekey,
                type: 'error',
                content: 'Error while fetching data',
            },
        }

        if (messageMap[props.status]) {
            messageApi.open(messageMap[props.status]);
        }
    }, [props.status, props.messagekey, messageApi,]);


    return (
        <>
            {contextHolder}
        </>
    )
}

