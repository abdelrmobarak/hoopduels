import './index.css'
import basketball from './assets/basketball.png'

interface AppProps {
  setShowApp: React.Dispatch<React.SetStateAction<boolean>>;
  setShowResults: React.Dispatch<React.SetStateAction<boolean>>;
  setPlayerOne: React.Dispatch<React.SetStateAction<string>>;
  setPlayerTwo: React.Dispatch<React.SetStateAction<string>>;
  setDataSet: any;
}

interface DataToSend {
  variable: string;
  secondvariable: string;
}

interface ResponseData {
  status: string;
  received: string;
}


function App({ setShowApp, setShowResults, setPlayerOne, setPlayerTwo, setDataSet }: AppProps) {

  function resultsClick() {
    setShowApp(false);
    setShowResults(true);
    const first: string = ((document.getElementById('inputone') as HTMLInputElement).value);
    const second: string = ((document.getElementById('inputtwo') as HTMLInputElement).value);
    const playerOne: string = first;
    const playerTwo: string = second;
    const dataToSend: DataToSend = {variable: playerOne, secondvariable: playerTwo};
    setPlayerOne(first);
    setPlayerTwo(second);


    fetch('http://127.0.0.1:5000/process_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();  
      })
      .then((data: ResponseData) => {
        setDataSet(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  return (
    <>
      <div className='flex min-h-screen justify-center items-center'>
        <h1 className='absolute flex flex-col items-center text-8xl font-bold text-orange font-karantina self-start py-8'>
          Hoop Duels
          <img draggable='false' className='w-36' src={basketball}></img>
        </h1>
      <div className='min-h-screen flex items-end py-24'>
      <div className='flex space-x-16 text-5xl font-bold'>
          <div className='flex flex-col items-center space-y-8 font-karantina'>
            <div className='w-64 h-64 bg-orange rounded-xl'></div>
            <input type='text' className='bg-grape text-stone text-center rounded-xl' id='inputone' placeholder='Enter Player One'></input>
          </div>
        <button className='bg-deepblue text-limegreen text-2xl w-32 h-32 rounded-2xl mt-16' onClick={resultsClick}>CLICK TO COMPARE</button>
        <div className='flex flex-col items-center space-y-8 font-karantina'>
        <div className='w-64 h-64 bg-orange rounded-xl'></div>
        <input type='text' className='bg-grape text-stone text-center rounded-xl' id='inputtwo' placeholder='Enter Player Two'></input>
          </div>
      </div>
      </div>

          <footer className='absolute bottom-2 font-bold text-orange'>
            made with ❤️ by abdel-rahman mobarak
          </footer>
      </div>
    </>
  )
}

export default App
