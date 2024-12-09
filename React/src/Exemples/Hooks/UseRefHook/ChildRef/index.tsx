import React, {forwardRef} from 'react';

const ChildRef = forwardRef((_, ref: React.ForwardedRef<HTMLHeadingElement>): React.ReactElement => {

    
    const containerSection : React.CSSProperties = {
        padding: '3rem',
        marginTop:'2rem',
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        height: '100vh',
        boxSizing:  'border-box',
        border:'1px solid black',
    }

    const refSection : React.CSSProperties = {
        padding: '1rem',
        boxSizing: 'border-box',
        border:'1px solid black',
        backgroundColor:'red',
    }

    return (
        <section style={containerSection}>
            <section style={refSection}>
                <h3 ref={ref}>Child Ref</h3>
            </section>
        </section>

    )
})

export default ChildRef;