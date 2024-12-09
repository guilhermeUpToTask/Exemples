import React from 'react';
import SimpleQueryExemple from './simpleQueryExemple';
import { Typography } from 'antd';
import DynamicQueryExemple from './DynamicQueryExemple';

const { Title } = Typography;

export default function ReactQueryExemples(): React.ReactElement {

    return (
        <section>
            <Title level={2}>React Query Exemples</Title>
            <SimpleQueryExemple/>
            <DynamicQueryExemple/>
        </section>
    )
}