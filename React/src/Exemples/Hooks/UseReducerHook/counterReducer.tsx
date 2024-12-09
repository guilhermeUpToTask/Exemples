export type CounterActtion = {
    type: 'decrement' | 'increment' | 'reset' | 'edit';
    value: number;
}

export default function counterReduce(state: number, action: CounterActtion): number {
    switch (action.type) {
        case 'decrement':
            return state - action.value;
        case 'increment':
            return state + action.value;
        case 'reset':
            return 0;
        case 'edit':
            return action.value;
        default:
            throw new Error();
    }
}

