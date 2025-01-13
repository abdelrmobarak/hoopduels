import './index.css'
import basketball from './assets/basketball.png'

interface AppProps {
  setShowApp: (show: boolean) => void;
  setShowResults: (show: boolean) => void;
}

function App({ setShowApp, setShowResults }: AppProps) {

  function resultsClick() {
    setShowApp(false);
    setShowResults(true);
  }

  return (
    <>
      <div className='flex min-h-screen justify-center items-center'>
        <h1 className='absolute flex flex-col items-center text-8xl font-bold text-orange font-karantina self-start py-8'>
          Hoop Duels
          <img className='w-36' src={basketball}></img>
        </h1>
      <div className='min-h-screen flex items-end py-24'>
      <div className='flex space-x-16 text-5xl font-bold'>
          <div className='flex flex-col items-center space-y-8 font-karantina'>
            <div className='w-64 h-64 bg-orange rounded-xl'></div>
            <input type='text' className='bg-grape text-stone text-center rounded-xl' placeholder='Enter Player One'></input>
          </div>
        <button className='bg-deepblue text-limegreen text-2xl w-32 h-32 rounded-2xl mt-16' onClick={resultsClick}>CLICK TO COMPARE</button>
        <div className='flex flex-col items-center space-y-8 font-karantina'>
        <div className='w-64 h-64 bg-orange rounded-xl'></div>
        <input type='text' className='bg-grape text-stone text-center rounded-xl' placeholder='Enter Player Two'></input>
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
