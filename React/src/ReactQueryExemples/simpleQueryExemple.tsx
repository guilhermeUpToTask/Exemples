import React from 'react';
import { useQuery } from 'react-query'
import { fakeFetchData } from './fakeFetch';
import type { fakeDataType } from './fakeFetch';
import { Typography } from 'antd';

const { Title } = Typography;

export default function SimpleQueryExemple(): React.ReactElement {
    const { data, isLoading, error } = useQuery<fakeDataType[]>('fakeDatas', fakeFetchData);


    const displayData = () => {
        return data?.map((item) => {
            return <p key={item.id}>{item.name}</p>
        })
    }

    const renderData = () => {
        if (isLoading) {
            return <p>Loading...</p>
        }
        else if (error) {
            return <p>Error... {(error as Error).message}</p>
        } else {
            return displayData()
        }

    }
    return (
        <section>
            <Title level={3}> Simple React Query Exemple</Title>
            {renderData()}
        </section>
    )
}