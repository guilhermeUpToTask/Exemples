import React from 'react';

interface ICallbackFormProps {
    onSubimitFunction: (values:{name: string}) => void;
    id: string;
}

//form is being memoize so the submit function must be wrapped inside a callbackFunction

const CallBackForm = React.memo((props: ICallbackFormProps) : React.ReactElement =>{
    const countReRender = React.useRef(0);
    const [name, setName] = React.useState('');

    console.log(props.id, ' Form CallBackForm Being Rendered:',countReRender.current++);
    
    
    return (
        <form onSubmit={
            (e) => {
                e.preventDefault();
            props.onSubimitFunction({name})
            }
        }>
            <input type="text" name="name" onChange={(e) => setName(e.target.value)} value={name}/>
            <input type="submit" value="Submit" />
        </form>
    )
});

export default CallBackForm