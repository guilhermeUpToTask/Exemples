
export function createConnection(name: string, value: number) {
    const connect = () => {
        return `
        Connected to the external system: ${name} with value: ${value}
        `;
    }

    const disconnect = () => {
        return `
        Disconnected to the external system: ${name} with value: ${value}
        `;
    }
    return {
        connect,
        disconnect,
    }
}