import React, { useState, useCallback } from 'react';
import CallBackForm from './CallBackForm';
type Theme = "white" | "black";

export default function UseCallBackHook(): React.ReactElement {

    const [theme, setTheme] = useState<Theme>("white");
    const [exempleState] = useState<string>("exemple");

    const changeTheme = () => {
        setTheme(theme === "white" ? "black" : "white");
    }

    const FormSectionStyle: React.CSSProperties = {
        border: '1px solid black',
        borderRadius: '5px',
        padding: '10px',
        margin: '10px',
        boxSizing: 'border-box',
        backgroundColor: theme,
        color: theme === "white" ? "black" : "white"
    }


    const onSubmitHandler = (values: { name: string }) => {
        console.log(exempleState, "Form Submitted:", values);
    }

    const onSubmitHandlerWithCallBack = useCallback((values: { name: string }) => {
        console.log(exempleState, "Form Submitted:", values);
    }, [exempleState]);


    return (
        <section>
            <h2>UseCallBackHook</h2>
            <p>
                Caching a function with useCallback  is only valuable in a few cases:
            </p>
            <ul>
                <li>
                    You pass it as a prop to a component wrapped in memo.
                    You want to skip re-rendering if the value hasn’t changed. Memoization lets your component
                    re-render only if dependencies changed.
                </li>
                <li>
                    The function you’re passing is later used as a dependency of some Hook.
                    For example, another function wrapped in useCallback depends on it,
                    or you depend on this function from useEffect.
                </li>
            </ul>
            <h3>open the  Console.Log to see if a ReRender of Form happens</h3>
            <button onClick={changeTheme}>Change Theme</button>

            <section style={FormSectionStyle}>
                <h3>Form without use CallBack - Id 1</h3>
                <CallBackForm onSubimitFunction={onSubmitHandler} id={'id:1'} />
                <h3>Form with use CallBack - id 2</h3>
                <CallBackForm onSubimitFunction={onSubmitHandlerWithCallBack} id={'id:2'} />
            </section>
        </section>
    )
}