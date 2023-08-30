import React, { useState, useCallback, useEffect } from 'react';
import { Typography, Skeleton } from 'antd';

export default function SkeletonLoader(): React.ReactElement {
    const [isLoading, setIsLoading] = useState(true);

    const switchIsLoading = useCallback(() => {
        const interval = setInterval(() => {
            setIsLoading(prevLoading => !prevLoading);
        }, 3000);

        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        const clearSwitchIsLoading = switchIsLoading();
        return () => clearSwitchIsLoading();
    }, [switchIsLoading]);

    return (
        <>
            <Typography.Title level={2}>
                Simple SkeletonExemple
            </Typography.Title>
            <article style={{ display: 'flex', justifyContent: 'center' }}>
                <Skeleton
                    title={true}
                    active
                    paragraph={false}
                    loading={isLoading}
                    style={{ width: '50%' }}
                >
                    <Typography.Title level={3}>
                        This is a exemple of a Loading Text
                    </Typography.Title>
                </Skeleton>
            </article>

        </>
    )
}