import React from 'react';
import ReactDOM from 'react-dom';
import { Viewer } from 'react-doc-viewer';

class Titre extends React.Component {
    render() {
        return (
          <h1>
            Dernière consultation :
          </h1>
        );
    }
}

const DocViewer = () => {
  // Path to your .docx file
  const docxFile = 'https://docs.google.com/document/d/1TrCS5lf76w8HXRZNN3EaGsnQv9zV0GFUrBTGHMl5gZs/edit#heading=h.d2sja573mg05';

  return (
    <div>
      <h1>Document Viewer</h1>
      <Viewer
        fileType="docx"
        filePath={docxFile}
        onError={e => console.log('Error:', e)}
      />
    </div>
  );
};

export default DocViewer;

ReactDOM.render(
    <React.StrictMode>
        <Titre/>
    </React.StrictMode>,
    document.getElementById('root')
  );