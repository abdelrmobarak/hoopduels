import { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'
import App from './App.tsx'
import Results from './Results.tsx'


const root = ReactDOM.createRoot(document.getElementById('root')!);

function Index() {
  const [showApp, setShowApp] = useState(true);
  const [showResults, setShowResults] = useState(false);
  const [playerOne, setPlayerOne] = useState('');
  const [playerTwo, setPlayerTwo] = useState('');
  const [dataSet, setDataSet] = useState([]);
  
  if (showApp) {
    return(
      <>
      <App setShowApp={setShowApp} setShowResults={setShowResults} 
      setPlayerOne={setPlayerOne} setPlayerTwo={setPlayerTwo}
      setDataSet={setDataSet}/>
      </>
    )
  };

  if (showResults) {
    return(
      <>
      <Results setShowApp={setShowApp} setShowResults={setShowResults} 
      playerOne={playerOne} 
      playerTwo={playerTwo} dataSet={dataSet}/>
      </>
    )
  };
}

root.render(
  <Index/>
);

