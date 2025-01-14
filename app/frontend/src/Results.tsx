import basketball from './assets/back.png'

interface AppProps {
    setShowApp: (show: boolean) => void;
    setShowResults: (show: boolean) => void;
}

function Results( { setShowApp, setShowResults }: AppProps) {

    function onBackClick() {
        setShowApp(true);
        setShowResults(false);
    }

    return(
    <div className='min-h-screen flex justify-center space-x-8 py-12 text-wrap'>
        <div className='flex flex-col text-center text-6xl'>
            <div className='font-karantina font-bold'>
                <h1>LeBron James in Year X</h1>
                <h1 className='text-5xl text-stone'>2023-2024</h1>
            </div>
        </div>

        <div className='flex flex-col text-center items-center'>
            <img draggable='false' onClick={onBackClick} className='w-32 h-32 hover:cursor-pointer' src={basketball}></img>
                <div className='text-2xl space-y-6 py-16 font-bold'>
                <h1>Points per Game</h1>
                <h1>Assists per Game</h1>
                <h1>Rebounds per Game</h1>
                <h1>Field Goal Percentage</h1>
                <h1>Steals per Game</h1>
                <h1>Blocks per Game</h1>
                <h1>Minutes Played</h1>
                <h1>Games Played</h1>
            </div>
        </div>

        <div className='flex flex-col text-center text-4xl'>
            <div className='font-karantina font-bold text-6xl'>
                <h1>Stephen Curry in Year X</h1>
                <h1 className='text-5xl text-stone'>2023-2024</h1>
            </div>
        </div>
    </div>
    );
}

export default Results;