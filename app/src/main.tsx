import { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'
import App from './App.tsx'
import Results from './Results.tsx'


const root = ReactDOM.createRoot(document.getElementById('root')!);

function Index() {
  const [showApp, setShowApp] = useState(true);
  const [showResults, setShowResults] = useState(false);

  if (showApp) {
    return(
      <>
      <App setShowApp={setShowApp} setShowResults={setShowResults}/>
      </>
    )
  };

  if (showResults) {
    return(
      <>
      <Results/>
      </>
    )
  };
}

root.render(
  <Index/>
);

