import React from 'react';
import useFakeDataById from './hooks/usefakeDataById';
import type { fakeDataType } from './fakeFetch';
import { Skeleton, Typography } from 'antd';
import MessageFeedBack from './MessageFeedBack';

const { Title } = Typography;

export default function DynamicQueryExemple(): React.ReactElement {
    const { data: firstData, isLoading: firstIsloading, error: firstError } = useFakeDataById(1);
    const { data: secondData, isLoading: secondIsloading, error: secondError,status } = useFakeDataById(10);

    const renderData = ({ data, isLoading, error }: { data: fakeDataType | undefined, isLoading: boolean, error: Error | null })
        : React.ReactElement => {
        if (isLoading) {
            return <Skeleton active paragraph={false} />;
        } else if (error) {
            return <p>Error: {error.message}</p>;
        } else {
            return <p>Name: {data?.name} with Id: {data?.id}</p>;
        }
    };

    return (
        <section>
            <MessageFeedBack status={status} messagekey={'secondFetch'}/>
            <Title level={3}>Dynamic React Query Exemple</Title>

            {renderData({ data: firstData, isLoading: firstIsloading, error: firstError as Error })}
            <Title level={3}>Exemple With Error:</Title>
            {renderData({ data: secondData, isLoading: secondIsloading, error: secondError as Error })}
        </section>
    );
}