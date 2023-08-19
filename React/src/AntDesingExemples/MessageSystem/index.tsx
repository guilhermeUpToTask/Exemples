import React from 'react';
import { Button, message, Space, Typography } from 'antd';

const { Title } = Typography;

export default function MessageSystem(): React.ReactElement {
    const [messageApi, contextHolder] = message.useMessage();
    const [isLoading, setIsLoading] = React.useState(false);
    const [isAsyncLoading, setIsAsyncLoading] = React.useState(false);

    // Messages Types
    const success = (key?: string) => {
        messageApi.open({
            key,
            type: 'success',
            content: 'This is a success message',
        });
    };

    const error = (key?: string) => {
        messageApi.open({
            key,
            type: 'error',
            content: 'This is an error message',
        });
    };

    const warning = (key?: string) => {
        messageApi.open({
            key,
            type: 'warning',
            content: 'This is a warning message',
        });
    };

    const loading = (key?: string) => {
        messageApi.open({
            key,
            type: 'loading',
            content: 'Sending Call'
        })
    }

    // Simulete Simuntaneos Message
    const simulateLoading = (messageType: 'success' | 'error') => {
        const key: string = messageType + 'SimuntaniusKey';
        setIsLoading(true);
        loading(key);

        setTimeout(() => {
            if (messageType === 'success') {
                success(key);
            } else {
                error(key);
            }

            setIsLoading(false);

        }, 1000)
    }

    // Simulate Async Simuntaneos Message
    const simulateAsyncLoading = async () => { 
        loading('async');
        setIsAsyncLoading(true);
        await asyncCall();
        success('async');
        setIsAsyncLoading(false);
    }
    const asyncCall = async (): Promise<{ id: number, name: string }> => {
        return new Promise((resolve) => {
            setTimeout(() => {
                const data = { id: 1, name: 'Example Data' };
                resolve(data);
            }, 1000);
        });
    }


    return (
        <>
            {contextHolder}
            <Title level={1}>Message System</Title>

            <Title level={2}>Simples Message Call</Title>
            <Space>
                <Button onClick={() => success()}>Success</Button>
                <Button onClick={() => error()}>Error</Button>
                <Button onClick={() => warning()}>Warning</Button>
            </Space>

            <Title level={2}>Sequential Message Call</Title>
            <Space>
                <Button loading={isLoading} onClick={() => simulateLoading('success')}>Success Call</Button>
                <Button loading={isLoading} onClick={() => simulateLoading('error')}>Error Call</Button>
                <Button loading={isAsyncLoading} onClick={simulateAsyncLoading}>Asycn Call</Button>
            </Space>
        </>
    );
}
