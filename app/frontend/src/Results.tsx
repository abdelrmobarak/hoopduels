import basketball from './assets/back.png'
import { useEffect } from 'react';

interface AppProps {
    setShowApp: React.Dispatch<React.SetStateAction<boolean>>;
    setShowResults: React.Dispatch<React.SetStateAction<boolean>>;
    playerOne: string;
    playerTwo: string;
    dataSet: any;
}


function Results( { setShowApp, setShowResults, playerOne, playerTwo, dataSet }: AppProps) {

    function onBackClick() {
        setShowApp(true);
        setShowResults(false);
        window.location.reload();
    }
    
    if (dataSet.length === 2) {
        console.log(dataSet);
        const apg1: number = dataSet[0]['APG1'];
        const apg2: number = dataSet[1]['APG2'];
        const bpg1: number = dataSet[0]['BPG1'];
        const bpg2: number = dataSet[1]['BPG2'];
        const fg1: number = dataSet[0]['FG1'];
        const fg2: number = dataSet[1]['FG2'];
        const gp1: number = dataSet[0]['GP1'];
        const gp2: number = dataSet[1]['GP2'];
        const mp1: number = dataSet[0]['MP1'];
        const mp2: number = dataSet[1]['MP2'];
        const ppg1: number = dataSet[0]['PPG1'];
        const ppg2: number = dataSet[1]['PPG2'];
        const rpg1: number = dataSet[0]['RPG1'];
        const rpg2: number = dataSet[1]['RPG2'];
        const spg1: number = dataSet[0]['SPG1'];
        const spg2: number = dataSet[1]['SPG2'];
        const yearone: string = dataSet[0]['SZN1'];
        const yeartwo: string = dataSet[1]['SZN2'];

        useEffect(() => {
            const a1 = document.getElementById('points1')!;
            const a2 = document.getElementById('points2')!;
            const as1 = document.getElementById('assists1')!;
            const as2 = document.getElementById('assists2')!;
            const r1 = document.getElementById('rebounds1')!;
            const r2 = document.getElementById('rebounds2')!;
            const f1 = document.getElementById('fg1')!;
            const f2 = document.getElementById('fg2')!;
            const b1 = document.getElementById('blocks1')!;
            const b2 = document.getElementById('blocks2')!;
            const s1 = document.getElementById('steals1')!;
            const s2 = document.getElementById('steals2')!;
            const m1 = document.getElementById('minutes1')!;
            const m2 = document.getElementById('minutes2')!;
            const g1 = document.getElementById('games1')!;
            const g2 = document.getElementById('games2')!;

            // Points per game comparison
            if (ppg1 > ppg2) {
                a1.classList.add('text-limegreen');
                a2.classList.add('text-red');
            } else if (ppg1 < ppg2) {
                a2.classList.add('text-limegreen');
                a1.classList.add('text-red');
            } else {
                a1.classList.add('text-stone');
                a2.classList.add('text-stone');
            }
            
            // Assists per game comparison
            if (apg1 > apg2) {
                as1.classList.add('text-limegreen');
                as2.classList.add('text-red');
            } else if (apg1 < apg2) {
                as2.classList.add('text-limegreen');
                as1.classList.add('text-red');
            } else {
                as1.classList.add('text-stone');
                as2.classList.add('text-stone');
            }
            
            // Blocks per game comparison
            if (bpg1 > bpg2) {
                b1.classList.add('text-limegreen');
                b2.classList.add('text-red');
            } else if (bpg1 < bpg2) {
                b2.classList.add('text-limegreen');
                b1.classList.add('text-red');
            } else {
                b1.classList.add('text-stone');
                b2.classList.add('text-stone');
            }
            
            // Field goals comparison
            if (fg1 > fg2) {
                f1.classList.add('text-limegreen');
                f2.classList.add('text-red');
            } else if (fg1 < fg2) {
                f2.classList.add('text-limegreen');
                f1.classList.add('text-red');
            } else {
                f1.classList.add('text-stone');
                f2.classList.add('text-stone');
            }
            
            // Games played comparison
            if (gp1 > gp2) {
                g1.classList.add('text-limegreen');
                g2.classList.add('text-red');
            } else if (gp1 < gp2) {
                g2.classList.add('text-limegreen');
                g1.classList.add('text-red');
            } else {
                g1.classList.add('text-stone');
                g2.classList.add('text-stone');
            }
            
            // Minutes played comparison
            if (mp1 > mp2) {
                m1.classList.add('text-limegreen');
                m2.classList.add('text-red');
            } else if (mp1 < mp2) {
                m2.classList.add('text-limegreen');
                m1.classList.add('text-red');
            } else {
                m1.classList.add('text-stone');
                m2.classList.add('text-stone');
            }
            
            // Rebounds per game comparison
            if (rpg1 > rpg2) {
                r1.classList.add('text-limegreen');
                r2.classList.add('text-red');
            } else if (rpg1 < rpg2) {
                r2.classList.add('text-limegreen');
                r1.classList.add('text-red');
            } else {
                r1.classList.add('text-stone');
                r2.classList.add('text-stone');
            }
            
            // Steals per game comparison
            if (spg1 > spg2) {
                s1.classList.add('text-limegreen');
                s2.classList.add('text-red');
            } else if (spg1 < spg2) {
                s2.classList.add('text-limegreen');
                s1.classList.add('text-red');
            } else {
                s1.classList.add('text-stone');
                s2.classList.add('text-stone');
            }}, []);

            return(
                <div className='min-h-screen flex justify-center items-center space-x-8 py-12 flex-wrap'>
                    <div className='flex flex-col text-center items-center mb-8 w-1/3'>
                        <div className='font-bold'>
                            <h1 className='font-karantina text-6xl'>{playerOne}</h1>
                            <h1 className='font-karantina text-5xl text-stone'>{yearone}</h1>
                            <div className='mt-4 text-5xl space-y-2'>
                                <h1 id='points1'>{ppg1}</h1>
                                <h1 id='assists1'>{apg1}</h1>
                                <h1 id='rebounds1'>{rpg1}</h1>
                                <h1 id='fg1'>{fg1}</h1>
                                <h1 id='steals1'>{spg1}</h1>
                                <h1 id='blocks1'>{bpg1}</h1>
                                <h1 id='minutes1'>{mp1}</h1>
                                <h1 id='games1'>{gp1}</h1>
                            </div>
                        </div>
                    </div>
            
                    <div className='flex flex-col text-center items-center mb-8'>
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
            
                    <div className='flex flex-col text-center items-center mb-8 w-1/3'>
                        <div className='font-bold text-6xl'>
                            <h1 className='font-karantina text-6xl'>{playerTwo}</h1>
                            <h1 className='text-5xl text-stone font-karantina'>{yeartwo}</h1>
                            <div className='mt-4 text-5xl space-y-2'>
                                <h1 id='points2'>{ppg2}</h1>
                                <h1 id='assists2'>{apg2}</h1>
                                <h1 id='rebounds2'>{rpg2}</h1>
                                <h1 id='fg2'>{fg2}</h1>
                                <h1 id='steals2'>{spg2}</h1>
                                <h1 id='blocks2'>{bpg2}</h1>
                                <h1 id='minutes2'>{mp2}</h1>
                                <h1 id='games2'>{gp2}</h1>
                            </div>
                        </div>
                    </div>
                </div>
            );
                   
    }
}

export default Results;