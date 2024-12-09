import React from 'react';
import type { ListType } from '..';
import { Lists } from '..';

interface IListProps {
    list: ListType;
}

export default function functionName(props: IListProps): React.ReactElement {


    const ListsMap: { [key in ListType]: string[] } = {
        [Lists.TREES]:
            [
                'Oak',
                'Maple',
                'Pine',
                'Spruce',
                'Cedar',
                'Birch',
                'Redwood',
                'Willow',
                'Elm',
                'Fir',
                'Ash',
                'Beech',
                'Poplar',
                'Cypress',
                'Palm',
                'Cherry',
                'Apple',
                'Pear',
                'Orange',
                'Lemon'],
        [Lists.ROCKS]:
            [
                'Granite',
                'Marble',
                'Slate',
                'Limestone',
                'Sandstone',
                'Basalt',
                'Quartzite',
                'Shale',
                'Gneiss',
                'Obsidian',
                'Pumice',
                'Chalk',
                'Flint',
                'Mica',
                'Gypsum',
                'Travertine',
                'Schist',
                'Dolomite',
                'Peridotite',
                'Rhyolite'
            ],
        [Lists.FLOWERS]: [
            'Rose',
            'Tulip',
            'Sunflower',
            'Lily',
            'Daisy',
            'Orchid',
            'Carnation',
            'Hibiscus',
            'Peony',
            'Daffodil',
            'Crocus',
            'Lavender',
            'Iris',
            'Chrysanthemum',
            'Gerbera',
            'Hyacinth',
            'Columbine',
            'Snapdragon',
            'Gladiolus',
            'Anemone'
        ],
    }

    const items = ListsMap[props.list].map ((item, index) => {
        return <li key={index} >{item}</li>
    });

    return (
        <ul>
            {items}
        </ul>
    )
}