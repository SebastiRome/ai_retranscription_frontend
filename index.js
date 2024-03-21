import React from "react";
import ReactDOM from 'react-dom';

function App() {
    return(
        <div>
            <h1>Dernière consultation</h1>
            <iframe title="Title" src="https://docs.google.com/document/d/e/2PACX-1vS-vHhxho9yOo62SpJqHh6739a8ilWqKDs55btepnNVch6b1rp3l2BkHo3mS2lb0ndKoXKTaX957mfQ/pub?embedded=true"></iframe>
        </div>
    );
}

export default App

ReactDOM.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>,
    document.getElementById('root')
  );
